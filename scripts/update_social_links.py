from pathlib import Path
import re

# ==========================================
# CONFIGURACIÓN
# ==========================================

WHATSAPP = "https://wa.me/573008201236?text=Hola,%20quiero%20información%20sobre%20las%20prendas%20de%20Olmo."
INSTAGRAM = "https://www.instagram.com/olmo_0510"
TIKTOK = "https://www.tiktok.com/@prendasolmo"

# ==========================================
# BUSCAR TODOS LOS index.html
# ==========================================

html_files = list(Path(".").glob("index.html"))
html_files += list(Path(".").glob("*/index.html"))

print(f"\nSe encontraron {len(html_files)} archivos HTML.\n")

# ==========================================
# ACTUALIZAR ENLACES
# ==========================================

for file in html_files:

    content = file.read_text(encoding="utf-8")

    # WhatsApp
    content = re.sub(
        r'<a([^>]*?)href="#"([^>]*?)aria-label="WhatsApp"',
        rf'<a\1href="{WHATSAPP}" target="_blank" rel="noopener noreferrer"\2aria-label="WhatsApp"',
        content
    )

    # Instagram
    content = re.sub(
        r'<a([^>]*?)href="#"([^>]*?)aria-label="Instagram"',
        rf'<a\1href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer"\2aria-label="Instagram"',
        content
    )

    # TikTok
    content = re.sub(
        r'<a([^>]*?)href="#"([^>]*?)aria-label="TikTok"',
        rf'<a\1href="{TIKTOK}" target="_blank" rel="noopener noreferrer"\2aria-label="TikTok"',
        content
    )

    file.write_text(content, encoding="utf-8")
    print(f"✅ {file}")

print("\n🎉 ¡Todas las páginas fueron actualizadas correctamente!")