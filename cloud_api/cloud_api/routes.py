from flask import Blueprint, jsonify, current_app, request

main_routes = Blueprint('main', __name__)

# 1. Lister les Load Balancers
@main_routes.route('/loadbalancers', methods=['GET'])
def list_load_balancers():
    conn = current_app.config['OPENSTACK_CONNECTION']
    
    # Récupérer tous les Load Balancers existants
    lbs = conn.load_balancer.load_balancers()
    
    # Retourner la liste des Load Balancers sous forme de JSON
    return jsonify([lb.to_dict() for lb in lbs])

# 2. Créer un Load Balancer
@main_routes.route('/loadbalancers', methods=['POST'])
def create_load_balancer():
    conn = current_app.config['OPENSTACK_CONNECTION']
    
    # Créer un Load Balancer avec les paramètres spécifiés
    lb = conn.load_balancer.create_load_balancer(
        name='my-load-balancer',  # Le nom du Load Balancer
        vip_subnet_id='your-subnet-id',  # L'ID du sous-réseau où sera créé le LB
        admin_state_up=True
    )
    
    # Retourner les détails du Load Balancer créé
    return jsonify({"load_balancer": lb.to_dict()})

# 3. Supprimer un Load Balancer
@main_routes.route('/loadbalancers/<id>', methods=['DELETE'])
def delete_load_balancer(id):
    conn = current_app.config['OPENSTACK_CONNECTION']
    
    # Supprimer le Load Balancer spécifié par son ID
    conn.load_balancer.delete_load_balancer(id)
    
    # Retourner un message de confirmation
    return jsonify({"message": f"Load Balancer {id} deleted."})

# 1. Lister les serveurs (GET /servers)
@main_routes.route('/servers', methods=['GET'])
def list_servers():
    conn = current_app.config['OPENSTACK_CONNECTION']
    
    # Récupérer tous les serveurs
    servers = conn.compute.servers()
    
    # Retourner la liste des serveurs sous forme de JSON
    return jsonify([server.to_dict() for server in servers])

# 2. Créer un serveur (POST /servers)
@main_routes.route('/servers', methods=['POST'])
def create_server():
    conn = current_app.config['OPENSTACK_CONNECTION']
    
    # Récupérer les données envoyées dans la requête POST
    server_name = request.json.get('name')
    image_id = request.json.get('image_id')
    flavor_id = request.json.get('flavor_id')
    network_id = request.json.get('network_id')
    
    # Créer un serveur avec les paramètres spécifiés
    server = conn.compute.create_server(
        name=server_name,
        image_id=image_id,
        flavor_id=flavor_id,
        networks=[{"uuid": network_id}]
    )
    
    # Démarrer le serveur
    server = conn.compute.wait_for_server(server)
    
    # Retourner les détails du serveur créé
    return jsonify({"server": server.to_dict()})

# 3. Supprimer un serveur (DELETE /servers/<id>)
@main_routes.route('/servers/<id>', methods=['DELETE'])
def delete_server(id):
    conn = current_app.config['OPENSTACK_CONNECTION']
    
    # Supprimer le serveur spécifié par son ID
    conn.compute.delete_server(id)
    
    # Retourner un message de confirmation
    return jsonify({"message": f"Server {id} deleted."})