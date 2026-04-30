# Darkly - Exploitation robots.txt - .hidden

## Analyse

Dans le fichier robots.txt situé à l'URL `http://x.x.x.x/robots.txt`, on trouve des instructions destinées aux outils de scraping.
On y remarque une ligne `Disallow: /.hidden`.
À cette URL, on trouve un index contenant plusieurs autres URLs. Au bout de chacun des chemins se trouve un fichier README.

## Exploitation

Écriture d'un script Python qui va explorer tous les chemins, ouvrir les fichiers README et copier leur contenu dans un fichier `results.txt`.
Il suffit ensuite d'effectuer une recherche du mot `flag` dans ce fichier.

## Bonnes pratiques

### Pour les développeurs et administrateurs système

- **Ne jamais lister de répertoires sensibles** dans `robots.txt` : ce fichier est public et constitue une invitation à explorer les chemins qu'il mentionne, même ceux marqués `Disallow`.
- **Désactiver l'indexation automatique** des répertoires sur le serveur web (directive `Options -Indexes` sur Apache, `autoindex off` sur Nginx) afin d'éviter qu'un simple accès à un dossier n'affiche son contenu.
- **Ne jamais stocker d'informations sensibles** (flags, mots de passe, clés API) dans des fichiers accessibles publiquement, même dans des répertoires supposément cachés.
- **Mettre en place des contrôles d'accès** (authentification, liste blanche d'IPs) sur tout répertoire qui ne doit pas être accessible au public.
- **Auditer régulièrement** les fichiers et répertoires exposés par le serveur web à l'aide d'outils comme `nikto` ou `dirb`.
