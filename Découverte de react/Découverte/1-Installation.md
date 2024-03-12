
À propos de ce tutoriel

Dans ce premier chapitre, nous allons voir comment commencer à utiliser React. Si vous voulez commencer simplement sans avoir à configurer de chose sur votre ordinateur vous pouvez utiliser l'éditeur en ligne CodeSandbox en utilisant le [modèle fournit sur la documentation](https://react.dev/learn) (en cliquant sur "fork").

Si on souhaite travailler en local avec React, il va falloir utiliser un outil spécifique pour convertir la syntaxe utilisée par la librairie (JSX) en JavaScript interprétable par le navigateur. Il existe plusieurs outils, mais nous allons utiliser [Vite](https://grafikart.fr/tutoriels/javascript-vite-1351) qui est à mon sens le plus simple d'utilisation. On peut créer un projet avec en une simple commande :


Installer node:https://github.com/nodesource/distributions/blob/master/README.md#ubuntu-versions

Installer via snap: https://github.com/nodejs/snap

1. **Installer une nouvelle version de Node.js :**
    
    - Choisissez et installez la version de Node.js souhaitée avec NVM :
    
        `nvm install <version>`
2. **Sélectionner la nouvelle version de Node.js :**
    
    - Sélectionnez la version installée :
        `nvm use <version>`
        ou définissez la version par défaut :
        `nvm alias default <version>`
        
3. **Vérifier la version installée :**
    - Vérifiez la version installée :
        
        `node --version `
        `npm --version`


Avec npm :

```bash
npm create vite@latest
```

Avec yarn :

```bash
yarn create vite
```

Avec PNPM :

```bash
pnpm create vite
```

L'installeur vous demandera alors le modèle à utiliser et on va sélectionner "react", et dans le second choix on va utiliser "JavaScript".

Une fois l'installation faite, il vous indiquera la marche à suivre pour lancer le projet.

- On commence par installer les dépendances avec le gestionnaire notre gestionnaire de paquet (pnpm, npm, yarn...).
- On peut ensuite démarrer le serveur de développement à l'aide du script "dev". Ce serveur sera ensuite accessible sur le port "5173" par défaut. Vous pouvez alors ouvrir la page "[http://localhost:5173](http://localhost:5173/)" sur votre navigateur.