À propos de ce tutoriel

Comme on l'a vu dans le chapitre parlant des changements d'état la fonction d'un composant est appelée à chaque nouveau rendu ce qui peut parfois amener à des problèmes si certains éléments sont complexes à calculer.

```jsx
function App () {
    const [password, setPassword] = useState('password')
    const [count, setCount] = useState(0)
    const hashedPassword = slowHashingMethod(password)

    return <div>
        <input type="text" value={password} onChange={e => setPassword(e.target.value)}/>
        Hash : {hashedPassword}
        Compteur : {count}
        <button onClick={setCount(v => v + 1)}>Incrémenter</button>
    </div>
}
```

Dans cette situation il est un petit peu dommage de demander à React de recalculer le hash du mot de passe si seul "count" change. Pour limiter l'impact en termes de performance on va avoir la possibilité d'utiliser la fonction `useMemo()` qui permettra de mémoriser une valeur tant que ses dépendances ne changent pas.

```jsx
function App () {
    const [password, setPassword] = useState('password')
    const [count, setCount] = useState(0)
    const hashedPassword = useMemo(() => {
        return slowHashingMethod(password)
    }, [password])

    return <div>
        <input type="text" value={password} onChange={e => setPassword(e.target.value)}/>
        Hash : {hashedPassword}
        Compteur : {count}
        <button onClick={setCount(v => v + 1)}>Incrémenter</button>
    </div>
}
```

Cette fonction n'aura d'autres utilisations que d'améliorer les performances afin de limiter les calculs . On pourrait alors être tenté de l'utiliser systématiquement , mais cela serait une mauvaise chose. Pour des opérations simples il est dommage d'utiliser plus de mémoire que nécessaire et on laissera dans ce cas là React refaire les calculs à chaque rendu. On réservera l'utilisation de cette fonction à des opérations lentes.

## Aller plus loin

[En apprendre plus sur la documentation](https://fr.react.dev/reference/react/useMemo)