async function incluirHTML() {
  const elementos = document.querySelectorAll('[data-include-html]');
  for (const el of elementos) {
    const archivo = el.getAttribute('data-include-html');
    if (!archivo) continue;

    try {
      const res = await fetch(archivo);
      if (!res.ok) throw new Error(`No se pudo cargar: ${archivo}`);
      el.innerHTML = await res.text();
      el.removeAttribute('data-include-html');
    } catch (e) {
      console.warn(e);
    }
  }
}

function initDarkMode() {
  const toggle = document.getElementById('dark-toggle');
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = savedTheme || (prefersDark ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', theme);
  document.body.setAttribute('data-theme', theme);

  if (toggle) updateToggleIcon(toggle, theme);

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('#dark-toggle');
    if (!btn) return;

    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    document.body.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateToggleIcon(btn, next);
  });
}

function updateToggleIcon(btn, theme) {
  btn.setAttribute('aria-label', theme === 'dark' ? 'Activar modo claro' : 'Activar modo oscuro');
}

function initMenu() {
  const menuToggle = document.querySelector('.menu-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const megaMenuItem = document.querySelector('.has-mega-menu');
  const megaMenuLink = document.querySelector('.has-mega-menu > a');

  if (!menuToggle || !navMenu) return;

  menuToggle.addEventListener('click', () => {
    const active = navMenu.classList.toggle('active');
    menuToggle.setAttribute('aria-expanded', active);
    menuToggle.setAttribute('aria-label', active ? 'Cerrar menú' : 'Abrir menú');
  });

  document.addEventListener('click', (e) => {
    if (!menuToggle.contains(e.target) && !navMenu.contains(e.target)) {
      navMenu.classList.remove('active');
      menuToggle.setAttribute('aria-expanded', 'false');
      menuToggle.setAttribute('aria-label', 'Abrir menú');
    }
  });

  if (megaMenuItem && megaMenuLink) {
    megaMenuItem.addEventListener('mouseenter', () => megaMenuLink.setAttribute('aria-expanded', 'true'));
    megaMenuItem.addEventListener('mouseleave', () => megaMenuLink.setAttribute('aria-expanded', 'false'));
    megaMenuLink.addEventListener('focus', () => megaMenuLink.setAttribute('aria-expanded', 'true'));
    megaMenuLink.addEventListener('blur', () => megaMenuLink.setAttribute('aria-expanded', 'false'));
  }
}

function initAgenciasPage() {
  const container = document.getElementById('agencias-lista');
  if (!container) return;

  const searchInput = document.getElementById('buscar-agencia');
  const filterButtons = document.querySelectorAll('[data-filter]');
  const resultCount = document.getElementById('count-results');
  const cards = Array.from(container.querySelectorAll('.flip-card'));
  let selectedFilter = 'todo';
  let searchQuery = '';

  const updateCards = () => {
    let visibleCount = 0;

    cards.forEach(card => {
      const category = card.dataset.categoria || '';
      const title = card.querySelector('h3')?.textContent.toLowerCase() || '';
      const type = card.querySelector('.agencia-tipo')?.textContent.toLowerCase() || '';
      const searchMatch = title.includes(searchQuery) || type.includes(searchQuery);
      const filterMatch = selectedFilter === 'todo' || category === selectedFilter;
      const shouldShow = searchMatch && filterMatch;

      card.style.display = shouldShow ? 'block' : 'none';
      if (shouldShow) visibleCount++;
    });

    if (resultCount) resultCount.textContent = String(visibleCount);
  };

  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      selectedFilter = button.dataset.filter || 'todo';
      filterButtons.forEach(btn => {
        const active = btn === button;
        btn.classList.toggle('active', active);
        btn.setAttribute('aria-pressed', String(active));
      });
      updateCards();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', () => {
      searchQuery = searchInput.value.toLowerCase();
      updateCards();
    });
  }

  cards.forEach(card => {
    card.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        card.classList.toggle('flipped');
      }
    });
    card.addEventListener('click', () => card.classList.toggle('flipped'));
  });

  updateCards();
}

document.addEventListener('DOMContentLoaded', async () => {
  await incluirHTML();
  initDarkMode();
  initMenu();
  initAgenciasPage();
});