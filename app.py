import os

from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

app = Flask(__name__)


project_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SECRET_KEY"

db = SQLAlchemy(app)


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    books = db.relationship('Book', backref='authorbr')


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(100), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)


class AuthorForm(FlaskForm):
    first_name = StringField("First Name: ")
    last_name = StringField("Last Name: ")
    submit = SubmitField("Submit")


@app.route('/')
def homePage():
    list_of_authors = Authors.query.all()
    
    return render_template('index.html', list1=list_of_authors)


@app.route('/home')
def home():
    return render_template('index.html', names=["Laz", "Joe", "Smith"])

@app.route('/create/<f_name>/<l_name>')
def createEntry(f_name, l_name):
    new_entry = Authors(first_name=f_name, last_name=l_name)
    db.session.add(new_entry)
    db.session.commit()
    return render_template('index.html')




@app.route('/add-author', methods=["GET", "POST"])
def add_owner():
    form = AuthorForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            new_entry = Authors(first_name=form.first_name.data, last_name=form.last_name.data)
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('homePage'))

    return render_template('add_author.html', form=form)


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    form = AuthorForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            updated_item = Authors.query.get(id)
            updated_item.first_name = form.first_name.data
            updated_item.last_name = form.last_name.data
            db.session.commit()
            return redirect(url_for("homePage"))

    return render_template('add_author.html', form=form)


@app.route('/delete/<int:id>')
def delete(id):
    deleted_item = Authors.query.get(id)
    db.session.delete(deleted_item)
    db.session.commit()
    return redirect(url_for("homePage"))


@app.route('/about', methods=['GET', 'POST'])
def about():
    return "Info about the whole team"


@app.route('/about/dave')
def aboutDave():
    return "Info about dave"
    
@app.route('/about/steve')
def aboutSteve():
    return "Info about Steve"

@app.route('/goog')
def goog():
    return redirect('https://www.google.com')



if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
