À propos de ce tutoriel

Maintenant que nous avons vu la notion d'état on va faire une petite aparté sur l'utilisation des formulaires et des champs dans le cadre de React.

```jsx
export function App () {
    const [value, setValue] = useState('John doe')
    return <form>
        <input name="firstname" value={value}/>
    </form>
}
```

Si on crée un composant avec cette structure on se retrouvera avec un champs dans lequel il n'est pas possible de taper. En effet, React s'assure que le DOM correspond à ce que l'on a décrit et le champs garde la valeur "John doe" ici.

Pour solutionner ce problème il faudra s'assurer que l'on change l'état lorsque l'utilisateur interagit avec le champs.

```jsx
export function App () {
    const [value, setValue] = useState('John doe')
    const handleChange = e => {
        setValue(e.target.value)
    }

    return <form>
        <input name="firstname" value={value} onChange={handleChange}/>
    </form>
}
```

On notera que la propriété `onChange` ne fonctionne pas comme l'évènement natif `change` du navigateur. Ici la fonction sera appelé dès que la valeur est modifiée (et pas juste quand on désélectionne le champs).

Dans cette situation on parlera de champs **contrôlé**, c'est React qui contrôle le champs et sa valeur et l'état doit être synchronisé pour que ça fonctionne.

Cependant, il est aussi possible de ne pas passer de valeur au champs et dans ce cas là React vous laissera taper ce que vous voulez à l'intérieur. On aura la possibilité d'ajouter une propriété `defaultValue` pour spécifier la valeur initial.

```jsx
export function App () {
    const handleChange = e => {
        // On peut écouter les changements
    }

    return <form>
        <input name="firstname" defaultValue="John doe" onChange={handleChange}/>
    </form>
}
```

## Aller plus loin

[En apprendre plus sur la documentation](https://fr.react.dev/reference/react-dom/components/input#controlling-an-input-with-a-state-variable)