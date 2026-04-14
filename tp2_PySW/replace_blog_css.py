from pathlib import Path

path = Path(r'c:\Users\LENOVO\OneDrive\Documentos\tp2_PySW\estilos\styles.css')
text = path.read_text(encoding='utf-8')
start = '/* ========================================\n   BLOG - ESTILO REVISTA NEWSPAPER\n   ======================================== */'
end = '/* ========================================\n   ACCESIBILIDAD Y MICRO-INTERACCIONES\n   ======================================== */'
idx1 = text.find(start)
idx2 = text.find(end, idx1)
if idx1 == -1 or idx2 == -1:
    raise ValueError(f'Marker not found: idx1={idx1}, idx2={idx2}')

replacement = '''/* ========================================
   BLOG - ESTILO REVISTA NEWSPAPER
   ======================================== */

:root {
    --blog-col-gap: 1.75rem;
    --blog-row-gap: 1.75rem;
    --blog-border-rule: 1px solid var(--border);
    --blog-featured-min-h: 340px;
    --article-radius: 20px;
    --article-img-h: 210px;

    /* Tag colors por categoria */
    --tag-aventura: #f97316;
    --tag-aventura-bg: rgba(249, 115, 22, 0.12);
    --tag-cultura: #8b5cf6;
    --tag-cultura-bg: rgba(139, 92, 246, 0.12);
    --tag-gastronomia: #ec4899;
    --tag-gastronomia-bg: rgba(236, 72, 153, 0.12);
    --tag-consejos: #3b82f6;
    --tag-consejos-bg: rgba(59, 130, 246, 0.12);
    --tag-relatos: #10b981;
    --tag-relatos-bg: rgba(16, 185, 129, 0.12);
}

/* ---- BLOG HEADER ---- */

.blog-header {
    position: relative;
    min-height: 62vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: clamp(5rem, 8vw, 7rem) var(--spacing-md) clamp(4rem, 6vw, 5rem);
    background: linear-gradient(160deg, var(--primary-dark) 0%, #0a4a45 50%, var(--bg) 100%);
    overflow: hidden;
    scroll-snap-align: start;
    isolation: isolate;
}

.blog-header-bg {
    position: absolute;
    inset: 0;
    background: url('https://images.unsplash.com/photo-1506929562872-bb421503ef21?w=1600&q=80') center/cover;
    opacity: 0.12;
    animation: slowZoom 28s ease-in-out infinite;
    will-change: transform;
}

@keyframes slowZoom {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.07); }
}

/* Lineas decorativas estilo periodico */
.blog-header-rule {
    position: absolute;
    left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--primary), var(--accent), transparent);
    opacity: 0.55;
}
.blog-header-rule.top { top: 0; }
.blog-header-rule.bottom { bottom: 60px; }

.blog-header-content {
    position: relative;
    z-index: 2;
    max-width: 780px;
}

.header-edition-label {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 1.25rem;
}

.edition-line {
    display: inline-block;
    width: 2.5rem;
    height: 1px;
    background: var(--primary);
    opacity: 0.6;
}

.blog-title-sub {
    display: block;
    font-size: clamp(0.7rem, 1.5vw, 0.85rem);
    font-weight: 600;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.5rem;
}

.blog-header h1 {
    font-size: clamp(2.8rem, 5.5vw, 4.5rem);
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    line-height: 1.05;
    margin-bottom: 1.1rem;
    color: var(--text);
    letter-spacing: -0.02em;
}

.blog-header h1 em {
    font-style: italic;
    color: var(--primary);
}

.blog-header p {
    font-size: clamp(1rem, 1.8vw, 1.15rem);
    margin-bottom: 1.75rem;
    color: var(--text-muted);
    max-width: 560px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.65;
}

.header-meta {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    flex-wrap: wrap;
    font-size: 0.82rem;
    color: var(--text-muted);
    background: var(--bg-surface-soft);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 0.6rem 1.4rem;
    backdrop-filter: blur(8px);
}

.header-meta [role="listitem"] {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
}

.header-meta-divider {
    opacity: 0.35;
}

.header-scroll {
    position: absolute;
    bottom: 1.75rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-soft);
    animation: headerBounce 2s ease-in-out infinite;
    transition: color 0.2s ease;
}

.header-scroll:hover,
.header-scroll:focus-visible {
    color: var(--primary);
}

@keyframes headerBounce {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50% { transform: translateX(-50%) translateY(6px); }
}

/* ---- BLOG FILTERS ---- */

.blog-filters {
    padding: 0.85rem var(--spacing-md);
    background: var(--bg-surface);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 62px;
    z-index: 22;
    backdrop-filter: blur(16px);
}

.filters-container {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 1.25rem;
    justify-content: center;
}

.filters-label {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--text-muted);
    white-space: nowrap;
    display: none;
}

@media (min-width: 640px) {
    .filters-label { display: inline-block; }
}

.tag-filters {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
}

.filter-label {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.45rem 1rem;
    background: var(--bg-card-soft);
    border: 1px solid var(--border);
    border-radius: 999px;
    cursor: pointer;
    transition: background-color 0.22s ease, border-color 0.22s ease, color 0.22s ease, transform 0.22s ease, box-shadow 0.22s ease;
    font-size: 0.82rem;
    font-weight: 500;
    color: var(--text-muted);
    user-select: none;
    white-space: nowrap;
}

.filter-label:hover {
    background: rgba(93, 208, 199, 0.1);
    border-color: var(--primary);
    color: var(--primary);
    transform: translateY(-2px);
}

.filter-label:focus-visible {
    outline: 2px solid var(--primary);
    outline-offset: 3px;
}

.filter-label.active {
    background: var(--primary);
    border-color: var(--primary);
    color: #041014;
    font-weight: 700;
    box-shadow: 0 4px 14px rgba(93, 208, 199, 0.28);
}

/* ---- FILTRADO CSS PURO (SOLO CSS) ---- */

[id="all"]:checked ~ .blog-grid-section .blog-article { display: block; }

[id="aventura"]:checked ~ .blog-grid-section .blog-article:not(.aventura),
[id="cultura"]:checked ~ .blog-grid-section .blog-article:not(.cultura),
[id="gastronomia"]:checked ~ .blog-grid-section .blog-article:not(.gastronomia),
[id="consejos"]:checked ~ .blog-grid-section .blog-article:not(.consejos),
[id="relatos"]:checked ~ .blog-grid-section .blog-article:not(.relatos) {
    display: none;
}

[id="all"]:checked ~ .blog-filters [for="all"],
[id="aventura"]:checked ~ .blog-filters [for="aventura"],
[id="cultura"]:checked ~ .blog-filters [for="cultura"],
[id="gastronomia"]:checked ~ .blog-filters [for="gastronomia"],
[id="consejos"]:checked ~ .blog-filters [for="consejos"],
[id="relatos"]:checked ~ .blog-filters [for="relatos"] {
    background: var(--primary);
    border-color: var(--primary);
    color: #041014;
    font-weight: 700;
    box-shadow: 0 4px 14px rgba(93, 208, 199, 0.28);
}

/* ---- BLOG GRID SECTION ---- */

.blog-grid-section {
    padding: clamp(3rem, 5vw, 4.5rem) var(--spacing-md);
    scroll-snap-align: start;
}

.blog-container {
    max-width: 1400px;
    margin: 0 auto;
}

.blog-section-header {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 1.5rem;
    margin-bottom: 2.5rem;
    padding-bottom: 1.5rem;
    border-bottom: var(--blog-border-rule);
}

.blog-section-title {
    font-size: clamp(1.5rem, 3vw, 2.2rem);
    font-family: 'Playfair Display', serif;
    letter-spacing: -0.02em;
    color: var(--text);
    line-height: 1.1;
}

.blog-section-subtitle {
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-top: 0.35rem;
}

.blog-issue-badge {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    flex-shrink: 0;
    border-left: 2px solid var(--primary);
    padding-left: 0.85rem;
}

.issue-num {
    font-size: 1.4rem;
    font-weight: 800;
    font-family: 'Playfair Display', serif;
    color: var(--primary);
    line-height: 1;
}

.issue-text {
    font-size: 0.68rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-muted);
}

/* ---- NEWSPAPER GRID ---- */

.blog-newspaper-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: var(--blog-row-gap) var(--blog-col-gap);
}

/* ---- ARTICULO FEATURED ---- */

.blog-article.featured {
    grid-column: span 2;
    grid-row: span 2;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    background: var(--bg-card);
    border-radius: var(--article-radius);
    overflow: hidden;
    border: 1px solid var(--border);
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.18);
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.4s ease;
}

.blog-article.featured .article-image {
    height: 100%;
    min-height: var(--blog-featured-min-h);
    clip-path: none;
}

.blog-article.featured:hover {
    transform: translateY(-6px);
    box-shadow: 0 36px 80px rgba(0, 0, 0, 0.26);
}

.blog-article.featured .article-content {
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 0.5rem;
    border-left: var(--blog-border-rule);
}

.blog-article.featured h2 {
    font-size: clamp(1.3rem, 2vw, 1.7rem);
    font-family: 'Playfair Display', serif;
    line-height: 1.25;
    letter-spacing: -0.02em;
}

/* ---- ARTICULOS NORMALES ---- */

.blog-article {
    background: var(--bg-card);
    border-radius: var(--article-radius);
    overflow: hidden;
    border: 1px solid var(--border);
    opacity: 0;
    transform: translateY(28px);
    transition:
        opacity 0.55s ease,
        transform 0.55s cubic-bezier(0.34, 1.56, 0.64, 1),
        box-shadow 0.3s ease,
        border-color 0.3s ease;
    will-change: transform, opacity;
    perspective: 800px;
}

.blog-article.revealed {
    opacity: 1;
    transform: translateY(0) rotateX(0) rotateY(0);
}

.blog-article:not(.featured):hover {
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.22);
    border-color: rgba(93, 208, 199, 0.25);
}

/* ---- IMAGEN DEL ARTICULO ---- */

.article-image {
    position: relative;
    overflow: hidden;
    height: var(--article-img-h);
}

.article-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    display: block;
}

.blog-article:hover .article-image img {
    transform: scale(1.07);
}

/* Overlay gradiente sobre imagen */
.article-image-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, transparent 40%, rgba(7, 11, 16, 0.65) 100%);
    opacity: 0;
    transition: opacity 0.35s ease;
}

.blog-article:hover .article-image-overlay {
    opacity: 1;
}

/* Numero decorativo del articulo (estilo revista) */
.article-image-number {
    position: absolute;
    top: 0.75rem;
    right: 0.85rem;
    font-size: 0.62rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    color: rgba(255, 255, 255, 0.55);
    font-family: 'Playfair Display', serif;
    z-index: 3;
}

/* ---- TAGS DE CATEGORIA ---- */

.article-tag-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.28rem 0.75rem;
    border-radius: 999px;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
    transition: transform 0.2s ease;
}

.blog-article:hover .article-tag-pill {
    transform: translateX(3px);
}

.aventura-tag  { background: var(--tag-aventura-bg);  color: var(--tag-aventura); }
.cultura-tag   { background: var(--tag-cultura-bg);   color: var(--tag-cultura); }
.gastronomia-tag { background: var(--tag-gastronomia-bg); color: var(--tag-gastronomia); }
.consejos-tag  { background: var(--tag-consejos-bg);  color: var(--tag-consejos); }
.relatos-tag   { background: var(--tag-relatos-bg);   color: var(--tag-relatos); }

/* ---- CONTENIDO DEL ARTICULO ---- */

.article-content {
    padding: 1.25rem 1.35rem;
}

.article-content h2,
.article-content h3 {
    line-height: 1.3;
    letter-spacing: -0.02em;
    color: var(--text);
    transition: color 0.2s ease;
}

.article-content h2 { margin-bottom: 0.75rem; }

.article-content h3 {
    font-size: clamp(1rem, 1.5vw, 1.15rem);
    margin-bottom: 0.65rem;
}

.blog-article:hover .article-content h3 {
    color: var(--primary);
}

.article-meta {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.72rem;
    color: var(--text-muted);
    margin-bottom: 0.75rem;
}

.meta-sep {
    opacity: 0.4;
}

.article-date {
    font-variant-numeric: tabular-nums;
}

.article-content p {
    color: var(--text-muted);
    font-size: 0.88rem;
    margin-bottom: 1rem;
    line-height: 1.6;
}

/* ---- LEER MAS ---- */

.read-more {
    color: var(--primary);
    font-weight: 600;
    font-size: 0.83rem;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    transition: gap 0.2s ease, color 0.2s ease;
}

.read-more:hover,
.read-more:focus-visible {
    gap: 0.7rem;
}

.read-more:focus-visible {
    outline: 2px solid var(--primary);
    outline-offset: 4px;
    border-radius: 4px;
}

.article-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1.1rem;
    gap: 0.75rem;
    flex-wrap: wrap;
}

.article-stats {
    display: flex;
    gap: 0.65rem;
}

.stat-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.75rem;
    color: var(--text-muted);
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    transition: color 0.2s ease, transform 0.2s ease;
    font-family: inherit;
}

.stat-btn:hover,
.like-btn:hover {
    color: var(--primary);
    transform: scale(1.08);
}

.like-btn[aria-pressed="true"] {
    color: #f87171;
}

/* ========================================
   COMENTARIOS CON AVATARES CSS
   ======================================== */

.blog-comments-section {
    padding: clamp(3rem, 5vw, 4.5rem) var(--spacing-md);
    background: var(--bg-surface-soft);
    scroll-snap-align: start;
    border-top: var(--blog-border-rule);
    border-bottom: var(--blog-border-rule);
}

.comments-container {
    max-width: 860px;
    margin: 0 auto;
}

.comments-header {
    text-align: center;
    margin-bottom: 2.5rem;
}

.comments-header h2 {
    font-size: clamp(1.5rem, 3vw, 2rem);
    font-family: 'Playfair Display', serif;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}

.comments-header p {
    color: var(--text-muted);
    font-size: 0.9rem;
}

.comments-grid {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    margin-bottom: 2.5rem;
}

/* ---- TARJETA DE COMENTARIO ---- */

.comment-card {
    display: flex;
    gap: 1.1rem;
    padding: 1.35rem;
    background: var(--bg-card);
    border-radius: 18px;
    border: 1px solid var(--border);
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    opacity: 0;
    transform: translateY(20px);
}

.comment-card.revealed {
    opacity: 1;
    transform: translateY(0);
}

.comment-card:hover {
    transform: translateX(4px);
    border-color: rgba(93, 208, 199, 0.3);
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.12);
}

/* ---- AVATARES CSS CON PSEUDOELEMENTOS ---- */

.comment-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    flex-shrink: 0;
    position: relative;
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.comment-card:hover .comment-avatar {
    transform: scale(1.1) rotate(-3deg);
}

.comment-avatar::before {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 0.92rem;
    letter-spacing: 0.02em;
    color: rgba(255, 255, 255, 0.95);
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
}

.comment-avatar::after {
    content: "";
    position: absolute;
    bottom: 1px;
    right: 1px;
    width: 11px;
    height: 11px;
    border-radius: 50%;
    border: 2px solid var(--bg-card);
}

.avatar-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.avatar-1::before { content: "MG"; }
.avatar-1::after { background: #10b981; }

.avatar-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
.avatar-2::before { content: "CR"; }
.avatar-2::after { background: #94a3b8; }

.avatar-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
.avatar-3::before { content: "LM"; }
.avatar-3::after { background: #10b981; }

.avatar-4 { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }
.avatar-4::before { content: "JF"; color: rgba(30, 20, 10, 0.85); }
.avatar-4::after { background: #94a3b8; }

.avatar-5 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
.avatar-5::before { content: "VS"; color: rgba(10, 30, 25, 0.85); }
.avatar-5::after { background: #10b981; }

/* ---- CONTENIDO DEL COMENTARIO ---- */

.comment-content {
    flex: 1;
    min-width: 0;
}

.comment-header {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 0.55rem;
}

.comment-author {
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--text);
}

.comment-date {
    font-size: 0.68rem;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
}

.comment-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.63rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    background: var(--surface-soft);
    border: 1px solid var(--border);
    padding: 0.22rem 0.6rem;
    border-radius: 999px;
    color: var(--primary);
    transition: background 0.2s ease;
}

.comment-card:hover .comment-badge {
    background: rgba(93, 208, 199, 0.08);
}

.comment-content p {
    color: var(--text-soft);
    font-size: 0.875rem;
    line-height: 1.65;
    margin-bottom: 0.8rem;
}

.comment-actions {
    display: flex;
    gap: 0.85rem;
    align-items: center;
}

.comment-like,
.comment-reply {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: none;
    border: 1px solid var(--border);
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    cursor: pointer;
    padding: 0.3rem 0.75rem;
    border-radius: 999px;
    transition: background 0.2s ease, color 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
    font-family: inherit;
}

.comment-like:hover,
.comment-reply:hover {
    color: var(--primary);
    border-color: var(--primary);
    background: rgba(93, 208, 199, 0.07);
    transform: translateY(-1px);
}

.comment-like:focus-visible,
.comment-reply:focus-visible {
    outline: 2px solid var(--primary);
    outline-offset: 3px;
}

.comment-like[aria-pressed="true"] {
    color: #f87171;
    border-color: rgba(248, 113, 113, 0.4);
    background: rgba(248, 113, 113, 0.06);
}

/* ---- FORMULARIO DE COMENTARIOS ---- */

.comment-form-wrapper {
    background: var(--bg-card);
    border-radius: 22px;
    border: 1px solid var(--border);
    padding: 2rem;
    margin-top: 0.5rem;
}

.comment-form-header {
    margin-bottom: 1.5rem;
}

.comment-form-header h3 {
    font-size: 1.2rem;
    font-family: 'Playfair Display', serif;
    margin-bottom: 0.25rem;
}

.comment-form-header p {
    font-size: 0.82rem;
    color: var(--text-muted);
}

.comment-form {
    display: flex;
    flex-direction: column;
    gap: 1.1rem;
}

.form-row-comment {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.form-field {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
}

.form-label {
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--text-muted);
    letter-spacing: 0.04em;
}

.comment-form input,
.comment-form textarea {
    padding: 0.8rem 1rem;
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: var(--text);
    font-size: 0.9rem;
    transition: border-color 0.25s ease, box-shadow 0.25s ease, background 0.25s ease;
    width: 100%;
    resize: vertical;
}

.comment-form input:focus,
.comment-form textarea:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(93, 208, 199, 0.15);
    background: var(--bg-card);
}

.comment-form input::placeholder,
.comment-form textarea::placeholder {
    color: var(--text-muted);
    opacity: 0.6;
}

.form-hint {
    font-size: 0.72rem;
    color: var(--text-muted);
    opacity: 0.7;
}

.btn-submit-comment {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.55rem;
    padding: 0.85rem 2rem;
    background: linear-gradient(135deg, var(--primary), var(--primary-dark));
    color: #041014;
    font-weight: 700;
    font-size: 0.9rem;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    transition: transform 0.25s ease, box-shadow 0.25s ease, filter 0.25s ease;
    align-self: flex-start;
    min-width: 200px;
}

.btn-submit-comment:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(93, 208, 199, 0.28);
    filter: brightness(1.06);
}

.btn-submit-comment:focus-visible {
    outline: 3px solid var(--primary);
    outline-offset: 4px;
}

.btn-submit-comment:disabled {
    opacity: 0.7;
    cursor: wait;
    transform: none;
}

/* ========================================
   NEWSLETTER CON PARALLAX
   ======================================== */

.blog-newsletter {
    position: relative;
    padding: clamp(3.5rem, 6vw, 5rem) var(--spacing-md);
    background: linear-gradient(135deg, var(--primary-dark) 0%, #0a4a45 60%, var(--primary) 100%);
    text-align: center;
    overflow: hidden;
    scroll-snap-align: start;
    isolation: isolate;
}

.newsletter-overlay {
    position: absolute;
    inset: 0;
    background: url('https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1600&q=80') center/cover;
    opacity: 0.08;
    will-change: transform;
}

/* Patron decorativo */
.newsletter-pattern {
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(circle at 20% 50%, rgba(255,255,255,0.06) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(247, 178, 103, 0.1) 0%, transparent 50%);
    pointer-events: none;
}

.newsletter-content {
    position: relative;
    z-index: 2;
    max-width: 560px;
    margin: 0 auto;
}

.newsletter-icon-wrapper {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 64px;
    height: 64px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 18px;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(8px);
    animation: iconPulse 3s ease-in-out infinite;
}

@keyframes iconPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.04); }
}

.newsletter-content h2 {
    font-size: clamp(1.5rem, 3.5vw, 2.2rem);
    font-family: 'Playfair Display', serif;
    margin-bottom: 0.65rem;
    color: white;
    letter-spacing: -0.02em;
}

.newsletter-content p {
    margin-bottom: 2rem;
    color: rgba(255, 255, 255, 0.8);
    font-size: 1rem;
    line-height: 1.6;
}

.newsletter-form {
    display: flex;
    gap: 0.5rem;
    max-width: 440px;
    margin: 0 auto 1.25rem;
}

.newsletter-form input {
    flex: 1;
    padding: 0.9rem 1.3rem;
    border: 1.5px solid rgba(255, 255, 255, 0.25);
    border-radius: 12px;
    font-size: 0.92rem;
    background: rgba(255, 255, 255, 0.12);
    color: white;
    backdrop-filter: blur(8px);
    transition: border-color 0.25s ease, background 0.25s ease;
}

.newsletter-form input::placeholder {
    color: rgba(255, 255, 255, 0.55);
}

.newsletter-form input:focus {
    outline: none;
    border-color: rgba(255, 255, 255, 0.6);
    background: rgba(255, 255, 255, 0.18);
}

.newsletter-form button {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.9rem 1.5rem;
    background: white;
    color: #041014;
    border: none;
    border-radius: 12px;
    font-weight: 800;
    font-size: 0.9rem;
    cursor: pointer;
    white-space: nowrap;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.newsletter-form button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.2);
}

.newsletter-form button:focus-visible {
    outline: 3px solid rgba(255, 255, 255, 0.8);
    outline-offset: 3px;
}

.newsletter-privacy {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.75rem;
    color: rgba(255, 255, 255, 0.55);
}

/* ========================================
   SCROLL SNAP
   ======================================== */

.snap-section {
    scroll-snap-align: start;
}

/* ========================================
   RESPONSIVE DEL BLOG
   ======================================== */

@media (max-width: 1200px) {
    .blog-newspaper-grid {
        grid-template-columns: repeat(3, 1fr);
    }
    .blog-article.featured {
        grid-column: span 3;
        grid-row: span 1;
        grid-template-columns: 1.1fr 0.9fr;
    }
    .blog-article.featured .article-image {
        min-height: 300px;
    }
}

@media (max-width: 900px) {
    .blog-newspaper-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    .blog-article.featured {
        grid-column: span 2;
        grid-template-columns: 1fr 1fr;
    }
    .blog-section-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.75rem;
    }
    .blog-issue-badge {
        align-items: flex-start;
    }
}

@media (max-width: 640px) {
    :root {
        --blog-col-gap: 1.25rem;
        --blog-row-gap: 1.25rem;
    }
    .blog-newspaper-grid {
        grid-template-columns: 1fr;
    }
    .blog-article.featured {
        grid-column: span 1;
        grid-template-columns: 1fr;
    }
    .blog-article.featured .article-image {
        height: 220px;
        min-height: unset;
    }
    .blog-article.featured .article-content {
        border-left: none;
        border-top: var(--blog-border-rule);
    }
    .form-row-comment {
        grid-template-columns: 1fr;
    }
    .newsletter-form {
        flex-direction: column;
    }
    .newsletter-form input,
    .newsletter-form button {
        width: 100%;
    }
    .comment-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.3rem;
    }
    .btn-submit-comment {
        width: 100%;
        align-self: stretch;
    }
}

@media (max-width: 480px) {
    .comment-card {
        gap: 0.85rem;
    }
    .header-meta {
        padding: 0.5rem 1rem;
        font-size: 0.75rem;
    }
    .comment-form-wrapper {
        padding: 1.35rem;
    }
}

/* ---- MODO OSCURO (refuerzo de variables ya existentes) ---- */
@media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
        --tag-aventura-bg: rgba(249, 115, 22, 0.15);
        --tag-cultura-bg: rgba(139, 92, 246, 0.15);
        --tag-gastronomia-bg: rgba(236, 72, 153, 0.15);
        --tag-consejos-bg: rgba(59, 130, 246, 0.15);
        --tag-relatos-bg: rgba(16, 185, 129, 0.15);
    }
}

@media (max-width: 900px) {
  .menu-toggle {
    display: flex;
  }

  .nav-menu {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    flex-direction: column;
    gap: 0.8rem;
    padding: 1.5rem;
    background: var(--bg-card);
    border-top: 1px solid var(--border);
    z-index: 25;
  }

  .nav-menu.active {
    display: flex;
  }

  .nav-container {
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
  }

  .nav-menu a {
    width: 100%;
    padding: 0.75rem 0;
  }

  .mega-menu {
    position: static;
    width: 100%;
    margin-top: 0.5rem;
    border: none;
    box-shadow: none;
    background: transparent;
    padding: 0;
  }

  .has-mega-menu .mega-panel {
    background: var(--bg-card);
    padding: 1rem;
    border-radius: 20px;
  }

  .hero-search {
    grid-template-columns: 1fr;
  }

  .hero-search svg {
    justify-self: center;
  }

  .hero-search button {
    width: 100%;
  }
}
'''

new_text = text[:idx1] + replacement + '\n\n' + text[idx2:]
path.write_text(new_text, encoding='utf-8')
print('Updated blog CSS block in styles.css')
'''
