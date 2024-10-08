"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Instancia de la familia
jackson_family = FamilyStructure("Jackson")

# Ruta para obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Ruta para agregar un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    member = request.json
    jackson_family.add_member(member)
    return jsonify({"message": "Member added successfully"}), 200

# Ruta para obtener un miembro específico por ID
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"message": "Member not found"}), 404

# Ruta para eliminar un miembro por ID
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    success = jackson_family.delete_member(id)
    if success:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"message": "Member not found"}), 404



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
