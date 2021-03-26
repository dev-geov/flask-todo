from flask import (
    Blueprint, 
    render_template, 
    request, 
    redirect, 
    url_for,
)

from flask_login import(
    login_required,
    current_user,
)

from .models import Todo
from . import db

todo = Blueprint('todo', __name__)


@todo.route('/add/', methods=["POST"])
@login_required
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("main.home"))


@todo.route('/update/<int:todo_id>/')
@login_required
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("main.home"))


@todo.route("/edit/<int:todo_id>/", methods=["POST"])
@login_required
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    title = request.form.get('title')
    todo.title = title
    db.session.commit()
    return redirect(url_for("main.home"))


@todo.route("/delete/<int:todo_id>/", methods=["POST"])
@login_required
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("main.home"))