# Darkly - Writeup : Local File Inclusion (LFI)

## Analyse

Le paramètre `page` dans l’URL est utilisé pour inclure des fichiers côté serveur :

```
/index.php?page=...
```

Aucune validation n’est appliquée sur cette valeur.

En modifiant le paramètre, il est possible d’accéder à des fichiers système :

```
http://10.19.202.124/index.php?page=../../../../../../../etc/passwd
```

Le contenu de `/etc/passwd` est affiché, confirmant une vulnérabilité de type Local File Inclusion.

## Bonnes pratiques

Ne jamais inclure directement une entrée utilisateur sans validation. Il faudrait par exemple dans ce cas verifier que le chemin est encore dans le bon dossier.
Ne jamais utiliser une donnée contrôlée par l’utilisateur dans une fonction d’inclusion.