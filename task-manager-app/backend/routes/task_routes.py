from flask import Blueprint
from controllers import task_controller

task_bp = Blueprint('tasks', __name__)

task_bp.route('/', methods=['GET'])(task_controller.get_tasks)
task_bp.route('/', methods=['POST'])(task_controller.create_task)
task_bp.route('/<task_id>', methods=['DELETE'])(task_controller.delete_task)
