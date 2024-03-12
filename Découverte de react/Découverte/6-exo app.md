![[Pasted image 20231118172600.png]]
À propos de ce tutoriel

Dans ce chapitre je vous propose de pratiquer un peu tout ce que l'on a vu jusqu'à maintenant à travers un exemple concret. Cet exemple sera aussi l'occasion de voir comment il faut réfléchir avec React.

L'objectif de cet exercice est de créer un système de listing produit avec une fonctionnalité de recherche et de filtre.

```js
const PRODUCTS = [  
    {category: "Fruits", price: "$1", stocked: true, name: "Apple"},  
    {category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit"},  
    {category: "Fruits", price: "$2", stocked: false, name: "Passionfruit"},  
    {category: "Vegetables", price: "$2", stocked: true, name: "Spinach"},  
    {category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin"},  
    {category: "Vegetables", price: "$1", stocked: true, name: "Peas"}  
]
```

Avec une interface qui ressemblera à ça :
![[Pasted image 20231118172600.png]]


# Resolution:  
## E1 : Penser en Racte

![[s_thinking-in-react_ui_outline.png]]


1. `FilterableProductTable`(gris) contient l’intégralité de l’application.
2. `SearchBar`(bleu) reçoit l’entrée de l’utilisateur.
3. `ProductTable`(lavande) affiche et filtre la liste en fonction de la saisie de l'utilisateur.
4. `ProductCategoryRow`(vert) affiche un en-tête pour chaque catégorie.
5. `ProductRow` (jaune) affiche une ligne pour chaque produit.
## E2 : Créer une version statique dans React


```jsx

function ProductCategoryRow({ category }) {
  return (
    <tr>
      <th colSpan="2">
        {category}
      </th>
    </tr>
  );
}

function ProductRow({ product }) {
  const name = product.stocked ? product.name :
    <span style={{ color: 'red' }}>
      {product.name}
    </span>;

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
}

function ProductTable({ products }) {
  const rows = [];
  let lastCategory = null;

  products.forEach((product) => {
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category} />
      );
    }
    rows.push(
      <ProductRow
        product={product}
        key={product.name} />
    );
    lastCategory = product.category;
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  );
}

function SearchBar() {
  return (
    <form>
      <input type="text" placeholder="Search..." />
      <label>
        <input type="checkbox" />
        {' '}
        Only show products in stock
      </label>
    </form>
  );
}

function FilterableProductTable({ products }) {
  return (
    <div>
      <SearchBar />
      <ProductTable products={products} />
    </div>
  );
}

const PRODUCTS = [
  {category: "Fruits", price: "$1", stocked: true, name: "Apple"},
  {category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit"},
  {category: "Fruits", price: "$2", stocked: false, name: "Passionfruit"},
  {category: "Vegetables", price: "$2", stocked: true, name: "Spinach"},
  {category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin"},
  {category: "Vegetables", price: "$1", stocked: true, name: "Peas"}
];

export default function App() {
  return <FilterableProductTable products={PRODUCTS} />;
}
```



## E3 : Trouver la représentation minimale mais complète de l'état de l'interface utilisateur

Pour rendre l'interface utilisateur interactive, vous devez permettre aux utilisateurs de modifier votre modèle de données sous-jacent. Vous utiliserez _state_ pour cela.

Considérez l’état comme l’ensemble minimal de données changeantes dont votre application doit se souvenir. Le principe le plus important pour structurer l’état est de le garder [SEC (Ne vous répétez pas).](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) Déterminez la représentation minimale absolue de l’état dont votre application a besoin et calculez tout le reste à la demande. Par exemple, si vous créez une liste de courses, vous pouvez stocker les éléments sous forme de tableau dans l'état. Si vous souhaitez également afficher le nombre d'éléments dans la liste, ne stockez pas le nombre d'éléments comme une autre valeur d'état. Lisez plutôt la longueur de votre tableau.

Pensez maintenant à toutes les données de cet exemple d’application :

1. La liste originale des produits
2. Le texte de recherche que l'utilisateur a saisi
3. La valeur de la case à cocher
4. La liste filtrée des produits

Lesquels d'entre eux appartiennent à l'État ? Identifiez ceux qui ne le sont pas :

- Reste -t-il **inchangé** dans le temps ? Si c'est le cas, ce n'est pas un état.
- Est-il **transmis par un parent** via des accessoires ? Si c'est le cas, ce n'est pas un état.
- **Pouvez-vous le calculer** en fonction de l'état ou des accessoires existants dans votre composant ? Si c'est le cas, ce n'est _certainement pas un état !_

