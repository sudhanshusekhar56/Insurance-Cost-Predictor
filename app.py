from flask import Flask, render_template, request, redirect
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


data = []


@app.route('/pred', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        address = open('model.pkl', 'rb')
        model = pickle.load(address)

        gender = int(request.form['gender'])
        smoker = int(request.form['smoker'])
        region = str(request.form['region'])
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])

        if region == 'ne':
            ne = 1
            nw = 0
            se = 0
            sw = 0
        elif region == 'nw':
            ne = 0
            nw = 1
            se = 0
            sw = 0
        elif region == 'se':
            ne = 0
            nw = 0
            se = 1
            sw = 0
        else:
            ne = 0
            nw = 0
            se = 0
            sw = 1

        data = [[gender, smoker, ne, nw, se, sw, age, bmi]]
        print(data)
        result = model.predict(data)

        final = round(result[0], 2)
        output = "The average cost for your insurance will be around Rs. " + \
            str(final)+"."
        return render_template('home.html', res=output)


if __name__ == "__main__":
    app.run(debug=True)
