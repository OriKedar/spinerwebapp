from flask import Flask, render_template, url_for, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from random import random, randint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
db = SQLAlchemy(app)

class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Record %r>' % self.id

@app.route('/Home', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        record_name = request.form['content']
        artist_name = request.form['artist']
        new_record = Records(content=record_name, artist=artist_name) 
      

        try:
            db.session.add(new_record)
            db.session.commit()
            return redirect('/Home')
        except:
            return 'There was an isseu adding the new record'

    else:
        records = Records.query.order_by(Records.artist).all()
        return render_template('index.html', records=records)


@app.route('/delete/<int:id>')
def delete(id):
    record_to_delete = Records.query.get_or_404(id)

    try:
        db.session.delete(record_to_delete)
        db.session.commit()
        return redirect('/Home')
    except:
        return 'There was a problem deleting that record'

@app.route('/update/<int:id>' , methods=['GET', 'POST'])
def update(id):
    record = Records.query.get_or_404(id)

    if request.method == 'POST':
        record.content = request.form['content']
        record.artist = request.form['artist']

        try:
            db.session.commit()
            return redirect('/Home')
        except:
            return 'There was ana issue updatinig your record'
    else:
        return render_template('update.html', record=record)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'OriKedar' or request.form['password'] != 'records':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)