À propos de ce tutoriel

Dans ce chapitre nous allons voir comment organiser le flux de données au sein d'une application React. Jusqu'à maintenant on a vu qu'on avait la possibilité de morceler notre système en plusieurs composants avec la possibilité de faire descendre de l'information des composants parents vers les composants enfants grâce au système de propriété mais avec les évènements il va être possible de faire remonter les informations dans l'autre sens vers les composants parents.


## Étape 4 : identifier où l’état devrait vivre [](https://fr.react.dev/learn/thinking-in-react#step-4-identify-where-your-state-should-live "Link for Étape 4 : identifier où l’état devrait vivre")

Après avoir identifié les données d’état minimales de votre appli, vous allez devoir identifier quel composant est responsable de faire évoluer cet état, c’est-à-dire quel composant _possède_ l’état. Souvenez-vous : React utilise un flux de données unidirectionnel, où les données descendent le long de la hiérarchie des composants, des parents vers les enfants. Il n’est pas toujours immédiatement évident de savoir quel composant devrait posséder quel état. C’est difficile si ce concept est nouveau pour vous, mais vous pouvez trouver la réponse en utilisant les étapes qui suivent !

Pour chaque élément d’état de votre application :

1. Identifiez _chaque_ composant qui affiche quelque chose sur base de cet état.
2. Trouvez leur plus proche ancêtre commun : un composant qui est au-dessus d’eux tous dans l’aborescence.
3. Décidez où l’état devrait vivre :
    1. Le plus souvent, vous pourrez mettre l’état directement dans leur ancêtre commun.
    2. Vous pouvez aussi le mettre dans un composant au-dessus de leur ancêtre commun.
    3. Si vous ne trouvez aucun composant dans lequel il semble logique de placer l’état, créez un nouveau composant spécifiquement pour contenir l’état, et insérez-le dans l’arborescence juste au-dessus de leur ancêtre commun


# Props vs. état [](https://fr.react.dev/learn/thinking-in-react#props-vs-state "Link for Props vs. état")

Masquer les détails

React propose deux types de données de « modèle » : les props et l’état. Ces deux types diffèrent de façon drastique :

- [Les **props** sont comme des arguments que vous passez](https://fr.react.dev/learn/passing-props-to-a-component) à une fonction. Elles permettent au composant parent de passer des données à un composant enfant et de personnaliser ainsi son apparence. Par exemple, un `Form` pourrait passer une prop `color` à un `Button`.
- [L’**état** est comme la mémoire du composant](https://fr.react.dev/learn/state-a-components-memory). Il permet au composant de garder trace de certaines informations et de les modifier en réaction à des interactions. Par exemple, un `Button` pourrait vouloir garder trace de son état `isHovered`.

Les props et l’état sont très différents, mais ils collaborent. Un composant parent conservera souvent des informations dans son état (pour pouvoir les faire évoluer) qu’il va **passer** à ses composants enfants _via_ leurs props. Si la différence vous semble encore un peu floue après cette première lecture, ne vous en faites pas. Bien la saisir nécessite un peu de pratique !