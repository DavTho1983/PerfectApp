from flask import Flask, render_template, request
from perfect_numbers import classify, listInRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecretKey'

num = 1
start = 1
end = 1
aliquot = 'abundant'
Classify = classify(num)
ListInRange = listInRange(start, end, aliquot)


@app.route('/')
def index():
    return render_template('index.html', num = num, start = start, end = end, aliquot = aliquot, classify = Classify, listInRange = ListInRange)

@app.route('/send', methods=['POST'])
def send():

    if request.method == 'POST':

        num = request.form['num']
        try:
            Classify = classify(int(num))
            return render_template('index.html', num = num, classify = Classify)
        except:
            return render_template('index.html', num = num, classify = 'not an integer')

@app.route('/aliRange', methods=['POST'])
def aliRange():

    if request.method == 'POST':

        start = request.form['start']
        end = request.form['end']
        aliquot = request.form['aliquot']

        try:
            ListInRange = listInRange(int(start), int(end), aliquot)
            return render_template('index.html', num = num, classify = Classify, start = start, end = end, aliquot = aliquot, listInRange = ListInRange)
        except:
            return render_template('index.html', num = num, classify = Classify, start = start, end = end, aliquot = aliquot, listInRange = 'not all integers')


if __name__ == '__main__':
    app.run(debug=True)
