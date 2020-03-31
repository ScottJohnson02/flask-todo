from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from . import db
import datetime


bp = Blueprint("todos", __name__)


@bp.route("/", methods=('GET', 'POST'))
def index():
    """View for home page which shows list of to-do items."""
    cur = db.get_db().cursor()

    if request.method == 'POST':
        task = request.form['task']
        error = None

        if not task:
            error = 'Task is required.'

        if error is None:
            # insets the user input into the database
            cur.execute(
                'INSERT INTO todos (description, completed,created_at) VALUES (%s,%s,%s)',
                (task, False, datetime.datetime.now())
            )
            g.db.commit()

    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)


@bp.route("/completed", methods=['GET', 'POST'])
def completed():

    cur = db.get_db().cursor()
    if request.method == 'POST':
        task = request.form['task']
        error = None

        if not task:
            error = 'Task is required.'

        if error is None:
            # insets the user input into the database
            cur.execute(
                'INSERT INTO todos (description, completed,created_at) VALUES (%s,%s,%s)',
                (task, False, datetime.datetime.now())
            )
            g.db.commit()

    cur.execute('SELECT * FROM todos WHERE completed = True')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)


@bp.route("/uncompleted", methods=['GET', 'POST'])
def uncompleted():

    cur = db.get_db().cursor()
    if request.method == 'POST':
        task = request.form['task']
        error = None

        if not task:
            error = 'Task is required.'

        if error is None:
            # insets the user input into the database
            cur.execute(
                'INSERT INTO todos (description, completed,created_at) VALUES (%s,%s,%s)',
                (task, False, datetime.datetime.now())
            )
            g.db.commit()

    cur.execute('SELECT * FROM todos WHERE completed = False')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)


@bp.route("/<int:id>/done", methods=('POST',))
def done(id):
    """Sets the task to completed"""
    cur = db.get_db().cursor()

    # update the task and set it to complete
    cur.execute(
        'UPDATE todos SET completed = True'
        ' WHERE id= %s ',
        (id,)
    )
    g.db.commit()

    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()

    return redirect(url_for('todos.index'))


@bp.route("/<int:id>/delete", methods=('POST',))
def delete(id):
    """Sets the task to delete"""
    cur = db.get_db().cursor()

    # delete the task
    cur.execute(
        'DELETE FROM todos WHERE id= %s', (id,)
    )
    g.db.commit()
    cur.close()
    return redirect(url_for('todos.index'))


@bp.route("/<int:id>/edit", methods=('GET', 'POST',))
def edit(id):
    """Edits the description of the task"""
    cur = db.get_db().cursor()
    if request.method == "POST":
        new = request.form['new']

        if not new:

            return render_template(edit.html)
            # update the task and set it to complete
        else:
            cur.execute(
                'UPDATE todos SET description = %s'
                ' WHERE id = %s ',
                (new, id)
            )
            g.db.commit()
            cur.close()

        return redirect(url_for('todos.index'))
    return render_template("edit.html")
