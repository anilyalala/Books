from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SECRET_KEY" 

db = SQLAlchemy(app)


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    books = db.relationship('Books', backref='authorbr')


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(100), unique=True)
    authors_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)


class AuthorForm(FlaskForm):
    first_name = StringField("First Name: ")
    last_name = StringField("Last Name: ")
    submit = SubmitField("Submit")

class BookForm(FlaskForm):
    book_title = StringField("Book Title: ")
    author = SelectField("Author", choices=[])
    submit = SubmitField("Submit")



@app.route('/')
def homePage():
    list_of_authors = Authors.query.all()
    list_of_books = Books.query.all()
    
    return render_template('index.html', list1=list_of_authors, list2=list_of_books)



#@app.route('/home')
#def home():
#    list _of_books = Books.query.all()

#    return render_template('index.html', list2=list_of_books)

@app.route('/create/<f_name>/<l_name>')
def createAuthor(f_name, l_name):
    new_entry = Authors(first_name=f_name, last_name=l_name)
    db.session.add(new_entry)
    db.session.commit()
    return render_template('index.html')


@app.route('/create/<b_name>')
def createBook(b_name):
    new_entry = Books(book_title=b_name)
    db.session.add(new_entry)
    db.session.commit()
    return render_template('index.html')



@app.route('/add-author', methods=["GET", "POST"])
def add_author():
    form = AuthorForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            new_entry = Authors(first_name=form.first_name.data, last_name=form.last_name.data)
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('homePage'))

    return render_template('add_author.html', form=form)



@app.route('/add-book', methods=["GET", "POST"])
def add_book():
    form = BookForm()

    authors = Authors.query.all()
    
    for author in authors:
        form.author.choices.append(
            (author.id, f"{author.first_name} {author.last_name}")
        )
        
    if request.method == 'POST':
        if form.validate_on_submit():
            new_entry = Books(book_title=form.book_title.data, authors_id=form.author.data)
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('homePage'))

    return render_template('add_book.html', form=form)


@app.route('/update/<int:id>', methods=["GET", "POST"])
def updateAuthor(id):
    form = AuthorForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            updated_item = Authors.query.get(id)
            updated_item.first_name = form.first_name.data
            updated_item.last_name = form.last_name.data
            db.session.commit()
            return redirect(url_for("homePage"))

    return render_template('add_author.html', form=form)


@app.route('/update/<int:id>', methods=["GET", "POST"])
def updateBook(id):
    form = BookForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            updated_item = Books.query.get(id)
            updated_item.book_title = form.book_title.data
            db.session.commit()
            return redirect(url_for("homePage"))

    return render_template('add_author.html', form=form)


@app.route('/deleteauthor/<int:id>', methods=["GET"])
def deleteAuthor(id):
        
    deleted_item = Authors.query.get(id)
    db.session.delete(deleted_item)
    db.session.commit()
    return redirect(url_for("homePage"))


@app.route('/deletebook/<int:id>', methods=["GET"])
def deleteBook(id):
    
    deleted_item = Books.query.get(id)
    db.session.delete(deleted_item)
    db.session.commit()
    return redirect(url_for("homePage"))

    

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)