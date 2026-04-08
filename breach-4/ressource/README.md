# Darkly - Writeup : récupération du flag via XSS “inattendu”

## Exploitation

Ce cas est un peu étrange : en essayant des failles XSS et des injections de balises `<script>`, on a testé un simple `script` **sans balise**, et cela donne le flag directement. C’est le genre de comportement qui **ne devrait pas se produire**.

## Bonnes pratiques

Pour éviter ce type de problème, il est recommandé d’utiliser des librairies ou des fonctions qui vérifient et échappent correctement les entrées utilisateur, comme `html_safe` ou d’autres outils de protection contre les injections XSS.  