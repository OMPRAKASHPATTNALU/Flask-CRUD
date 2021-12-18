from flask import Flask,render_template, url_for, redirect, flash, jsonify, request
from project_flask import app, db
from project_flask.forms import RegistrationForm, LoginForm, SearchForm, EditForm
from project_flask.models import User,  Data
from sqlalchemy import and_
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/Registration', methods=['GET', 'POST'])
def registration():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("Registration.html",form=form)    

@app.route('/Login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user:
            if form.email.data==user.email and form.password.data==user.password:
                return redirect(url_for('search'))
        else:
            flash('Login Credential doesnt exist,Please Signup',category='error')
            return redirect(url_for('registration')) 
    return render_template("login.html",form=form)    

@app.route('/Search', methods=['GET', 'POST'])
def search():
    form=SearchForm()
    Editform=EditForm()
    all=Data.query.all()
    if form.validate_on_submit():
        d=Data.query.filter_by(name=form.name.data).\
            filter_by(subject=form.subject.data).first()    
        if d:
            if form.name.data==d.name and form.subject.data==d.subject:
                print(d)
                k=Data.query.filter_by(id=d.id).first()
                k.marks=form.mark.data
                #data=Data(name=form.name.data,subject=form.subject.data,marks=form.mark.data)
                db.session.commit()
                return redirect(url_for('search'))  
        else:        
            data=Data(name=form.name.data,subject=form.subject.data,marks=form.mark.data)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('search'))
    return render_template("search.html",form=form,Editform=Editform,all=all)    

@app.route('/Delete/<int:sid>', methods=['GET', 'POST'])
def delete(sid):
    stud= Data.query.filter_by(id=sid).first()
    if stud:
        db.session.delete(stud)
        db.session.commit()
    return redirect(url_for('search'))    

@app.route('/Edit/<int:eid>', methods=['GET', 'POST'])
def edit(eid):
    Editform=EditForm()   
    if request.method == 'GET':
        k=Data.query.filter_by(id=eid).first()
        print(k)
    return jsonify(username=k.name,
                email=k.subject,
                id=k.marks)      
    if request.method == 'POST':   
        return'Hello'            

@app.route('/Update', methods=['GET', 'POST'])
def update():
    Editform=EditForm()  
    if Editform.validate_on_submit():
        #print(Editform.id.data)
        d=Data.query.filter_by(id=Editform.id.data).first()    
        if d:
            if Editform.name.data==d.name and Editform.subject.data==d.subject:
                k=Data.query.filter_by(id=d.id).first()
                k.marks=Editform.mark.data
                #data=Data(name=form.name.data,subject=form.subject.data,marks=form.mark.data)
                db.session.commit()
    return redirect(url_for('search'))  
