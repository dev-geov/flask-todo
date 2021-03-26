from flask import (
    Blueprint,
    render_template,
    request
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
    qs = request.args.get('status')

    todo_list = None
    if qs == 'on':
        todo_list = Todo.query.filter_by(complete=True, user_id=current_user.id)
    elif qs == 'off':
        todo_list = Todo.query.filter_by(complete=False, user_id=current_user.id)
    else:
        todo_list = Todo.query.filter_by(user_id=current_user.id)
    
    todo_count = todo_list.count()
    return render_template(
        'home/index.html', 
        todo_list=todo_list,
        name=current_user.name,
        todo_count=todo_count,
    )
