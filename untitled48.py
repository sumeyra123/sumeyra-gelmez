# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:34:25 2023

@author: Sümeyra Nihal GELMEZ
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
db = SQLAlchemy(app)
class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), unique=True, nullable=False)
    today = db.Column(db.String(80), nullable=False)
    tomorrow = db.Column(db.String(80), nullable=False)
    day_after_tomorrow = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return '<Weather %r>' % self.city
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather = Weather.query.filter_by(city=city).first()
        if weather is None:
            weather = Weather(city=city, today='-', tomorrow='-', day_after_tomorrow='-')
            db.session.add(weather)
            db.session.commit()
        return redirect(url_for('index'))
    else:
        weather = Weather.query.all()
        return render_template('index.html', weather=weather)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_confirmation = request.form['password_confirmation']
        nickname = request.form['nickname']
        if password != password_confirmation:
            return redirect(url_for('register'))
        user = User(username=username, password=password, nickname=nickname)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('register.

);                             