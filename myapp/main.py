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
    print(qs)
    todo_list = None
    if qs == 'on':
        todo_list = current_user.todos().filter_by(complete=True)
    elif qs == 'off':
        todo_list = current_user.todos().filter_by(complete=False)
    else:
        todo_list = current_user.todos()
    
    todo_count = todo_list.count()
    return render_template(
        'home/index.html', 
        todo_list=todo_list,
        name=current_user.name,
        todo_count=todo_count,
    )
