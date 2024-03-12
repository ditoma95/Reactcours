
## Introduction

React est une bibliothèque JavaScript qui permet de simplifier la création d’interface. Elle permet une synchronisation plus simple et plus efficace entre les données de votre application et le rendu HTML.

Explication: 
	- Quelle problème  react essai de réglé 
	
	![[Capture d’écran du 2023-11-16 10-46-44.png]]



## Petit Rappel

- **Fonctions Fléchées**
- **map() , filter , reduice()**


## Terminologie


1. **HOC**
    
    - Les composants haut ordre (Higher Order Components - HOC) sont des fonctions qui prennent un composant et renvoient un nouveau composant avec des fonctionnalités supplémentaires.
2. **Composant (Component) :**
    
    - Un composant est une partie réutilisable de l'interface utilisateur qui peut contenir de la logique et des éléments d'interface. Les composants peuvent être imbriqués pour construire des interfaces plus complexes.
3. **Propriétés (Props) :**
    
    - Les propriétés sont des valeurs que vous pouvez passer à un composant pour influencer son comportement ou son rendu. Les props sont définies dans le composant parent et sont accessibles dans le composant enfant.
4. **État (State) :**
    
    - L'état représente les données internes d'un composant qui peuvent changer au fil du temps. Lorsque l'état d'un composant change, le composant est réexécuté pour refléter cette modification.
5. **Cycle de Vie (Lifecycle) :**
    
    - Le cycle de vie d'un composant se réfère aux différentes étapes qu'il traverse, de sa création à sa destruction. Chaque étape offre des points d'accroche où vous pouvez exécuter du code spécifique.
5. **Rendu conditionnel :**
    
    - Le rendu conditionnel se produit lorsque vous décidez quel contenu afficher en fonction d'une condition. Cela peut être réalisé avec des structures de contrôle comme `if` ou l'opérateur ternaire.

1. **Hooks :**
    
    - Les hooks sont des fonctions spéciales qui permettent d'utiliser l'état et d'autres fonctionnalités de React dans les composants fonctionnels. Parmi les hooks les plus couramment utilisés, citons `useState`, `useEffect`, `useContext`, etc.
8. **JSX :**
    
	- JSX est une syntaxe de langage de balisage utilisée avec React pour décrire à quoi devrait ressembler l'interface utilisateur. C'est une extension de la syntaxe JavaScript qui ressemble à du XML/HTML.
9. **Bundleur**  #vite
		Un "bundler" (ou "bundleur") est un outil qui combine et regroupe plusieurs fichiers source (tels que des fichiers JavaScript, CSS, ou d'autres ressources) en un seul fichier (le "bundle"). Cela permet de réduire le nombre de requêtes réseau nécessaires pour charger une application web et d'optimiser les performances.
		#Vite
		**Pourquoi utiliser Vite?**

			- rafrechissement automatique
			- bundler le projer js
			- import de ficher non javaScript
			- Utilistaion de module nodjs-backend du coté fronte si il est prix en charge
1. **Babel** 
	  permet aux développeurs d'utiliser des fonctionnalités JavaScript modernes avant même qu'elles soient prises en charge nativement par les navigateurs. Cela inclut l'utilisation de syntaxe telle que les fonctions fléchées, les modules, les classes, etc.

## Les différents Type de rendu


1. **Rendu Côté Serveur (SSR - Server-Side Rendering) :**
    
    - **Description :** Dans le rendu côté serveur, le contenu de la page est généré sur le serveur avant d'être envoyé au navigateur de l'utilisateur. Le serveur renvoie une page HTML complète, généralement avec les données préremplies.
    - **Avantages :** Le contenu est indexable par les moteurs de recherche, le temps de chargement initial peut être plus rapide.
    - **Inconvénients :** Le temps de rendu dépend du serveur, la complexité de la gestion de l'état côté client peut augmenter.
2. **Rendu Côté Client (CSR - Client-Side Rendering) :**
    
    - **Description :** Dans le rendu côté client, le serveur envoie une page HTML minimale au navigateur, et le rendu final est effectué par le navigateur lui-même à l'aide de JavaScript. Les données peuvent être récupérées et affichées après le chargement initial.
    - **Avantages :** Une fois la page chargée, les interactions peuvent être plus rapides, possibilité de créer des applications monopage (SPA).
    - **Inconvénients :** Le contenu n'est pas indexable de manière optimale par les moteurs de recherche, le temps de chargement initial peut être plus long.
3. **Rendu Hybride (Hybrid Rendering) :**
    
    - **Description :** Le rendu hybride combine à la fois le rendu côté serveur et le rendu côté client. Certains éléments de la page sont rendus côté serveur, tandis que d'autres sont rendus côté client après le chargement initial.
    - **Avantages :** Combinaison des avantages du SSR et du CSR, permet une meilleure expérience utilisateur.
    - **Inconvénients :** Complexité accrue dans la mise en œuvre et la maintenance.