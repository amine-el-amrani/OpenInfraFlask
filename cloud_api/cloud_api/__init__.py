from flask import Flask
from dotenv import load_dotenv
import os
import openstack

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Connexion à OpenStack avec les variables d'environnement
    conn = openstack.connect(
        auth_url=os.getenv('OS_AUTH_URL'),
        project_name=os.getenv('OS_PROJECT_NAME'),
        username=os.getenv('OS_USERNAME'),
        password=os.getenv('OS_PASSWORD'),
        user_domain_name=os.getenv('OS_USER_DOMAIN_NAME'),
        project_domain_name=os.getenv('OS_PROJECT_DOMAIN_NAME'),
        region_name=os.getenv('OS_REGION_NAME')
    )

    # Mettre la connexion à OpenStack dans la configuration de l'application
    app.config['OPENSTACK_CONNECTION'] = conn

    # Importer les routes
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app