`Component`est la classe de base pour les composants React définis comme [classes JavaScript.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) Les composants de classe sont toujours pris en charge par React, mais nous ne recommandons pas de les utiliser dans du nouveau code.

```jsx
import { Component } from 'react';  

class Greeting extends Component {  
	render() {  
		return <h1>Hello, {this.props.name}!</h1>;  
	}  
}
```

### `state` [](https://react.dev/reference/react/Component#state "Lien vers cette rubrique")

L'état d'un composant de classe est disponible sous forme de fichier `this.state`. Le `state`champ doit être un objet. Ne modifiez pas l’état directement. Si vous souhaitez changer d'état, appelez `setState`auprès du nouvel état.

```jsx
class Counter extends Component {  
	state = {  
		age: 42,  
	};  
	handleAgeChange = () => {
		this.setState({  
			age: this.state.age + 1  
		});
	};  
	
	render() {  
		return (  
			<>  
				<button onClick={this.handleAgeChange}>  
					Increment age  
				</button>  
				<p>You are {this.state.age}.</p>  
			</>  
		);  
	}  
}
```

Définir `state`des composants en classe équivaut à appeler [`useState`](https://react.dev/reference/react/useState)des composants de fonction.

### Migration d'un composant simple d'une classe vers une fonction


```jsx
function App () {
    return <div>Bonjour les gens</div>
}
```
