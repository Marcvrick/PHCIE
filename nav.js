/* Navigation mobile — source unique, injectée par build.js sur toutes les pages.
 *
 * 69 pages portent encore un ancien handler de hamburger enfoui dans un script
 * de page (jusqu'à 1642 lignes chez quiz-automedication) : impossible à retirer
 * sans découper chaque script à la main. Il faut donc les neutraliser à
 * l'exécution, et sans dépendre de l'ordre de chargement — les pages marques
 * bindent le leur dans un `requestIdleCallback(initPage, {timeout: 2000})`,
 * donc bien après ce fichier, quel que soit `defer`.
 *
 * D'où l'écoute en phase de CAPTURE sur document : elle passe avant tout
 * listener posé sur le bouton, peu importe quand il a été posé.
 * stopImmediatePropagation() coupe l'évènement là, les anciens handlers ne le
 * voient jamais, et le double-toggle (deux bascules sur un clic = menu qui ne
 * s'ouvre pas) ne peut plus se produire.
 *
 * Le bug du 12 août 2026 — 13 pages basculant `nav-open` ou `open` alors que
 * style.css n'implémente que `.nav-links.active` — est fermé par construction :
 * une seule classe, définie ici.
 */
(function () {
    function nav() { return document.querySelector('.nav-links'); }

    document.addEventListener('click', function (e) {
        var el = e.target;
        if (!el || !el.closest) return;
        var btn = el.closest('.mobile-menu-toggle');
        if (!btn) return;

        e.stopImmediatePropagation();
        e.preventDefault();

        var links = nav();
        if (!links) return;
        var isOpen = links.classList.toggle('active');
        btn.setAttribute('aria-expanded', isOpen);
    }, true);

    // Fermeture au clic hors du menu.
    document.addEventListener('click', function (e) {
        var links = nav();
        if (!links || !links.classList.contains('active')) return;
        if (links.contains(e.target)) return;
        links.classList.remove('active');
        var btn = document.querySelector('.mobile-menu-toggle');
        if (btn) btn.setAttribute('aria-expanded', 'false');
    });
})();
