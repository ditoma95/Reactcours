À propos de ce tutoriel

Lors de notre TP on avait mis en place une navigation basée sur les hash dans l'url, mais dans un cas concret on va plutôt vouloir utiliser de jolies URL.

## Configuration serveur

Pour que ce type de navigation fonctionne, il est important que le serveur soit configuré pour rediriger toutes les URLs (qui ne correspondent pas à un fichier existant) vers le fichier `index.html`. C'est ensuite notre code JavaScript qui va se charger d'afficher le bon contenu en fonction de l'URL.

## La librairie react-router-dom

La librairie [react-router-dom](https://reactrouter.com/en/main) va nous permettre de déclarer les routes en amont, et gérera pour nous l'affichage.

```jsx
import * as React from "react";
import { createRoot } from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
  Route,
  Link,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/contact",
    element: <Contact />,
  },
]);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
```

N'hésitez pas à faire un petit tour sur la documentation pour [un petit aperçu des fonctionnalités offertes par react-router-dom](https://reactrouter.com/en/main/start/overview)