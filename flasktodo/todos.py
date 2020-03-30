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
            cur.execute(
                'INSERT INTO todos (description, completed,created_at) VALUES (%s,%s,%s)',
                (task, False, datetime.datetime.now())
            )
            g.db.commit()

        flash(error)

    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)
