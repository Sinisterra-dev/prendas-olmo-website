import os
import re

def update_files():
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Determine link prefix based on file location
                # if it's ./index.html, prefix is ''
                # if it's ./mujer/index.html, prefix is '../'
                is_root = (os.path.abspath(filepath) == os.path.abspath('index.html'))
                link_prefix = '' if is_root else '../'

                # 1. Update copyright year
                content = content.replace('2024 Prendas Olmo', '2026 Prendas Olmo')

                # 2. Add favicon if missing
                favicon_tag = f'<link rel="icon" href="{link_prefix}favicon.ico" />'
                if 'rel="icon"' not in content:
                    content = content.replace('</head>', f'    {favicon_tag}\n</head>')
                else:
                    # Optional: Could replace existing favicon but let's just make sure year and footer is right
                    pass

                # 3. Replace footer
                # Find the footer start and end
                footer_start = content.find('<footer')
                footer_end = content.find('</footer>', footer_start)
                if footer_start != -1 and footer_end != -1:
                    new_footer = f'''<footer class="bg-surface-container-lowest dark:bg-primary-container text-on-surface dark:text-on-primary-container border-t border-outline-variant dark:border-outline">
<div class="grid grid-cols-1 md:grid-cols-2 gap-gutter px-margin-desktop max-w-container-max-width mx-auto py-stack-lg">
<div class="col-span-1">
<div class="flex items-center gap-3 mb-6">
<!-- TODO: Reemplazar con imagen local en assets/images/logo.png (Recomendado: 200x50 px) -->
<img alt="Logo" class="h-10 w-auto" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBwBAeZ8y924m4t1BQ2pdx3Di18N6_3PUbrsblNvlsa1hq2Q9eOUXxbWtSEEym663UEg-xz6XMHmCyw4XjKtlrSJyh1MCHnaTXQvkP2HdWxe-oVlE0iwmaOVsBVk3ShfxdAxA8zfiuzaMng1jQbkKUNvyfTmRM1CaZ6jMkAVVzVhikUTjZolRBmr9AssU1_Ad5R3CZ81PHdHDUeLF7QmuaxL16FF8r9vm5NxBP45p1_rHipRc4IOOfv9LWYvyqZv0YcTNaDBkA87mM"/>
<span class="font-headline-md text-primary dark:text-primary-fixed">Prendas Olmo</span>
</div>
<p class="font-body-md opacity-70 mb-6">Moda consciente y sofisticada para el estilo de vida contemporáneo.</p>
</div>
<div class="col-span-1 md:justify-self-end">
<h4 class="font-label-caps text-label-caps mb-6 text-primary">Contacto y Síguenos</h4>
<ul class="space-y-3 mb-6">
<li><a class="font-body-md text-on-surface-variant hover:text-primary transition-colors" href="{link_prefix}contacto/">Contacto</a></li>
</ul>
<div class="flex gap-4">
<a class="hover:text-primary transition-colors" href="#"><span class="material-symbols-outlined">qr_code_2</span></a>
<a class="hover:text-primary transition-colors" href="#"><span class="material-symbols-outlined">camera</span></a>
</div>
</div>
</div>
<div class="border-t border-outline-variant px-margin-desktop max-w-container-max-width mx-auto py-6 flex flex-col md:flex-row justify-between items-center opacity-60">
<p class="font-body-md">© 2026 Prendas Olmo. Todos los derechos reservados.</p>
</div>
</footer>'''
                    content = content[:footer_start] + new_footer + content[footer_end + 9:]

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

update_files()
