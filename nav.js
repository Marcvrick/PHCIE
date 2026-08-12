/* Navigation mobile — source unique, injectée par build.js sur toutes les pages.
 *
 * Chargée en `defer` : elle s'exécute APRÈS les scripts inline de fin de page.
 * 69 pages portent encore un ancien handler de hamburger enfoui dans un script
 * de page (jusqu'à 1642 lignes chez quiz-automedication) — impossible à retirer
 * sans découper chaque script à la main. Le clone du bouton coupe court : cloner
 * un noeud ne recopie pas ses écouteurs, donc tout handler hérité disparaît et
 * seul celui d'ici reste. Le bug de 2026-08-12 (13 pages basculant `nav-open` ou
 * `open` alors que style.css n'implémente que `.nav-links.active`) ne peut plus
 * se reproduire : une seule classe, définie ici.
 */
(function () {
    var toggle = document.querySelector('.mobile-menu-toggle');
    var navLinks = document.querySelector('.nav-links');
    if (!toggle || !navLinks) return;

    var clean = toggle.cloneNode(true);
    toggle.parentNode.replaceChild(clean, toggle);

    clean.addEventListener('click', function (e) {
        // Les anciens scripts posent aussi un listener « clic hors du menu » sur
        // document, dont la closure pointe encore sur le bouton d'origine — pour
        // eux, un clic sur le clone est un clic dehors, et ils referment aussitôt.
        // Couper la propagation les met hors circuit sans toucher à leur code.
        e.stopPropagation();
        var isOpen = navLinks.classList.toggle('active');
        clean.setAttribute('aria-expanded', isOpen);
    });

    // Fermeture au clic hors du menu.
    document.addEventListener('click', function (e) {
        if (navLinks.contains(e.target) || clean.contains(e.target)) return;
        navLinks.classList.remove('active');
        clean.setAttribute('aria-expanded', 'false');
    });
})();
