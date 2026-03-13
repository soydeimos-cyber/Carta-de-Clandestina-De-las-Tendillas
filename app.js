document.addEventListener('DOMContentLoaded', () => {
    const menuContainer = document.getElementById('menu-container');
    const filterGroupContainer = document.getElementById('filter-group-container');
    const categoryNav = document.querySelector('.categories-nav');
    const resetBtn = document.getElementById('reset-filters');
    
    // State
    let currentCategory = 'all';
    let activeDietaryFilters = new Set(); // Stores filters like 'veg', 'allergen-Gluten', etc.

    // Verify data exists
    if (!window.menuData) {
        menuContainer.innerHTML = '<div class="empty-state"><p>Error cargando la carta. Por favor, refresque la página.</p></div>';
        return;
    }

    // Function to calculate all unique allergens from the data
    function getUniqueAllergens(data) {
        const allergensSet = new Set();
        data.forEach(dish => {
            if (dish.alergenos && Array.isArray(dish.alergenos)) {
                dish.alergenos.forEach(a => {
                    // Normalize (Capitalize first letter, rest lowercase)
                    const clean = a.trim();
                    if(clean) {
                        const formatted = clean.charAt(0).toUpperCase() + clean.slice(1).toLowerCase();
                        allergensSet.add(formatted);
                    }
                });
            }
        });
        // Sort alphabetically, optionally pull Gluten to front
        const allergensArray = Array.from(allergensSet).sort();
        const glutenIndex = allergensArray.indexOf('Gluten');
        if (glutenIndex > -1) {
            allergensArray.splice(glutenIndex, 1);
            allergensArray.unshift('Gluten');
        }
        return allergensArray;
    }

    // Function to build dynamic dietary buttons
    function buildDietaryButtons(allergens) {
        let buttonsHtml = '';
        
        allergens.forEach(allergen => {
            // Icon logic based on common allergens
            let icon = 'fa-solid fa-circle-exclamation'; 
            const lowerAllergen = allergen.toLowerCase();
            if (lowerAllergen === 'gluten') icon = 'fa-solid fa-wheat-awn-circle-exclamation';
            else if (lowerAllergen === 'lácteos' || lowerAllergen === 'leche') icon = 'fa-solid fa-cow';
            else if (lowerAllergen === 'pescado') icon = 'fa-solid fa-fish';
            else if (lowerAllergen === 'marisco' || lowerAllergen === 'crustáceos' || lowerAllergen === 'moluscos') icon = 'fa-solid fa-shrimp';
            else if (lowerAllergen.includes('sec')) icon = 'fa-solid fa-leaf';
            else if (lowerAllergen.includes('huev')) icon = 'fa-solid fa-egg';
            
            // "Libre de X" means "Safe from X"
            buttonsHtml += `
                <button class="diet-btn dynamic" data-filter="allergen-${allergen}">
                    <i class="${icon}"></i> Libre de ${allergen}
                </button>
            `;
        });

        filterGroupContainer.insertAdjacentHTML('beforeend', buttonsHtml);
    }

    // Function to set up category tabs
    function setupCategoryNav() {
        const catBtns = categoryNav.querySelectorAll('.cat-btn');
        catBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                catBtns.forEach(b => b.classList.remove('active'));
                const currentBtn = e.currentTarget;
                currentBtn.classList.add('active');
                
                currentCategory = currentBtn.dataset.category;
                renderMenu();
            });
        });
    }

    // Function to set up dietary (allergen/veg) filters as toggles
    function setupDietaryFilters() {
        const dietBtns = filterGroupContainer.querySelectorAll('.diet-btn');
        const badgeCount = document.getElementById('active-filters-count');
        
        function updateBadgeAndReset() {
            const count = activeDietaryFilters.size;
            // Show/hide reset button
            resetBtn.style.display = count > 0 ? 'block' : 'none';
            
            // Update badge
            if (count > 0) {
                badgeCount.textContent = count;
                badgeCount.style.display = 'inline-flex';
            } else {
                badgeCount.style.display = 'none';
            }
        }
        
        dietBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const currentBtn = e.currentTarget;
                const filterId = currentBtn.dataset.filter;
                
                if (activeDietaryFilters.has(filterId)) {
                    activeDietaryFilters.delete(filterId);
                    currentBtn.classList.remove('active');
                } else {
                    activeDietaryFilters.add(filterId);
                    currentBtn.classList.add('active');
                }
                
                updateBadgeAndReset();
                renderMenu();
            });
        });

        // Reset all button
        resetBtn.addEventListener('click', () => {
            activeDietaryFilters.clear();
            dietBtns.forEach(b => b.classList.remove('active'));
            updateBadgeAndReset();
            renderMenu();
        });
    }

    // Main render function integrating ALL state
    function renderMenu() {
        menuContainer.innerHTML = '';
        
        // 1. Filter by category
        let filteredData = window.menuData;
        
        if (currentCategory !== 'all') {
            filteredData = filteredData.filter(dish => 
                (dish.categoria || '').toLowerCase() === currentCategory.toLowerCase()
            );
        }

        // 2. Map through active dietary filters
        if (activeDietaryFilters.size > 0) {
            activeDietaryFilters.forEach(filterId => {
                
                if (filterId === 'veg') {
                    // Must be vegan/vegetarian compatible
                    filteredData = filteredData.filter(dish => 
                        dish.opciones_veganas_vegetarianas === true || typeof dish.opciones_veganas_vegetarianas === 'string'
                    );
                } else if (filterId.startsWith('allergen-')) {
                    const targetAllergen = filterId.replace('allergen-', '');
                    
                    filteredData = filteredData.filter(dish => {
                        const standardizedAllergens = (dish.alergenos || []).map(a => a.trim().charAt(0).toUpperCase() + a.trim().slice(1).toLowerCase());
                        const lacksAllergen = !standardizedAllergens.includes(targetAllergen);
                        
                        // Fallback for explicitly safe adaptations (mostly Gluten)
                        if (targetAllergen === 'Gluten' && !lacksAllergen) {
                             return dish.opciones_sin_gluten === true || typeof dish.opciones_sin_gluten === 'string';
                        }
                        
                        return lacksAllergen;
                    });
                }
            });
        }

        if (filteredData.length === 0) {
            menuContainer.innerHTML = `
                <div class="empty-state">
                    <i class="fa-solid fa-plate-wheat"></i>
                    <p>No se encontraron platos que coincidan con los filtros seleccionados.</p>
                </div>
            `;
            return;
        }

        filteredData.forEach((dish, index) => {
            const card = document.createElement('article');
            card.className = 'dish-card';
            card.style.animationDelay = `${index * 0.05}s`;

            // Category visual hint mapping
            let catName = "Plato";
            if(dish.categoria) {
                catName = dish.categoria.charAt(0).toUpperCase() + dish.categoria.slice(1);
            }

            // Badges HTML
            let badgesHtml = `<div class="dietary-badges">`;
            badgesHtml += `<span class="badge category-badge">${catName}</span> `;
            
            // Gluten Free Badge
            if (dish.opciones_sin_gluten === true) {
                badgesHtml += '<span class="badge gluten-free"><i class="fa-solid fa-check"></i> Sin Gluten</span>';
            } else if (typeof dish.opciones_sin_gluten === 'string') {
                badgesHtml += `<span class="badge adaptation" title="${dish.opciones_sin_gluten}"><i class="fa-solid fa-wrench"></i> Adap. Sin Gluten</span>`;
            }

            // Veg Badge
            if (dish.opciones_veganas_vegetarianas === true) {
                badgesHtml += '<span class="badge vegan"><i class="fa-solid fa-leaf"></i> Veg / Vegano</span>';
            } else if (typeof dish.opciones_veganas_vegetarianas === 'string') {
                badgesHtml += `<span class="badge adaptation" title="${dish.opciones_veganas_vegetarianas}"><i class="fa-solid fa-wrench"></i> Adap. Vegana</span>`;
            }
            badgesHtml += '</div>';

            // Allergens HTML
            let allergensHtml = '';
            if (dish.alergenos && dish.alergenos.length > 0) {
                allergensHtml = `
                    <div class="allergens-container">
                        <span class="allergens-label">Alérgenos:</span>
                        <div class="allergens-list">
                            ${dish.alergenos.map(a => `<span class="allergen-tag">${a}</span>`).join('')}
                        </div>
                    </div>
                `;
            }

            // Photo HTML logic
            const hasRealPhoto = dish.foto && dish.foto !== "placeholder.jpg" && !dish.foto.includes("Gemini_Generated_Image");
            const photoContent = hasRealPhoto 
                ? `<img src="photos/${dish.foto}" alt="${dish.nombre}" class="dish-photo" onerror="this.parentElement.innerHTML='<div class=\\'photo-placeholder\\'><i class=\\'fa-regular fa-image\\'></i><span>Foto no disponible</span></div>'">`
                : `<div class="photo-placeholder"><i class="fa-solid fa-camera-rotate"></i><span>Foto próximamente</span></div>`;

            // Description HTML
            let descHtml = `<div class="dish-description">${dish.descripcion || 'Sin descripción disponible.'}`;
            
            // Add adaptation notices if filtered and dish needs adaptation
            if (typeof dish.opciones_sin_gluten === 'string') {
                descHtml += `<span class="adaptation-notice"><i class="fa-solid fa-circle-info"></i> Nota Sin Gluten: ${dish.opciones_sin_gluten}</span>`;
            }
            if (typeof dish.opciones_veganas_vegetarianas === 'string') {
                descHtml += `<span class="adaptation-notice"><i class="fa-solid fa-circle-info"></i> Nota Vegana: ${dish.opciones_veganas_vegetarianas}</span>`;
            }
            descHtml += `</div>`;

            card.innerHTML = `
                <div class="dish-header">
                    <h2 class="dish-title">${dish.nombre}</h2>
                    <span class="dish-price">${dish.precio}€</span>
                </div>
                
                ${badgesHtml}
                ${allergensHtml}
                
                <div class="dish-actions" style="margin-top: auto; padding-top: 1rem;">
                    <button class="action-btn toggle-photo">
                        <i class="fa-solid fa-image"></i> Foto
                    </button>
                    <button class="action-btn toggle-desc">
                        <i class="fa-solid fa-file-lines"></i> Info
                    </button>
                </div>
                
                <div class="dropdown-content photo-dropdown">
                    <div class="dish-photo-container">
                        ${photoContent}
                    </div>
                </div>
                
                <div class="dropdown-content desc-dropdown">
                    ${descHtml}
                </div>
            `;

            menuContainer.appendChild(card);

            // Add Event Listeners for Dropdowns
            const btnPhoto = card.querySelector('.toggle-photo');
            const dropPhoto = card.querySelector('.photo-dropdown');
            const btnDesc = card.querySelector('.toggle-desc');
            const dropDesc = card.querySelector('.desc-dropdown');

            btnPhoto.addEventListener('click', () => {
                const isActive = dropPhoto.classList.contains('show');
                dropDesc.classList.remove('show');
                btnDesc.classList.remove('active');
                
                if (isActive) {
                    dropPhoto.classList.remove('show');
                    btnPhoto.classList.remove('active');
                } else {
                    dropPhoto.classList.add('show');
                    btnPhoto.classList.add('active');
                }
            });

            btnDesc.addEventListener('click', () => {
                const isActive = dropDesc.classList.contains('show');
                dropPhoto.classList.remove('show');
                btnPhoto.classList.remove('active');
                
                if (isActive) {
                    dropDesc.classList.remove('show');
                    btnDesc.classList.remove('active');
                } else {
                    dropDesc.classList.add('show');
                    btnDesc.classList.add('active');
                }
            });
        });
    }

    // Initialization
    function init() {
        const uniqueAllergens = getUniqueAllergens(window.menuData);
        buildDietaryButtons(uniqueAllergens);
        setupCategoryNav();
        setupDietaryFilters();
        renderMenu();
    }

    init();
});
