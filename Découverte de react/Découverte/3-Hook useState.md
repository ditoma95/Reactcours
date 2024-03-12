À propos de ce tutoriel

Le principal intérêt de React va être la possibilité de créer une interface réactive qui évolue en fonction des interactions faites par l'utilisateur. En plus des propriétés que l'on reçoit en paramètres des fonctions nous allons pouvoir générer un état (sorte de mémoire interne à notre composant) qui sera ensuite utilisé dans notre rendu JSX. On aura ensuite la possibilité de modifier cet état et React se chargera de refléter les modifications à l'écran.

```jsx
import { useState } from 'react'

export function Counter () {
    const [count, setCount] = useState(0)
    const increment = () => setCount(count + 1)

    return(
	    <div>
	        <p>Compteur : {count}</p>
	        <button onClick={increment}>Incrémenter</button>
	    </div>
    )
}
```


Le setter peut être appelé de 2 manières différentes

- Avec la nouvelle valeur : `setCount(3)`
- Avec une fonction qui prendra la valeur courante de l'état et qui renverra la nouvelle valeur : `setCount(n => n+1)`

## Le rerendu

Cette syntaxe peut sembler étrange mais il faut comprendre comment REACT va fonctionner lorsqu'il y a un changement de valeur.

À l'initialisation notre fonction va être appelée et va renvoyer un noeud JSX qui va représenter la structure HTML que l'on souhaite injecter dans la page. Lorsque la fonction `useState` est appelée, React réserve un petit espace mémoire pour sauvegarder la valeur. Ce nœud sera ensuite traité par la librairie `react-dom` qui va l'injecter dans le DOM.

Lors de l'action utilisateur, le setter est appelé et va changer la valeur dans l'espace mémoire associé en notifiant React qu'il y a eu un changement au niveau de ce composant. React va donc appeler la fonction à nouveau pour obtenir la nouvelle version du noeud JSX.

Ce noeud sera comparé à l'ancienne version pour déterminer les modification à effectuer au niveau du DOM.

## La notion de hook

Dans le cadre de react les fonction comme `useState` seront appelées des "hooks" et ce sont des fonctions qui ont plusieurs caractéristique

- Un hook sera toujours nommé en commençant par `use`
- Un hook ne peut être appelé en dehors d'un composant
- Les hooks doivent toujours être appelé dans le même ordre (React utilise l'ordre d'appel pour associer les valeurs lors des rendus consécutif) et en même quantité (pas de hook dans une condition par exemple).

## Aller plus loin

[En apprendre plus sur la documentation](https://fr.react.dev/learn/state-a-components-memory)