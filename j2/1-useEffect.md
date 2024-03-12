# #DOC-Les-Effets



> **C'est quoi un Effet**
>**Les _Effets_ vous permettent de spécifier des effets de bord causés par le rendu lui-même, plutôt que par un événement particulier.** **Envoyer un message dans la discussion est un _événement_, parce que c’est directement lié au fait que l’utilisateur a cliqué sur un bouton précis. En revanche, mettre en place la connexion au serveur est un _Effet_ parce que ça doit se produire quelle que soit l’interaction qui a entraîné l’affichage du composant. Les Effets sont exécutés à la fin de la phase de commit, après que l’écran a été mis à jour. C’est le bon moment pour synchroniser les composants React avec des systèmes extérieurs (comme par exemple le réseau ou une bibliothèque tierce).**
> 

## Vous n’avez pas forcément besoin d’un Effet [](https://fr.react.dev/learn/synchronizing-with-effects#you-might-not-need-an-effect "Link for Vous n’avez pas forcément besoin d’un Effet")

**Ne vous précipitez pas pour ajouter des Effets à vos composants.** Gardez à l’esprit que les Effets sont généralement utilisés pour « sortir » de votre code React et vous synchroniser avec un système _extérieur_. Ça inclut les API du navigateur, des _widgets_ tiers, le réseau, etc. Si votre Effet se contente d’ajuster des variables d’état sur la base d’autres éléments d’état, [vous n’avez pas forcément besoin d’un Effet](https://fr.react.dev/learn/you-might-not-need-an-effect).
## Étape 1 : déclarez un Effet [](https://fr.react.dev/learn/synchronizing-with-effects#step-1-declare-an-effect "Link for Étape 1 : déclarez un Effet")

Pour déclarer un Effet dans votre composant, importez le [Hook `useEffect`](https://fr.react.dev/reference/react/useEffect) depuis React :

```jsx
import { useEffect } from 'react';
```

Ensuite, appelez-le au niveau racine de votre composant et placez le code adéquat dans votre Effet :

```jsx
function MyComponent() {  
	useEffect(() => {    
		// Du code ici qui s’exécutera après *chaque* rendu  
	});  
	return <div />;
}
```

Chaque fois que le composant calculera son rendu, React mettra l’affichage à jour _et ensuite_ exécutera le code au sein du `useEffect`. En d’autres termes, **`useEffect` « retarde » l’exécution de ce bout de code jusqu’à ce que le résultat du rendu se reflète à l’écran.**
## Exo useEffect

Voyons comment vous pouvez utiliser un Effet pour vous synchroniser avec un système extérieur. Prenons un composant React `<VideoPlayer>`. Ce serait chouette de pouvoir contrôler son état de lecture (en cours ou en pause) en lui passant une prop `isPlaying` :

```
<VideoPlayer isPlaying={isPlaying} />
```

Votre composant personnalisé `VideoPlayer` utilise la balise native [`<video>`](https://developer.mozilla.org/fr/docs/Web/HTML/Element/video) du navigateur :

```jsx
function VideoPlayer({ src, isPlaying }) {  
	// TODO: se servir de isPlaying  
	return <video src={src} />;
}
```
## Correction

```jsx
import { useState, useRef, useEffect } from 'react';

function VideoPlayer({ src, isPlaying }) {
	const ref = useRef(null);
	useEffect(()=>{
		if (isPlaying) {
			// Ces appels sont interdits pendant le rendu.
			ref.current.play();
		} else {
			// En plus, ça plante.
			ref.current.pause();
		}
	})
	return <video ref={ref} src={src} loop playsInline />;
}
export default function App() {
	const [isPlaying, setIsPlaying] = useState(false);
	return (
		<>
			<button onClick={() => setIsPlaying(!isPlaying)}>
				{isPlaying ? 'Pause' : 'Lecture'}
			</button>
			<VideoPlayer
			isPlaying={isPlaying}
			src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
			/>
		</>
	);
}
```
## PiègeEffets

Par défaut, les Effets s’exécutent après _chaque_ rendu. C’est pourquoi le code suivant **produirait une boucle infinie :**

```jsx
const [count, setCount] = useState(0);
useEffect(() => {  
	setCount(count + 1);
});
```

Les Effets s’exécutent _en conséquence_ d’un rendu. Modifier l’état _déclenche_ un rendu. Le modifier au sein d’un Effet, c’est un peu comme brancher une multiprise sur elle-même. L’Effet s’exécute, modifie l’état, ce qui entraîne un nouveau rendu, ce qui déclenche une nouvelle exécution de l’Effet, qui modifie à nouveau l’état, entraînant un nouveau rendu, et ainsi de suite.

Les Effets ne devraient normalement synchroniser vos composants qu’avec des systèmes _extérieurs_. S’il n’y a pas de système extérieur et que vous voulez seulement ajuster un bout d’état sur base d’un autre, [vous n’avez pas forcément besoin d’un Effet](https://fr.react.dev/learn/you-might-not-need-an-effect).

## Étape 2 : spécifiez les dépendances de l’Effet

Par défaut, les Effets s’exécutent après _chaque_ rendu. Souvent pourtant, **ce n’est pas ce que vous voulez** :

- Parfois, c’est lent. La synchronisation avec un système extérieur n’est pas toujours instantanée, aussi vous pourriez vouloir l’éviter si elle est superflue. Par exemple, vous ne souhaitez pas vous reconnecter au serveur de discussion à chaque frappe clavier.
- Parfois, c’est incorrect. Par exemple, vous ne voulez pas déclencher une animation de fondu entrant à chaque frappe clavier. L’animation ne devrait se dérouler qu’une seule fois, après que le composant apparaît.

Pour mettre ce problème en évidence, revoici l’exemple précédent avec quelques appels à `console.log` en plus, et un champ de saisie textuelle qui met à jour l’état du parent. Voyez comme la saisie entraîne la ré-exécution de l’Effet :
#problème
```jsx
import { useState, useRef, useEffect } from 'react';

function VideoPlayer({ src, isPlaying }) {
  const ref = useRef(null);

  useEffect(() => {
    if (isPlaying) {
      console.log('Appel à video.play()');
      ref.current.play();
    } else {
      console.log('Appel à video.pause()');
      ref.current.pause();
    }
  });

  return <video ref={ref} src={src} loop playsInline />;
}

export default function App() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [text, setText] = useState('');
  return (
    <>
      <input value={text} onChange={e => setText(e.target.value)} />
      <button onClick={() => setIsPlaying(!isPlaying)}>
        {isPlaying ? 'Pause' : 'Lecture'}
      </button>
      <VideoPlayer
        isPlaying={isPlaying}
        src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
      />
    </>
  );
}

```
#Solution
```jsx
useEffect(() => {
    if (isPlaying) {
      console.log('Appel à video.play()');
      ref.current.play();
    } else {
      console.log('Appel à video.pause()');
      ref.current.pause();
    }
  }, [isPlaying]); // Là, on va avoir un problème
  return <video ref={ref} src={src} loop playsInline />;
}
```

En spécifiant `[isPlaying]` comme tableau de dépendances, nous disons à React qu’il devrait éviter de ré-exécuter votre Effet si `isPlaying` n’a pas changé depuis le rendu précédent. Grâce à cet ajustement, la saisie dans le champ n’entraîne plus la ré-exécution de l’Effet, mais activer Lecture / Pause si :


### Piège

Le comportement n’est pas le même entre une absence du tableau de dépendances, et un tableau de dépendances _vide_ `[]` :

```jsx
useEffect(() => {  
	// S’exécute après chaque rendu
});
useEffect(() => {  
	// S’exécute uniquement au montage (apparition du composant)
}, []);
useEffect(() => {  
	// S’exécute au montage *mais aussi* si a ou b changent depuis le rendu précédent
}, [a, b]);
```

Nous verrons de plus près ce que « montage » signifie lors de la prochaine étape.

#### Pourquoi n’a-t-on pas ajouté la ref au tableau de dépendances ?
A votre avis 

## Étape 3 : ajoutez du code de nettoyage si besoin

Prenons un autre exemple. Vous écrivez un composant `ChatRoom` qui a besoin de se connecter à un serveur de discussion lorsqu’il apparaît. Vous disposez d’une API `createConnection()` qui renvoie un objet avec des méthodes `connect()` et `disconnect()`. Comment garder votre composant connecté pendant qu’il est affiché à l’utilisateur ?

Commencez par écrire le code de l’Effet :

```
useEffect(() => {  const connection = createConnection();  connection.connect();});
```

Ce serait toutefois beaucoup trop lent de vous (re)connecter après chaque rendu ; vous spécifiez donc un tableau de dépendances :

```
useEffect(() => {  const connection = createConnection();  connection.connect();}, []);
```

**Le code dans l’Effet n’utilise ni props ni état, donc votre tableau de dépendances est vide `[]`. Vous indiquez ici à React qu’il ne faut exécuter le code que lors du « montage » du composant, c’est-à-dire lorsque celui-ci apparaît à l’écran pour la première fois.**

App.js
```jsx
import { useEffect } from 'react';
import { createConnection } from './chat.js';

export default function ChatRoom() {
  useEffect(() => {
    const connection = createConnection();
    connection.connect();
  }, []);
  return <h1>Bienvenue dans la discussion !</h1>;
}

```
chat.js
```jsx
export function createConnection() {
  // Une véritable implémentation se connecterait en vrai
  return {
    connect() {
      console.log('✅ Connexion...');
    },
    disconnect() {
      console.log('❌ Déconnecté.');
    }
  };
}
```
Cet Effet n’est exécuté qu’au montage, vous vous attendez donc sans doute à ce que `"✅ Connexion..."` ne soit logué qu’une fois en console. **Et pourtant, en vérifiant la console, vous voyez deux occurrences de `"✅ Connexion..."`. Qu’est-ce qui se passe ?**

#SOLUTION:
Ajouter une fonction de  nettoyage du useEffect qui s' exécuterrat apres chaque demontage du composant
```jsx
return () => {  
	connection.disconnect();  
};
```

Vous voyez maintenant trois logs dans la console en mode développement :

1. `"✅ Connexion..."`
2. `"❌ Déconnecté."`
3. `"✅ Connexion..."`
**C’est le comportement correct en développement. En StrictMode **

### La plupart des Effets que vous aurez à écrire correspondront à un des scénarios courants ci-après.

- #### Contrôler_des_widgets_non_React
- #### S’abonner à des événements
- #### Déclencher des animations
- #### Charger des données

## En résumé[](https://fr.react.dev/learn/synchronizing-with-effects#recap "Link for En résumé")

- Contrairement aux événements, les Effets sont déclenchés par le rendu lui-même plutôt que par une interaction spécifique.
- Les Effets vous permettent de synchroniser un composant avec un système extérieur (API tierce, appel réseau, etc.)
- Par défaut, les Effets sont exécutés après chaque rendu (y compris le premier).
- React sautera un Effet si toutes ses dépendances ont des valeurs identiques à celles du rendu précédent.
- Vous ne pouvez pas « choisir » vos dépendances. Elles sont déterminées par le code au sein de l’Effet.
- Un tableau de dépendances vide (`[]`) correspond à une exécution seulement lors du « montage » du composant, c’est-à-dire son apparition à l’écran.
- En mode strict, React monte les composants deux fois (seulement en développement !) pour éprouver la qualité d’implémentation des Effets.
- Si votre Effet casse en raison du remontage, vous devez implémenter sa fonction de nettoyage.
- React appellera votre fonction de nettoyage avant l’exécution suivante de l’Effet, ainsi qu’au démontage.


[En apprendre plus sur la documentation](https://fr.react.dev/learn/synchronizing-with-effects)

# #GRAFIKART

Lien vers le cours de grafikart

https://grafikart.fr/tutoriels/react-hook-useeffect-1328#autoplay