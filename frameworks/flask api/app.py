from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import TaskForm
from models import Task
from extensions import db
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
# app.config.from_object('config')

db.init_app(app)
# db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_task.html', form=form)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
