# OpenInfraFlask

OpenInfraFlask est une API REST développée en Flask qui permet de gérer des ressources d'infrastructure cloud sur OpenStack, telles que les Load Balancers et les serveurs (machines virtuelles). Le projet utilise le SDK OpenStack pour interagir avec les services OpenStack, et permet de créer, lister et supprimer des ressources cloud de manière simple via des endpoints API.

## Technologies utilisées
- Python 3
- Flask - Framework léger pour créer des API REST.
- OpenStack SDK - Interagis avec les services OpenStack via leur API.
- Poetry - Outil de gestion des dépendances et des environnements virtuels.
- Dotenv - Chargement des variables d'environnement depuis un fichier .env.

## Fonctionnalités
1. Load Balancers
- Lister les Load Balancers : Récupérer la liste des Load Balancers existants sur OpenStack.
- Créer un Load Balancer : Créer un nouveau Load Balancer sur un sous-réseau spécifié.
- Supprimer un Load Balancer : Supprimer un Load Balancer existant en spécifiant son ID.

2. Serveurs (Machines virtuelles)
- Lister les serveurs : Récupérer la liste des serveurs (machines virtuelles) sur OpenStack.
- Créer un serveur : Créer un nouveau serveur (instance) en spécifiant un nom, une image, une taille (flavor), et un réseau.
- Supprimer un serveur : Supprimer un serveur existant en spécifiant son ID.