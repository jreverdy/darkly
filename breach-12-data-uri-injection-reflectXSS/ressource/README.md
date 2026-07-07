# Darkly - Exploitation Data URI Injection - src parameter

## Analyse

En naviguant sur le site, on découvre l'URL suivante : `http://10.14.200.156/?page=media&src=nsa`.
Le paramètre `src` est utilisé par le serveur pour inclure une ressource (ici une image). Ce paramètre n'est pas correctement filtré, ce qui le rend vulnérable à une injection de Data URI.

## Exploitation

Une Data URI permet d'intégrer du contenu directement dans une URL sous la forme :
`data:[type];base64,[contenu encodé en base64]`

On encode le payload en base64 :

```bash
echo -n "<script>alert(1)</script>" | base64
# → PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

On injecte ensuite la Data URI dans le paramètre `src` :
http://x.x.x.x/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
Le serveur interprète le contenu encodé et exécute le script, ce qui permet d'obtenir le flag.

## Bonnes pratiques

### Pour les développeurs et administrateurs système

- **Ne jamais faire confiance aux paramètres utilisateur** : tout paramètre passé dans l'URL doit être considéré comme potentiellement malveillant et doit être strictement validé côté serveur avant d'être utilisé.
- **Mettre en place une liste blanche de valeurs autorisées** : si `src` ne doit accepter que quelques ressources connues (ex. `nsa`, `logo`), le serveur doit rejeter toute valeur ne figurant pas dans cette liste, plutôt que de tenter de filtrer les valeurs dangereuses.
- **Interdire les schémas URI dangereux** : les schémas `data:`, `javascript:` et `vbscript:` ne doivent jamais être acceptés comme valeur d'un paramètre destiné à charger une ressource externe.
- **Mettre en place une Content Security Policy (CSP)** : une CSP correctement configurée permet de bloquer l'exécution de scripts injectés, même si la validation côté serveur est défaillante. Par exemple, la directive `default-src 'self'` interdit le chargement de ressources externes non autorisées.
- **Échapper les sorties** : toute valeur issue de l'URL qui est réinjectée dans le HTML doit être correctement échappée pour éviter son interprétation par le navigateur.

### À retenir sur les Data URI

Une Data URI n'est pas une simple image ou un lien anodin : elle peut contenir du HTML, du JavaScript ou tout autre contenu interprétable par le navigateur. Accepter des Data URIs depuis une entrée utilisateur est équivalent à lui permettre d'injecter du code arbitraire dans la page.
