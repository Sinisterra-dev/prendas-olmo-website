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