Ce qui reste, c'est probablement l'État.

Reprenons-les un par un :

1. La liste originale des produits est **transmise en tant qu'accessoires, ce n'est donc pas un état.**
2. Le texte recherché semble être un état puisqu'il change avec le temps et ne peut être calculé à partir de rien.
3. La valeur de la case à cocher semble être un état puisqu'elle change avec le temps et ne peut être calculée à partir de rien.
4. La liste filtrée des produits **n'est pas un état car elle peut être calculée** en prenant la liste originale des produits et en la filtrant en fonction du texte de recherche et de la valeur de la case à cocher.

## E4 : Identifiez où votre État devrait vivre

Après avoir identifié les données d'état minimales de votre application, vous devez identifier quel composant est responsable de la modification de cet état ou _est propriétaire_ de cet état. N'oubliez pas : React utilise un flux de données unidirectionnel, transmettant les données dans la hiérarchie des composants, du composant parent au composant enfant. Il n’est peut-être pas immédiatement clair quel composant doit posséder quel état. Cela peut être difficile si vous êtes nouveau dans ce concept, mais vous pouvez le comprendre en suivant ces étapes !

Pour chaque élément d'état de votre candidature :

1. Identifiez _chaque_ composant qui restitue quelque chose en fonction de cet état.
2. Recherchez le composant parent commun le plus proche, un composant situé au-dessus d'eux tous dans la hiérarchie.
3. Décidez où l’État doit vivre :
    1. Souvent, vous pouvez placer l’État directement dans leur société mère commune.
    2. Vous pouvez également placer l'état dans un composant situé au-dessus de son parent commun.
    3. Si vous ne trouvez pas de composant pour lequel il est logique de posséder l'état, créez un nouveau composant uniquement pour contenir l'état et ajoutez-le quelque part dans la hiérarchie au-dessus du composant parent commun.

À l'étape précédente, vous avez trouvé deux éléments d'état dans cette application : le texte de saisie de la recherche et la valeur de la case à cocher. Dans cet exemple, ils apparaissent toujours ensemble, il est donc logique de les placer au même endroit.

Passons maintenant en revue notre stratégie pour eux :

1. **Identifiez les composants qui utilisent l'état :**
    - `ProductTable`doit filtrer la liste de produits en fonction de cet état (texte de recherche et valeur de la case à cocher).
    - `SearchBar`doit afficher cet état (texte de recherche et valeur de la case à cocher).
2. **Recherchez leur parent commun :** le premier composant parent que les deux composants partagent est `FilterableProductTable`.
3. **Décidez où réside l'état** : nous conserverons le texte du filtre et les valeurs d'état vérifiées dans `FilterableProductTable`.

Ainsi, les valeurs de l’État vivront `FilterableProductTable`.

