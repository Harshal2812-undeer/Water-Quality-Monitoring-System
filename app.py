from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Setup Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

def train_model_and_save(data_file, model_file):
    # Load the dataset
    data = pd.read_csv(data_file)

    # Convert 'Water Type' to binary labels
    data['Water Type'] = data['Water Type'].map({'Impure': 0, 'Pure': 1})

    # Split features and target variable
    X = data.drop(columns=['Water Type'])
    y = data['Water Type']

    # Split the data into training and testing sets
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Random Forest Classifier
    clf = RandomForestClassifier()

    # Train the classifier
    clf.fit(X_train, y_train)

    # Save the trained model
    with open(model_file, 'wb') as file:
        pickle.dump(clf, file)

def predict_water_purity(model_file, pH, turbidity, temperature):
    # Load the trained model
    with open(model_file, 'rb') as file:
        clf = pickle.load(file)

    # Make prediction
    prediction = clf.predict([[pH, turbidity, temperature]])

    # Return the result
    return "Pure" if prediction[0] == 1 else "Impure"

@app.route('/')
def index():
    if 'email' not in session:
        return redirect('/login')
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    pH = float(request.form['pH'])
    turbidity = float(request.form['turbidity'])
    temperature = float(request.form['temperature'])

    result = predict_water_purity("water_purity_model.pkl", pH, turbidity, temperature)
    return render_template('index.html', prediction1=result)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/')  # Redirect to home page after successful login
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')

if __name__=="__main__":
    train_model_and_save("wqms_dataset.csv", "water_purity_model.pkl")
    app.run(debug=True)
