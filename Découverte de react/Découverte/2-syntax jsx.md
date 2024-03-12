
À propos de ce tutoriel

Dans ce chapitre je vous propose de découvrir la syntaxe JSX qui est une syntaxe spécifique utilisée par React pour représenter la structure HTML à injecter dans la page. Cette syntaxe est conçue comme une extension du javascript classique qui permet de décrire des éléments comme on le ferait dans une page HTML.

```jsx
export function App () {
    return <div>Bonjour les gens</div>
}
```

Cependant même si la syntaxe est relativement similaire à ce que l'on peut écrire au niveau de l'HTML il faudra faire attention à quelques détails :

- Les balises doivent être systématiquement fermées : `<img src="" alt=""/>`
- Les attributs sont écrit en camelCase sauf pour les attributs commençant par `data-` et `aria-` : `<input autoFocus/>`
- L'attribut `class` s'écrira `className` (pour éviter les conflits avec le mot clef `class` en JavaScript)
- L'attribut `for` s'écrira `htmlFor` (pour éviter les conflits avec le mot clef `for` en JavaScript).
- L'attribut `style` s'écrira sous forme d'objet avec les propriétés CSS écrites en camelCase `<div style={{width: 50, height: 50, backgroundColor: 'blue'}}/>`

Vous pouvez convertir du code HTML en JSX en utilisant [des outils de conversion](https://transform.tools/html-to-jsx).

Un autre point important est qu'une fonction ne doit renvoyer qu'un seul noeud JSX racine. Cependant, si on ne souhaite pas ajouter un élément HTML il est possible d'utiliser un fragment.

```jsx
export function App () {
    return <>
        <p>Premier paragraphe</p>
        <p>Second paragraphe</p>
    </>
}
```

## Interpoler les variables

Le gros avantage que va nous offrir cette syntaxe est la possibilité de pouvoir interpoler des variables au niveau de la structure HTML. Cette interpolation se fait à l'aide d'accolade.

```jsx
const text = 'Hello les gens'
const id = 'monid'
export function App () {
    return <h1 id={id}>{text}</h1>
}
```

Dans le cadre du JSX plusieurs éléments constituent des enfants valides :

- Une chaine de caractère
- Une valeur null, undefined ou false
- Un tableau d'éléments JSX

Cette règle va permettre d'utiliser du javascript au milieu d'éléments HTML afin de conditionner leur affichage.

```jsx
<>
    {title && <h1>{title}</h1>}
    <p>Mon texte</p>
</>
```

On aura aussi la possibilité d'utiliser des tableaux pour créer plusieurs enfants (on utilisera très souvent la fonction `map()`) . Dans le cas d'un tableau, il faudra rajouter un attribut `key` (unique pour chaque élément) pour spécifier une clé à chaque enfant (React utilise cette clef pour garder une trace de l'élément dans le DOM).

```jsx
const todos = [
    'Tâche 1',
    'Tâche 2',
    'Tâche 3'
]
export function App () {
    return <>
        <h1>Ma todolist</h1>
        <ul>
            {todos.map(todo => (<li key={todo}>{todo}</li>))}
        </ul>
    </>
}
```

## Écouteur d'évènement

La syntaxe JSX permettra aussi de brancher des écouteurs d'événements facilement sur nos éléments HTML. Cela se fera au travers d'attributs commençant par `on` qui recevront en paramètre une fonction qui sera exécutée lorsque l'événement est déclenché.

```jsx
export function App () {
    const doSomething = () => {
        alert('Bonjour !')
    }

    return <div onClick={doSomething}>Bonjour les gens</div>
}
```

Ses fonctions recevront en paramètre un événement sur lequel il sera possible d'utiliser des méthodes similaires à celles que l'on connaît pour les événements natifs du navigateur.

```jsx
export function App () {
    const doSomething = (e) => {
        e.preventDefault()
        e.stopPropagation()
    }

    return <form onSubmit={doSomething}>Bonjour les gens</div>
}
```

## Une fonction = Un composant

Lorsque l'on travaille avec React on va parler de "composants". Un composant est décrit sous la forme d'une fonction qui recevra les différents attributs sous forme d'objet et qui renverra du JSX.

```jsx
function Title ({color, children}) {
    return <h1 style={{color: color}}>{children}</h1>
}
```

Ensuite, il est ensuite possible d'utiliser ce composant comme une sorte d'élément HTML personnalisé.

```jsx
export function App () {
    return <>
        <Title color="red">Ceci est un titre</Title>
        <p>Premier paragraphe</p>
    </>
}
```

Ce découpage nous permettra d'éviter la répétition et on découpera notre application en plusieurs composants réutilisables.

## Aller plus loin

[En apprendre plus sur la documentation](https://fr.react.dev/learn/writing-markup-with-jsx)