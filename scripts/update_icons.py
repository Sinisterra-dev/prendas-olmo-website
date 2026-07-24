import os
import re

def update_files():
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Add FontAwesome if missing
                fa_tag = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />'
                if 'font-awesome' not in content:
                    content = content.replace('</head>', f'    {fa_tag}\n</head>')

                # 2. Replace the icons
                # The exact string from my previous script was:
                old_icons = '''<div class="flex gap-4">
<a class="hover:text-primary transition-colors" href="#"><span class="material-symbols-outlined">qr_code_2</span></a>
<a class="hover:text-primary transition-colors" href="#"><span class="material-symbols-outlined">camera</span></a>
</div>'''
                new_icons = '''<div class="flex gap-4 text-2xl">
<a class="hover:text-primary transition-colors" href="#" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
<a class="hover:text-primary transition-colors" href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
<a class="hover:text-primary transition-colors" href="#" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a>
</div>'''

                content = content.replace(old_icons, new_icons)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

update_files()
