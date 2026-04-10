# Darkly - Writeup : récupération du flag via XSS “inattendu”

## Analyse

Ce cas est un peu étrange : en essayant des failles XSS et des injections de balises `<script>`, on se rend compte que tout ce qui est entre chevron est supprimé du commentaire. On a donc testé un simple `script` **sans balise**, et cela donne le flag directement.

## Bonnes pratiques

Pour éviter ce type de problème, il est recommandé d’utiliser des librairies ou des fonctions qui vérifient et échappent correctement les entrées utilisateur, comme `html_safe` ou d’autres outils de protection contre les injections XSS.  