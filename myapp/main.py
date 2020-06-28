from flask import (
    Blueprint,
    render_template,
)

from .models import Todo
from . import db, create_app

main = Blueprint('main', __name__)


@main.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template('home/index.html', todo_list=todo_list)


    