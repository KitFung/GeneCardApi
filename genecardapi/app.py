from flask import Flask, jsonify
from config import DefaultConfig


__all__ = ['create_app']


def create_app(config=None, app_name=None):

    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name)

    configure_app(app, config)
    configure_blueprints(app)
    configure_errror_handlers(app)
    configure_cli(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)
    if config:
        app.config.from_object(config)


def configure_blueprints(app):
    from api import all_api
    for bp in all_api:
        app.register_blueprint(bp)


def configure_errror_handlers(app):
    # @app.errorhandler(204)
    # def error204(error):
    #     return jsonify(data=[]), 204
    pass


def configure_cli(app):
    pass



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

