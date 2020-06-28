from flask import (
    Blueprint,
    render_template,
)

from myapp.models import Todo
from . import db

from flask_login import(
    login_required,
    current_user,
)

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def home():
    db.create_all()
    todo_list = Todo.query.filter_by(user_id=current_user.id)
    todo_count = todo_list.count()
    return render_template(
        'home/index.html', 
        todo_list=todo_list,
        name=current_user.name,
        todo_count=todo_count,
    )
