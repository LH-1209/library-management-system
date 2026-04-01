from flask import Blueprint, jsonify, request
from extensions import db

author_api = Blueprint('author_api', __name__)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@author_api.route('/', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    result = [{'id': a.id, 'name': a.name} for a in authors]
    return jsonify(result)

@author_api.route('/', methods=['POST'])
def add_author():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': '缺少 name 字段'}), 400
    new_author = Author(name=data['name'])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'id': new_author.id, 'name': new_author.name}), 201

@author_api.route('/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    author = Author.query.get(author_id)
    if not author:
        return jsonify({'error': '作者不存在'}), 404
    data = request.json
    if 'name' in data:
        author.name = data['name']
    db.session.commit()
    return jsonify({'id': author.id, 'name': author.name})

@author_api.route('/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = Author.query.get(author_id)
    if not author:
        return jsonify({'error': '作者不存在'}), 404
    db.session.delete(author)
    db.session.commit()
    return jsonify({'message': '删除成功'})