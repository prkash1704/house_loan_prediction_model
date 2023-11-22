import pickle5 as pickle
from flask import Flask, render_template, request

app = Flask(__name__)

df = pickle.load(open("models/housepredt.pkl","rb"))

@app.route('/', methods=['GET'])
def home():
    price=''
    if request.args.get('Population') and request.args.get('Income') and request.args.get('Age') and request.args.get('Rooms'):
        query = request.args.get('Population')
        Population = eval(query)

        query = request.args.get('Income')
        Income = eval(query)

        query = request.args.get('Age')
        Age = eval(query)

        query = request.args.get('Rooms')
        Rooms = eval(query)

        Predt = [[Population,Income,Age,Rooms]]

        price = df.predict(Predt)
        price = str(price[0])

    return render_template('index.html',res=price)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
