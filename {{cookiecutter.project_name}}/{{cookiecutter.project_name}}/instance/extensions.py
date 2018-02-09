"""Register flask extensions here."""
import flask_sqlalchemy
import flask_migrate

from .db import Base

db = flask_sqlalchemy.SQLAlchemy(model_class=Base)

def register_extensions(app):
    # Add flask sqlalchemy
    db.init_app(app)

    # SQLAlchemy Migration Facility
    migrate = flask_migrate.Migrate(app, db)
