from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from sqlalchemy.sql import text

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_user_db'
app.config['SECRET_KEY'] = 'Sunniva2023'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_all_users():
    """Render all the users for homepage"""
    users= User.query.all()
    return render_template('users.html', users=users)

@app.route('/add_user', methods=['GET'])
def show_users_form():
   """Show add user form"""
   return render_template('/add_user.html')
    
@app.route('/add_user', methods=['POST'])
def add_new_user():
     """Add new users to User table"""
     first_name = request.form['first_name']
     last_name = request.form['last_name']
     image_url = request.form['image_url']
     new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
     db.session.add(new_user)
     db.session.commit()

     return redirect(f"/{new_user.id}")

@app.route('/<int:user_id>')
def show_user(user_id):
    """Show User details"""
    user = User.query.get_or_404(user_id)
    return render_template('/details.html', user=user)

@app.route('/edit', methods=['POST'])
def save_edited_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    saved_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(saved_user)
    db.session.commit()

    return redirect("/")
    
@app.route('/edit', methods=['GET'])
def show_edit_page():
    """Renders the edit form"""
    
    return render_template('/edit.html')



