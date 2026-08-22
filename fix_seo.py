import re

file_path = "d:/Documentos/Oryon Agência/Site com IA/Site-psicologa-rebeka/dist/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Image Width/Height
content = content.replace(
    '<img src="assets/img/logo.png" alt="Rebeka Psicologia Clínica" class="h-10 w-auto" onerror="this.style.display=\'none\'">',
    '<img src="assets/img/logo.png" alt="Rebeka Psicologia Clínica" class="h-10 w-auto" width="200" height="80" onerror="this.style.display=\'none\'">'
)
content = content.replace(
    '<img src="assets/img/hero-bg.webp" alt="Consultório de Psicologia em Palmas" class="w-full h-full object-cover" loading="lazy" onerror="this.style.opacity=\'0\'">',
    '<img src="assets/img/hero-bg.webp" alt="Consultório de Psicologia em Palmas" class="w-full h-full object-cover" loading="lazy" width="1920" height="1080" onerror="this.style.opacity=\'0\'">'
)
content = content.replace(
    '<img src="assets/img/sobre.webp" alt="Acolhimento Ético e Humanizado" class="relative rounded-3xl shadow-xl w-full h-auto object-cover" loading="lazy" onerror="this.style.opacity=\'0\'">',
    '<img src="assets/img/sobre.webp" alt="Acolhimento Ético e Humanizado" class="relative rounded-3xl shadow-xl w-full h-auto object-cover" loading="lazy" width="800" height="1000" onerror="this.style.opacity=\'0\'">'
)
content = content.replace(
    '<img src="assets/img/servico-1.webp" alt="Identidade e Ciclos da Vida" class="w-full h-56 object-cover rounded-2xl mb-8" loading="lazy" onerror="this.style.opacity=\'0\'">',
    '<img src="assets/img/servico-1.webp" alt="Identidade e Ciclos da Vida" class="w-full h-56 object-cover rounded-2xl mb-8" loading="lazy" width="800" height="600" onerror="this.style.opacity=\'0\'">'
)
content = content.replace(
    '<img src="assets/img/servico-2.webp" alt="Maternidade e Luto Perinatal" class="w-full h-56 object-cover rounded-2xl mb-8" loading="lazy" onerror="this.style.opacity=\'0\'">',
    '<img src="assets/img/servico-2.webp" alt="Maternidade e Luto Perinatal" class="w-full h-56 object-cover rounded-2xl mb-8" loading="lazy" width="800" height="600" onerror="this.style.opacity=\'0\'">'
)
content = content.replace(
    '<img src="assets/img/servico-3.webp" alt="Esgotamento e Relações de Trabalho" class="w-full h-56 object-cover rounded-2xl mb-8" loading="lazy" onerror="this.style.opacity=\'0\'">',
    '<img src="assets/img/servico-3.webp" alt="Esgotamento e Relações de Trabalho" class="w-full h-56 object-cover rounded-2xl mb-8" loading="lazy" width="800" height="600" onerror="this.style.opacity=\'0\'">'
)
content = content.replace(
    '<img src="assets/img/servico-4.webp" alt="Desenvolvimento de Autonomia" class="w-full h-56 object-cover rounded-2xl mb-8" loading="lazy" onerror="this.style.opacity=\'0\'">',
    '<img src="assets/img/servico-4.webp" alt="Desenvolvimento de Autonomia" class="w-full h-56 object-cover rounded-2xl mb-8" loading="lazy" width="800" height="600" onerror="this.style.opacity=\'0\'">'
)
content = content.replace(
    '<img src="assets/img/beneficios.webp" alt="Espaço Seguro e Livre de Julgamentos" class="rounded-[2.5rem] shadow-2xl w-full h-auto object-cover relative z-10" loading="lazy" onerror="this.style.opacity=\'0\'">',
    '<img src="assets/img/beneficios.webp" alt="Espaço Seguro e Livre de Julgamentos" class="rounded-[2.5rem] shadow-2xl w-full h-auto object-cover relative z-10" loading="lazy" width="800" height="800" onerror="this.style.opacity=\'0\'">'
)
content = content.replace(
    '<img src="assets/img/logo.png" alt="Rebeka Psicologia Clínica" class="h-12 w-auto mb-6 filter brightness-0 invert" onerror="this.style.display=\'none\'" loading="lazy">',
    '<img src="assets/img/logo.png" alt="Rebeka Psicologia Clínica" class="h-12 w-auto mb-6 filter brightness-0 invert" width="200" height="80" onerror="this.style.display=\'none\'" loading="lazy">'
)

# 2. Fix Render-blocking fonts
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">',
    '<link rel="preload" href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"></noscript>'
)

# 3. Add ARIA tags to Mobile Menu Button
content = content.replace(
    '<button @click="open = !open" class="text-texto hover:text-primaria focus:outline-none">',
    '<button @click="open = !open" aria-label="Abrir menu" :aria-expanded="open" aria-controls="mobile-menu" class="text-texto hover:text-primaria focus:outline-none">'
)
content = content.replace(
    '<div x-show="open" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 scale-95" x-transition:enter-end="opacity-100 scale-100" x-transition:leave="transition ease-in duration-100" x-transition:leave-start="opacity-100 scale-100" x-transition:leave-end="opacity-0 scale-95" @click.away="open = false" class="absolute top-16 left-0 right-0 bg-white shadow-xl rounded-b-2xl md:hidden z-50">',
    '<div id="mobile-menu" x-show="open" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 scale-95" x-transition:enter-end="opacity-100 scale-100" x-transition:leave="transition ease-in duration-100" x-transition:leave-start="opacity-100 scale-100" x-transition:leave-end="opacity-0 scale-95" @click.away="open = false" class="absolute top-16 left-0 right-0 bg-white shadow-xl rounded-b-2xl md:hidden z-50">'
)

# 4. Add aria-hidden to all SVGs (they are decorative)
content = content.replace('<svg ', '<svg aria-hidden="true" ')

# 5. Fix FAQ ARIA attributes
for i in range(1, 9):
    content = content.replace(
        f'<button @click="active !== {i} ? active = {i} : active = null" class="w-full text-left px-8 py-6 bg-white hover:bg-fundo/50 focus:outline-none flex justify-between items-center transition-colors">',
        f'<button @click="active !== {i} ? active = {i} : active = null" :aria-expanded="active === {i} ? \'true\' : \'false\'" aria-controls="faq-answer-{i}" class="w-full text-left px-8 py-6 bg-white hover:bg-fundo/50 focus:outline-none flex justify-between items-center transition-colors">'
    )
    content = content.replace(
        f'<div x-show="active === {i}" x-collapse style="display: none;" class="px-8 pb-6 bg-white text-texto text-lg border-t border-gray-50 pt-4">',
        f'<div id="faq-answer-{i}" x-show="active === {i}" x-collapse style="display: none;" class="px-8 pb-6 bg-white text-texto text-lg border-t border-gray-50 pt-4">'
    )

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("SEO & A11y Fixes applied successfully.")
