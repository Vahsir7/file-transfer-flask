from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['UPLOAD_FOLDER'] = 'application/static/uploads'

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Files

    with app.app_context():
        db.create_all()
    
    from .controller import main_bp
    app.register_blueprint(main_bp)

    return app
