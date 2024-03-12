
À propos de ce tutoriel

Le hook `useRef` va permettre de référencer une valeur qui n'est pas nécessaire au code du rendu et contrairement à l'état sa valeur pourra être mutée.

```js
const ref = useRef(initialValue)

// On peut ensuite modifier ou récupérer la valeur via la propriété "current"
ref.current = "Nouvelle valeur"
```

Lorsque l'on modifie la valeur à l'intérieur d'une référence il n'y a pas de changement d'état, le composant n'est alors pas re rendu. Aussi dans le code JSX on ne fera jamais appel à une référence.

```jsx
// Interdit !
return <div>{ref.current}</div>
```

## Ref et accès au DOM

Les références seront souvent utilisées pour récupérer un élément du DOM afin d'effectuer des opérations spécifiques.

```jsx
function App () {
    const inputRef = useRef(null)
    const handleClick = () => {
        inputRef.current.focus()
    }

    return <div>
        <input type="text" ref={inputRef}/>
        <button onClick={handleClick}>
            Focaliser le champs
            </button>
    </div>
}
```

## Aller plus loin

[En apprendre plus sur la documentation](https://fr.react.dev/reference/react/useRef#manipulating-the-dom-with-a-ref)