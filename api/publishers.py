from flask import Blueprint, jsonify, request
from extensions import db

publishers_api = Blueprint('publishers_api', __name__)

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@publishers_api.route('/', methods=['GET'])
def get_publishers():
    publishers = Publisher.query.all()
    result = [{'id': p.id, 'name': p.name} for p in publishers]
    return jsonify(result)

@publishers_api.route('/', methods=['POST'])
def add_publisher():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': '缺少 name 字段'}), 400
    new_pub = Publisher(name=data['name'])
    db.session.add(new_pub)
    db.session.commit()
    return jsonify({'id': new_pub.id, 'name': new_pub.name}), 201

@publishers_api.route('/<int:publisher_id>', methods=['PUT'])
def update_publisher(publisher_id):
    pub = Publisher.query.get(publisher_id)
    if not pub:
        return jsonify({'error': '出版社不存在'}), 404
    data = request.json
    if 'name' in data:
        pub.name = data['name']
    db.session.commit()
    return jsonify({'id': pub.id, 'name': pub.name})

@publishers_api.route('/<int:publisher_id>', methods=['DELETE'])
def delete_publisher(publisher_id):
    pub = Publisher.query.get(publisher_id)
    if not pub:
        return jsonify({'error': '出版社不存在'}), 404
    db.session.delete(pub)
    db.session.commit()
    return jsonify({'message': '删除成功'})