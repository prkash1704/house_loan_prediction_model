from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("/workspaces/house_loan_prediction_model/housepredt.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html', res='')

@app.route('/', methods=['POST'])
def predict():
    price = ''
    if request.form.get('Population') and request.form.get('Income') and request.form.get('Age') and request.form.get('Rooms'):
        Population = float(request.form['Population'])
        Income = float(request.form['Income'])
        Age = float(request.form['Age'])
        Rooms = float(request.form['Rooms'])

        Predt = [[Population, Income, Age, Rooms]]

        price = str(model.predict(Predt)[0])

    return render_template('index.html', res=price)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
