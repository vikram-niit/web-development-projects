from flask import jsonify, request
from models.task_model import Task

def get_tasks():
    tasks = Task.get_all()
    for t in tasks:
        t['_id'] = str(t['_id'])
    return jsonify(tasks)

def create_task():
    data = request.get_json()
    if not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    task_id = Task.create({'title': data['title'], 'completed': False})
    return jsonify({'_id': str(task_id), 'title': data['title'], 'completed': False}), 201

def delete_task(task_id):
    Task.delete(task_id)
    return jsonify({'message': 'Task deleted'})
