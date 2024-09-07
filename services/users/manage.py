
from project import app
from flask.cli import FlaskGroup
#entonces
cli=FlaskGroup(app)

if __name__=="__main__":
    cli()