from flask import Blueprint, jsonify, request
from extensions import db

book_api = Blueprint('book_api', __name__)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=True)

    # 使用字符串引用模型，避免循环导入
    author = db.relationship('Author', backref='books')
    publisher = db.relationship('Publisher', backref='books')

@book_api.route('/', methods=['GET'])
def get_books():
    books = Book.query.all()
    result = []
    for b in books:
        result.append({
            'id': b.id,
            'title': b.title,
            'author': b.author.name if b.author else None,
            'publisher': b.publisher.name if b.publisher else None
        })
    return jsonify(result)

@book_api.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': '图书不存在'}), 404
    return jsonify({'id': book.id, 'title': book.title})

@book_api.route('/', methods=['POST'])
def add_book():
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': '缺少 title 字段'}), 400
    new_book = Book(
        title=data['title'],
        author_id=data.get('author_id'),
        publisher_id=data.get('publisher_id')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id, 'title': new_book.title}), 201

@book_api.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': '图书不存在'}), 404
    data = request.json
    if 'title' in data:
        book.title = data['title']
    if 'author_id' in data:
        book.author_id = data['author_id']
    if 'publisher_id' in data:
        book.publisher_id = data['publisher_id']
    db.session.commit()
    return jsonify({'id': book.id, 'title': book.title})

@book_api.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error': '图书不存在'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': '删除成功'})