Ajoutez un état au composant avec le [`useState()`Hook.](https://react.dev/reference/react/useState) Les hooks sont des fonctions spéciales qui vous permettent de vous « connecter » à React. Ajoutez deux variables d'état en haut de `FilterableProductTable`et spécifiez leur état initial

``

```jsx
import { useState } from 'react';

function FilterableProductTable({ products }) {
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);

  return (
    <div>
      <SearchBar 
        filterText={filterText} 
        inStockOnly={inStockOnly} />
      <ProductTable 
        products={products}
        filterText={filterText}
        inStockOnly={inStockOnly} />
    </div>
  );
}

function ProductCategoryRow({ category }) {
  return (
    <tr>
      <th colSpan="2">
        {category}
      </th>
    </tr>
  );
}

function ProductRow({ product }) {
  const name = product.stocked ? product.name :
    <span style={{ color: 'red' }}>
      {product.name}
    </span>;

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
}

function ProductTable({ products, filterText, inStockOnly }) {
  const rows = [];
  let lastCategory = null;

  products.forEach((product) => {
    if (
      product.name.toLowerCase().indexOf(
        filterText.toLowerCase()
      ) === -1
    ) {
      return;
    }
    if (inStockOnly && !product.stocked) {
      return;
    }
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category} />
      );
    }
    rows.push(
      <ProductRow
        product={product}
        key={product.name} />
    );
    lastCategory = product.category;
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  );
}

function SearchBar({ filterText, inStockOnly }) {
  return (
    <form>
      <input 
        type="text" 
        value={filterText} 
        placeholder="Search..."/>
      <label>
        <input 
          type="checkbox" 
          checked={inStockOnly} />
        {' '}
        Only show products in stock
      </label>
    </form>
  );
}

const PRODUCTS = [
  {category: "Fruits", price: "$1", stocked: true, name: "Apple"},
  {category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit"},
  {category: "Fruits", price: "$2", stocked: false, name: "Passionfruit"},
  {category: "Vegetables", price: "$2", stocked: true, name: "Spinach"},
  {category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin"},
  {category: "Vegetables", price: "$1", stocked: true, name: "Peas"}
];

export default function App() {
  return <FilterableProductTable products={PRODUCTS} />;
}

```





## E5 : Ajouter un flux de données inverse

Actuellement, votre application s'affiche correctement avec les accessoires et l'état descendant dans la hiérarchie. Mais pour modifier l'état en fonction des entrées de l'utilisateur, vous devrez prendre en charge le flux de données dans l'autre sens : les composants du formulaire situés au plus profond de la hiérarchie doivent mettre à jour l'état dans `FilterableProductTable`.

React rend ce flux de données explicite, mais cela nécessite un peu plus de saisie que la liaison de données bidirectionnelle. Si vous essayez de taper ou de cocher la case dans l'exemple ci-dessus, vous verrez que React ignore votre saisie. C'est intentionnel. En écrivant `<input value={filterText} />`, vous avez défini la `value`prop de the `input`pour qu'elle soit toujours égale à l' `filterText`état transmis par `FilterableProductTable`. Puisque `filterText`l'état n'est jamais défini, l'entrée ne change jamais.

Vous souhaitez faire en sorte que chaque fois que l'utilisateur modifie les entrées du formulaire, l'état soit mis à jour pour refléter ces modifications. L'État appartient à `FilterableProductTable`, donc lui seul peut appeler `setFilterText`et `setInStockOnly`. Pour permettre `SearchBar`la mise à jour de l' `FilterableProductTable`état de , vous devez transmettre ces fonctions à`SearchBar` :



```jsx
import { useState } from 'react';

function FilterableProductTable({ products }) {
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);

  return (
    <div>
      <SearchBar 
        filterText={filterText} 
        inStockOnly={inStockOnly} 
        onFilterTextChange={setFilterText} 
        onInStockOnlyChange={setInStockOnly} />
      <ProductTable 
        products={products} 
        filterText={filterText}
        inStockOnly={inStockOnly} />
    </div>
  );
}

function ProductCategoryRow({ category }) {
  return (
    <tr>
      <th colSpan="2">
        {category}
      </th>
    </tr>
  );
}

function ProductRow({ product }) {
  const name = product.stocked ? product.name :
    <span style={{ color: 'red' }}>
      {product.name}
    </span>;

  return (
    <tr>
      <td>{name}</td>
      <td>{product.price}</td>
    </tr>
  );
}

function ProductTable({ products, filterText, inStockOnly }) {
  const rows = [];
  let lastCategory = null;

  products.forEach((product) => {
    if (
      product.name.toLowerCase().indexOf(
        filterText.toLowerCase()
      ) === -1
    ) {
      return;
    }
    if (inStockOnly && !product.stocked) {
      return;
    }
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category} />
      );
    }
    rows.push(
      <ProductRow
        product={product}
        key={product.name} />
    );
    lastCategory = product.category;
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  );
}

function SearchBar({
  filterText,
  inStockOnly,
  onFilterTextChange,
  onInStockOnlyChange
}) {
  return (
    <form>
      <input 
        type="text" 
        value={filterText} placeholder="Search..." 
        onChange={(e) => onFilterTextChange(e.target.value)} />
      <label>
        <input 
          type="checkbox" 
          checked={inStockOnly} 
          onChange={(e) => onInStockOnlyChange(e.target.checked)} />
        {' '}
        Only show products in stock
      </label>
    </form>
  );
}

const PRODUCTS = [
  {category: "Fruits", price: "$1", stocked: true, name: "Apple"},
  {category: "Fruits", price: "$1", stocked: true, name: "Dragonfruit"},
  {category: "Fruits", price: "$2", stocked: false, name: "Passionfruit"},
  {category: "Vegetables", price: "$2", stocked: true, name: "Spinach"},
  {category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin"},
  {category: "Vegetables", price: "$1", stocked: true, name: "Peas"}
];

export default function App() {
  return <FilterableProductTable products={PRODUCTS} />;
}
```
