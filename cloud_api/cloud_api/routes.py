from flask import Blueprint, jsonify, current_app

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