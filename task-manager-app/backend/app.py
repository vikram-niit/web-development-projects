from flask import Flask
from flask_cors import CORS
from routes.task_routes import task_bp
import config

app = Flask(__name__)
CORS(app)

app.register_blueprint(task_bp, url_prefix='/api/tasks')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
