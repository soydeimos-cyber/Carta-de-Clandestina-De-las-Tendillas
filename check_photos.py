import urllib.request
import os

images = [
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAw8MuvBinwGgLvdX8j3NJwUvphavfAJ_RZLROhh3yHFFFISN8kPBbv5_PdXns5KPe4FeA02bx48MTNzbKxRrwx9iTfHH32pOAlSYgomhbuudM0rjOXYU7BfLf8egTDTbXNTjTuV", "Albondigas de Ciervo.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAx5RRSoJ0wbWop6Pq5X-KbZwe2xOLPTF_6QnGR4m8vwn755aCiGS8orfl5injFc9Hhew3EdGPNz-xVga0sK5jnHmtx8YvvCk1FXGCMldf0kSmBh574vwhUGpwi72_nzGzaY0Y5LFQ", "Gilda.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAw5TN4HjhruILiKEFg4LZKtYEQlXS5hTM9BtPCGBC7tSJdh_zcaOJ5hxP2BtwiMv9xa0EONSCcVo7Epn6gK_ViYmXWG6zv54hD7q-zDpSyeggQj-CzR7MM0ZG9ac2-YitrX4KC_", "anchoa 00.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAxS3I7bZ0vA4Tf5zI0sA_r1xHq1yM-Hq5S12X5zBw8lBx3I6uV9v2pY6a4wAByS6X9P0f7PZgY1H-HqV8_S1qLwH2T_5Vq8sHz5H_y", "crujiente de bacalao.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAwhzPcxz9uL9B2d4f8_jQvZl86H6Q99v9l_R8z-1q_Jp21H9-nQo0Wqg7bH25Yk5P2Y6Z_9qJw3_J7r_e9q18Qz_W5d6Pq9z4Fz5CgV", "Gemini_Generated_Image_58w37d58w37d58w3.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAzi2a0S5fQ-mZ7B-1s0bWcK8A7hN3k_XgA2yD_P0r0lR5bW4T_3n8G_b8L2zQ7P0V-O4fUa7Lg1F2qV3xN2qK4x-G-u1bVp8u3-6X2h", "Ensaladilla.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAwN6K8qF8_K3_eN2fA3k_aU5Q7gH2jH3_D9u_P1sU3gB7vY3-bQ9tM3q0Wj-bN3q-nL0bV5vT_J3_mK_k9v0zF_2FqW8oN9L8c7b8C", "ensalala de perdiz.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAzH9Q3W0M5A9fS9r8A2qJkZ2L7Q4F6g6X8L3N8qK0bN7_mQ8D5nI9J2lT2rG1L7dY6N9fQ4nS2mK-u4fG2vM-l4-H2xZt2V2pA4U0O", "Callos.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAyG7wD5F8nQj2T2u_Z2g_yD9M5gA6sL8X-Z1T4lR1_zL4kX_aM_q_k_F2Z6y8Q2gJ3bT9zN8sY2bO3X4h_G4mV2gD5bL9O4N2V_9M", "Arroz de Changurro.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAyH4r_Q1kR_O9lG2qR5K-dG9_gS1mD9_g-w_uM4V-hI5aF8cQ-J2sN5aZ_N5oG5j_K3xQ2bK9T_dM-xK5oK8I1nF_pA4u-S5O9H1X", "Steak Tartar.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAyK2V7W3G_bX0_K4B0jQ0o_Z0mI_H1A_l5_X3k_Q0kL0jT8q0hV0Y7jW8dK9jH1N-K5Q3-J_K_gI0M-tK_8hQ1I_D4mX8W5_B7x0Z", "Presa Iberica.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAyQ2I9V-T3Z7qM_8U_xQ1iG_X1F1_Q9-V1bK5jA0_fB9T7yO9G6pK-aK8v2S0L4rT5kN2eC1yS5x_Q_H_wA9vH0-wK7U_n_P3aH2d", "Cochinillo.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAyX7-rX_bJ8xG_gI2mA3-t-O3Q9S1sH8aB-cM_K7zU_5sQ-V_yJ8bU_eM_t-D4_U9mY8hB_aT9R4tD2K_6lF_eH4R3_nE-fA_a_tJ", "Bacalao en Témpura.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAwR2_bA5y_V9N-wG0G_z5N_6qF0L0x-T_7uP8tJ5_E1zH_aW_2gJ8E0c_e1G4R_sD-R5gH_jV1A0yH9wW-mB7cR-O_1D_wW5wA9A", "Ruibarbo.jpeg"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAyS-7G-X0T-H2M4_zD4pB_9sA0yF_Q5q_aB2mJ8jW0_pU7_G9s-Y7gI-gI8gU7rQ7rL-Y4uC_6D-fX-X-gS4_B4eA_Z9D8O_5Z0N", "Cúpula Chocolate.jpeg")
]

# Note: NotebookLM links need to be found for download. Let's see if the old query fetched all. I'll just check if they are already downloaded or not. Let me use mcp_notebooklm_source_get_content

print("Check existing...")
for x in images:
    if os.path.exists(os.path.join("photos", x[1])):
        print(f"Exists: {x[1]}")
    else:
        print(f"Missing: {x[1]}")
