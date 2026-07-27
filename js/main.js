/* ===================================
   JavaScript for Prendas Olmo
   =================================== */

// Reveal animation on scroll
const reveals = document.querySelectorAll('.reveal');

const revealOnScroll = () => {
    reveals.forEach(element => {
        const windowHeight = window.innerHeight;
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        if (elementTop < windowHeight - elementVisible) {
            element.classList.add('active');
        }
    });
};

window.addEventListener('scroll', revealOnScroll);
revealOnScroll(); // Initial check

// Header shadow on scroll (for index.html)
const header = document.querySelector('header');
if (header) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('shadow-md');
            header.classList.remove('h-20');
            header.classList.add('h-16');
        } else {
            header.classList.remove('shadow-md');
            header.classList.remove('h-16');
            header.classList.add('h-20');
        }
    });
}

// Micro-interaction for scroll header (for para_mujer.html)
const mujerHeader = document.querySelector('header');
if (mujerHeader) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            mujerHeader.classList.add('h-16', 'shadow-sm');
            mujerHeader.classList.remove('h-20');
        } else {
            mujerHeader.classList.remove('h-16', 'shadow-sm');
            mujerHeader.classList.add('h-20');
        }
    });
}

// Micro-interactions for nav scroll (for para_hombre.html)
const nav = document.querySelector('nav');
if (nav) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.classList.add('h-16');
            nav.classList.remove('h-20');
            nav.classList.add('bg-white/90', 'backdrop-blur-md');
        } else {
            nav.classList.remove('h-16');
            nav.classList.add('h-20');
            nav.classList.remove('bg-white/90', 'backdrop-blur-md');
        }
    });
}

// Simple Scroll Reveal Logic (for nosotros.html)
const nosotrosReveals = document.querySelectorAll('.reveal');

const nosotrosRevealOnScroll = () => {
    const windowHeight = window.innerHeight;
    nosotrosReveals.forEach(reveal => {
        const elementTop = reveal.getBoundingClientRect().top;
        const elementVisible = 150;
        if (elementTop < windowHeight - elementVisible) {
            reveal.classList.add('active');
        }
    });
};

window.addEventListener('scroll', nosotrosRevealOnScroll);
window.onload = nosotrosRevealOnScroll;

// Micro-interactions Script for header scroll (for nueva_coleccion.html)
const coleccionHeader = document.querySelector('header');
if (coleccionHeader) {
    document.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            coleccionHeader.classList.add('h-16', 'shadow-sm');
            coleccionHeader.classList.remove('h-20');
        } else {
            coleccionHeader.classList.add('h-20');
            coleccionHeader.classList.remove('h-16', 'shadow-sm');
        }
    });
}

// Subtle scroll behavior for header (for ofertas.html)
const ofertasNav = document.querySelector('nav');
if (ofertasNav) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            ofertasNav.classList.add('shadow-sm');
            ofertasNav.classList.remove('h-20');
            ofertasNav.classList.add('h-16');
        } else {
            ofertasNav.classList.remove('shadow-sm');
            ofertasNav.classList.add('h-20');
            ofertasNav.classList.remove('h-16');
        }
    });
}

// Simple Fade In Intersection Observer (for ofertas.html)
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('opacity-100', 'translate-y-0');
            entry.target.classList.remove('opacity-0', 'translate-y-10');
        }
    });
}, observerOptions);

document.querySelectorAll('.group').forEach(el => {
    el.classList.add('transition-all', 'duration-1000', 'opacity-0', 'translate-y-10');
    observer.observe(el);
});

// ===================================
// Mobile Menu (Minimal Implementation)
// ===================================

const menuButton = document.querySelector('button.md\\:hidden');
let mobileMenu = null;
let mobileMenuOverlay = null;

if (menuButton) {
    // Create mobile menu
    mobileMenu = document.createElement('div');
    mobileMenu.style.cssText = 'position:fixed;top:80px;left:0;right:0;background:#fcf9f8;border-bottom:1px solid #cfc4c5;transform:translateY(-100%);opacity:0;visibility:hidden;transition:all 0.3s ease;z-index:40;box-shadow:0 4px 6px rgba(0,0,0,0.1);';
    
    // Get current page path
    const currentPath = window.location.pathname;
    const isRoot = currentPath === '/' || currentPath.endsWith('/index.html');
    
    // Menu items
    const menuItems = [
        { text: 'Inicio', href: isRoot ? '/' : '../' },
        { text: 'Mujer', href: isRoot ? 'mujer/' : '../mujer/' },
        { text: 'Hombre', href: isRoot ? 'hombre/' : '../hombre/' },
        { text: 'Colecciones', href: isRoot ? 'colecciones/' : '../colecciones/' },
        { text: 'Ofertas', href: isRoot ? 'ofertas/' : '../ofertas/' },
        { text: 'Nosotros', href: isRoot ? 'nosotros/' : '../nosotros/' },
        { text: 'Contacto', href: isRoot ? 'contacto/' : '../contacto/' }
    ];
    
    // Add links to menu
    menuItems.forEach(item => {
        const link = document.createElement('a');
        link.href = item.href;
        link.textContent = item.text;
        link.style.cssText = 'display:block;padding:16px 20px;font-family:Montserrat,sans-serif;font-size:14px;letter-spacing:0.15em;font-weight:600;text-transform:uppercase;color:#1c1b1b;text-decoration:none;border-bottom:1px solid #e5e2e1;';
        link.addEventListener('click', () => closeMenu());
        mobileMenu.appendChild(link);
    });
    
    // Create overlay
    mobileMenuOverlay = document.createElement('div');
    mobileMenuOverlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.5);opacity:0;visibility:hidden;transition:all 0.3s ease;z-index:35;';
    mobileMenuOverlay.addEventListener('click', () => closeMenu());
    
    // Insert into DOM
    const header = document.querySelector('header') || document.querySelector('nav');
    if (header) {
        header.parentNode.insertBefore(mobileMenu, header.nextSibling);
    }
    document.body.appendChild(mobileMenuOverlay);
    
    // Toggle menu
    menuButton.addEventListener('click', () => {
        const isOpen = mobileMenu.style.transform === 'translateY(0)';
        if (isOpen) {
            closeMenu();
        } else {
            openMenu();
        }
    });
    
    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && mobileMenu.style.transform === 'translateY(0)') {
            closeMenu();
        }
    });
    
    // Close on resize
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 768 && mobileMenu.style.transform === 'translateY(0)') {
            closeMenu();
        }
    });
}

function openMenu() {
    mobileMenu.style.transform = 'translateY(0)';
    mobileMenu.style.opacity = '1';
    mobileMenu.style.visibility = 'visible';
    mobileMenuOverlay.style.opacity = '1';
    mobileMenuOverlay.style.visibility = 'visible';
    document.body.style.overflow = 'hidden';
}

function closeMenu() {
    mobileMenu.style.transform = 'translateY(-100%)';
    mobileMenu.style.opacity = '0';
    mobileMenu.style.visibility = 'hidden';
    mobileMenuOverlay.style.opacity = '0';
    mobileMenuOverlay.style.visibility = 'hidden';
    document.body.style.overflow = '';
}
