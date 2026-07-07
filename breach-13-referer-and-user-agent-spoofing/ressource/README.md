# Darkly - Exploitation Referer / User-Agent

## Analyse

À l'URL `http://10.14.200.156/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`, on peut retrouver du texte caché dans le HTML.
On y lit : `You must come from : "https://www.nsa.gov/"` et `Let's use this browser : "ft_bornToSec". It will help you a lot.`

## Exploitation

Dans le header de la requête GET, on modifie le `Referer` en `https://www.nsa.gov/` et l'`User-Agent` en `ft_bornToSec` :

```bash
curl -A "ft_bornToSec" -H "Referer: https://www.nsa.gov/" "http://10.14.200.156/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
```

Une fois la requête renvoyée, le flag s'affiche.

## Bonnes pratiques

### Pour les développeurs et administrateurs système

- **Ne jamais utiliser les headers HTTP comme mécanisme d'authentification** : les headers `Referer` et `User-Agent` sont entièrement contrôlés par le client et peuvent être falsifiés en quelques secondes. Ils ne constituent en aucun cas une preuve d'identité fiable.
- **Ne pas conditionner l'accès à une ressource sur la valeur d'un header** : toute logique de contrôle d'accès doit reposer sur des mécanismes robustes côté serveur (sessions, tokens, authentification).
- **Ne pas exposer d'indices dans le code source HTML** : indiquer dans le HTML les conditions exactes à remplir pour obtenir un accès revient à fournir le mode d'emploi de l'exploitation.

### À retenir sur les headers HTTP

Les headers HTTP sont de simples métadonnées que n'importe quel client peut modifier à volonté. `Referer` et `User-Agent` sont par nature non fiables et ne doivent jamais être utilisés à des fins de sécurité.
