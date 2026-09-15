/**
 * MUHAMMED FAYIS - PORTFOLIO INTERACTION ENGINE
 * Premium Engineering Consultancy & Project Management
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileNav();
  initActiveNavObserver();
  initScrollReveal();
  initContactForm();
  initBackToTop();
  initPortraitParallax();
  disableVideoPiP();
});

/**
 * Disable Picture-in-Picture on hero video
 */
function disableVideoPiP() {
  const video = document.getElementById('heroPortraitVideo');
  if (video) {
    video.disablePictureInPicture = true;
  }
}

/**
 * 1. Sticky Navigation Bar with Scroll Threshold
 */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/**
 * 2. Mobile Navigation Drawer & Toggle
 */
function initMobileNav() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');
  const backdrop = document.getElementById('navBackdrop');
  const closeBtn = document.getElementById('mobileSidebarClose');

  if (!toggleBtn || !navMenu) return;

  const openSidebar = () => {
    navMenu.classList.add('is-open');
    toggleBtn.classList.add('is-active');
    toggleBtn.setAttribute('aria-expanded', 'true');
    if (backdrop) backdrop.classList.add('is-active');
    document.body.style.overflow = 'hidden';
  };

  const closeSidebar = () => {
    navMenu.classList.remove('is-open');
    toggleBtn.classList.remove('is-active');
    toggleBtn.setAttribute('aria-expanded', 'false');
    if (backdrop) backdrop.classList.remove('is-active');
    document.body.style.overflow = '';
  };

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (navMenu.classList.contains('is-open')) {
      closeSidebar();
    } else {
      openSidebar();
    }
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeSidebar);
  }

  if (backdrop) {
    backdrop.addEventListener('click', closeSidebar);
  }

  // Close mobile drawer when clicking any link
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (navMenu.classList.contains('is-open')) {
        closeSidebar();
      }
    });
  });

  // Close when pressing Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navMenu.classList.contains('is-open')) {
      closeSidebar();
    }
  });
}

/**
 * 3. Active Nav Link Indicator on Scroll
 */
function initActiveNavObserver() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

  if (!sections.length || !navLinks.length) return;

  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const currentId = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${currentId}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(section => observer.observe(section));
}

/**
 * 4. Subtle Scroll Reveal Animations
 */
function initScrollReveal() {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) return;

  const elementsToReveal = document.querySelectorAll(
    '.expertise-card, .timeline-item, .sector-card, .skill-category-card, .edu-card, .spec-box, .experience-hero-badge, .metric-highlight-banner'
  );

  elementsToReveal.forEach((el, index) => {
    el.classList.add('reveal-on-scroll');
    // Stagger transition delay slightly for grids
    const delay = (index % 3) * 0.1;
    el.style.transitionDelay = `${delay}s`;
  });

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  elementsToReveal.forEach(el => observer.observe(el));
}

/**
 * 5. Interactive Contact Form with Validation & Feedback
 */
function initContactForm() {
  const form = document.getElementById('projectContactForm');
  const toast = document.getElementById('formToast');
  if (!form || !toast) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = form.querySelector('#contactName').value.trim();
    const email = form.querySelector('#contactEmail').value.trim();
    const subject = form.querySelector('#contactSubject').value.trim();
    const message = form.querySelector('#contactMessage').value.trim();

    if (!name || !email || !message) {
      showToast(toast, 'Please fill in all required fields.', 'error');
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      showToast(toast, 'Please enter a valid corporate or professional email address.', 'error');
      return;
    }

    // Prepare direct mailto URL as client fallback
    const mailtoLink = `mailto:Muhdfayishere@gmail.com?subject=${encodeURIComponent(
      `[Portfolio Inquiry] ${subject || 'Engineering Project Inquiry'} from ${name}`
    )}&body=${encodeURIComponent(
      `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`
    )}`;

    showToast(
      toast,
      'Opening your email client to send your message to Muhammed Fayis...',
      'success'
    );

    setTimeout(() => {
      window.location.href = mailtoLink;
      form.reset();
    }, 1200);
  });
}

function showToast(element, message, type) {
  element.textContent = message;
  element.className = `form-toast ${type}`;
  element.style.display = 'block';

  setTimeout(() => {
    element.style.display = 'none';
  }, 6000);
}

/**
 * 6. Back-to-Top Action
 */
function initBackToTop() {
  const backToTopBtn = document.getElementById('backToTopBtn');
  if (!backToTopBtn) return;

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/**
 * 7. Subtle Portrait Parallax
 */
function initPortraitParallax() {
  const wrapper = document.querySelector('.portrait-wrapper');
  if (!wrapper) return;

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion || window.innerWidth < 768) return;

  wrapper.addEventListener('mousemove', (e) => {
    const rect = wrapper.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    
    const rotateX = -(y / rect.height) * 8;
    const rotateY = (x / rect.width) * 8;

    wrapper.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
  });

  wrapper.addEventListener('mouseleave', () => {
    wrapper.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
  });
}
