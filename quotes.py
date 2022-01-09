from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
#import os
#import re

app = Flask(__name__)

#uri = os.getenv('HEROKU_POSTGRESQL_BROWN_URL')  # or other relevant config var
#if uri.startswith('postgres://'):
#uri = uri.replace('postgres://', 'postgresql://', 1)




#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Kcjewel19@13.40.193.121/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://gchkbtwvwcxhtk:24dcb28361c6b1d48156ed6e9af1d30db8a2ac16204a9e41e184a5278450aa96@ec2-63-32-7-190.eu-west-1.compute.amazonaws.com:5432/dd0rfd2617vti2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db =SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
