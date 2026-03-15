document.addEventListener('DOMContentLoaded', () => {
    const rawData = window.menuData || [];
    const container = document.getElementById('app-container');

    // Mapear los datos de data.js al formato "carta"
    const carta = {
        divertimentos: [],
        entrantes: [],
        principales: [],
        postres: []
    };

    let counters = { DIV: 1, ENT: 1, PRI: 1, POS: 1 };

    rawData.forEach(item => {
        const cat = (item.categoria || "").toLowerCase();
        let prefix = "PRI";
        let targetArray = carta.principales;

        if (cat.includes('divertimento')) { prefix = "DIV"; targetArray = carta.divertimentos; }
        else if (cat.includes('entrante')) { prefix = "ENT"; targetArray = carta.entrantes; }
        else if (cat.includes('postre')) { prefix = "POS"; targetArray = carta.postres; }

        const mappedItem = {
            id: `${prefix}-${String(counters[prefix]++).padStart(3, '0')}`,
            nombre: item.nombre,
            descripcion: item.descripcion ? item.descripcion.trim() : "",
            alergenos: item.alergenos || [],
            imagen: item.foto ? `photos/${item.foto}` : null,
            precio: item.precio
        };

        targetArray.push(mappedItem);
    });

    const categoryTitles = {
        divertimentos: 'Divertimentos',
        entrantes: 'Entrantes',
        principales: 'Principales',
        postres: 'Postres'
    };

    let htmlContent = '';

    Object.keys(carta).forEach(categoryKey => {
        const items = carta[categoryKey];
        if (items.length === 0) return;

        htmlContent += `
            <section class="mb-12">
                <h2 class="text-2xl font-bold text-gray-800 mb-6 pb-2 border-b-2 border-gray-200 capitalize tracking-tight">
                    ${categoryTitles[categoryKey] || categoryKey}
                </h2>
                <!-- Grid: 1 col on mobile, 2 cols on tablet (sm:grid-cols-2), 3 cols on large desktop (lg:grid-cols-3) -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        `;

        items.forEach(dish => {
            const hasDesc = dish.descripcion && dish.descripcion.length > 0;
            const hasAllergens = dish.alergenos && dish.alergenos.length > 0;
            
            const descId = `desc-${dish.id}`;
            const alloId = `allo-${dish.id}`;

            const imageSrc = dish.imagen ? dish.imagen : '';
            const fallbackHTML = `<div class="w-full h-52 bg-gray-200 flex items-center justify-center text-gray-500 text-sm">Sin imagen</div>`;
            const imageHTML = dish.imagen 
                ? `<img src="${imageSrc}" alt="${dish.nombre}" class="w-full h-52 object-cover cursor-pointer hover:opacity-90 transition-opacity" onclick="openModal('${imageSrc}', '${dish.nombre.replace(/'/g, "\\'")}')" onerror="this.onerror=null; this.outerHTML='${fallbackHTML.replace(/"/g, '&quot;')}';">`
                : fallbackHTML;

            // Accordion 1: Descripción
            let descAccordion = '';
            if (hasDesc) {
                descAccordion = `
                    <div class="border-b border-gray-100">
                        <button class="w-full py-3 flex justify-between items-center text-left font-semibold text-gray-700 hover:text-gray-900 focus:outline-none" aria-expanded="false" aria-controls="${descId}" onclick="toggleAccordion(this, '${descId}')">
                            <span>Descripción</span>
                            <span class="accordion-icon text-sm text-gray-500 transition-transform duration-300">▼</span>
                        </button>
                        <div id="${descId}" class="accordion-content">
                            <div class="accordion-inner text-sm text-gray-600 pb-3 leading-relaxed">
                                ${dish.descripcion}
                            </div>
                        </div>
                    </div>
                `;
            } else {
                descAccordion = `
                    <div class="border-b border-gray-100 py-3">
                        <span class="text-sm text-gray-400 italic">Descripción no disponible</span>
                    </div>
                `;
            }

            // Accordion 2: Alérgenos
            let alloAccordion = '';
            if (hasAllergens) {
                const chipsHtml = dish.alergenos.map(a => `<span class="inline-block bg-gray-100 text-gray-700 text-xs px-2 py-1 rounded-full font-medium tracking-wide border border-gray-200 uppercase">${a}</span>`).join(' ');
                alloAccordion = `
                    <div>
                        <button class="w-full py-3 flex justify-between items-center text-left font-semibold text-gray-700 hover:text-gray-900 focus:outline-none" aria-expanded="false" aria-controls="${alloId}" onclick="toggleAccordion(this, '${alloId}')">
                            <span>Alérgenos</span>
                            <span class="accordion-icon text-sm text-gray-500 transition-transform duration-300">▼</span>
                        </button>
                        <div id="${alloId}" class="accordion-content">
                            <div class="accordion-inner pb-3 flex flex-wrap gap-2">
                                ${chipsHtml}
                            </div>
                        </div>
                    </div>
                `;
            }

            htmlContent += `
                <article class="dish-card bg-white rounded-xl shadow-md overflow-hidden flex flex-col border border-gray-100">
                    <!-- Fotografía -->
                    <div class="w-full">
                        ${imageHTML}
                    </div>
                    <!-- Contenido -->
                    <div class="p-5 flex-grow flex flex-col">
                        <div class="flex justify-between items-start gap-4 mb-4">
                            <h3 class="text-lg font-bold text-gray-900 leading-tight">${dish.nombre}</h3>
                            ${dish.precio ? `<span class="text-lg font-bold text-blue-600 shrink-0">${dish.precio.toFixed(2)}€</span>` : ''}
                        </div>
                        
                        <!-- Interacciones -->
                        <div class="mt-auto border-t border-gray-100 pt-2">
                            ${descAccordion}
                            ${alloAccordion}
                        </div>
                    </div>
                </article>
            `;
        });

        htmlContent += `
                </div>
            </section>
        `;
    });

    if (htmlContent === '') {
        htmlContent = `<p class="text-center text-gray-500 py-10">No hay platos disponibles.</p>`;
    }

    container.innerHTML = htmlContent;
});

// Accordion toggle function
window.toggleAccordion = function(button, panelId) {
    const isExpanded = button.getAttribute('aria-expanded') === 'true';
    const panel = document.getElementById(panelId);
    const icon = button.querySelector('.accordion-icon');
    
    // Toggle ARIA state
    button.setAttribute('aria-expanded', !isExpanded);
    
    // Toggle visual state
    if (!isExpanded) {
        panel.classList.add('open');
        icon.classList.add('open');
        icon.textContent = '▲';
    } else {
        panel.classList.remove('open');
        icon.classList.remove('open');
        icon.textContent = '▼';
    }
};

// Image Modal Functions
window.openModal = function(src, alt) {
    const modal = document.getElementById('image-modal');
    const modalImg = document.getElementById('modal-image');
    if (modal && modalImg) {
        modalImg.src = src;
        modalImg.alt = alt;
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden'; // Prevent scrolling
    }
};

window.closeModal = function() {
    const modal = document.getElementById('image-modal');
    if (modal) {
        modal.classList.add('hidden');
        document.body.style.overflow = ''; // Restore scrolling
    }
};
