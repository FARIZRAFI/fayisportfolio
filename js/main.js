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
  initProjectGalleryLightbox();
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

/**
 * 8. Project Field Gallery Lightbox Modal
 */
function initProjectGalleryLightbox() {
  const modal = document.getElementById('projectLightboxModal');
  const overlay = document.getElementById('lightboxOverlay');
  const closeBtn = document.getElementById('lightboxCloseBtn');
  const imgEl = document.getElementById('lightboxImg');
  const titleEl = document.getElementById('lightboxTitle');
  const subEl = document.getElementById('lightboxSub');
  const tagEl = document.getElementById('lightboxTag');
  const counterEl = document.getElementById('lightboxCounter');
  const prevBtn = document.getElementById('lightboxPrevBtn');
  const nextBtn = document.getElementById('lightboxNextBtn');

  if (!modal || !imgEl) return;

  // Collect distinct project items
  const cards = Array.from(document.querySelectorAll('.project-marquee-track .project-slide-card[data-index]'));
  const items = [];
  const seenIndices = new Set();
  cards.forEach(card => {
    const idx = parseInt(card.dataset.index, 10);
    if (!seenIndices.has(idx)) {
      seenIndices.add(idx);
      items.push({
        index: idx,
        src: card.dataset.src,
        title: card.dataset.title,
        sub: card.dataset.sub,
        tag: card.dataset.tag
      });
    }
  });

  items.sort((a, b) => a.index - b.index);
  if (items.length === 0) return;

  let currentIndex = 0;

  function updateModal(index) {
    if (index < 0) index = items.length - 1;
    if (index >= items.length) index = 0;
    currentIndex = index;

    const item = items[currentIndex];
    imgEl.src = item.src;
    imgEl.alt = item.title;
    titleEl.textContent = item.title;
    subEl.textContent = item.sub;
    tagEl.textContent = item.tag;
    counterEl.textContent = `${currentIndex + 1} / ${items.length}`;
  }

  function openModal(index) {
    updateModal(index);
    modal.classList.add('is-active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    if (closeBtn) closeBtn.focus();
  }

  function closeModal() {
    modal.classList.remove('is-active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  // Attach click listeners to all cards in the marquee (both original and duplicate sets)
  cards.forEach(card => {
    const idx = parseInt(card.dataset.index, 10);
    card.addEventListener('click', () => openModal(idx));
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openModal(idx);
      }
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (overlay) overlay.addEventListener('click', closeModal);

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      updateModal(currentIndex - 1);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      updateModal(currentIndex + 1);
    });
  }

  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('is-active')) return;
    if (e.key === 'Escape') closeModal();
    if (e.key === 'ArrowLeft') updateModal(currentIndex - 1);
    if (e.key === 'ArrowRight') updateModal(currentIndex + 1);
  });
}

