# Darkly - Writeup : Accès à une page via paramètre hashé

## Analyse

Sur la page d’accueil, un lien "copyright" est présent :

```
?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

Bizarre me diriez vous ? En regardant un peu les failles connues sur `OWASP Top 10 2025`, on tombe assez vite sur `https://cwe.mitre.org/data/definitions/601.html`

L'idee ici est de faire rediriger la page actuelle sur un autre site, potentiellement une copie malveillantes afin de voler des credentials ou tout autre chose.

`http://10.13.200.231/index.php?page=redirect&site=www.google.fr

## Bonnes pratiques

* Ne jamais faire confiance à une URL fournie directement par l'utilisateur.
* Mettre en place une **liste blanche** des destinations autorisées et n'autoriser que celles-ci.
* Vérifier systématiquement les paramètres utilisés pour effectuer une redirection.
* Lorsque cela est possible, afficher un écran de confirmation avant de rediriger l'utilisateur vers un domaine externe.
