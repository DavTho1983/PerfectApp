from flask import Flask, render_template, request
from perfect_numbers import classify, listInRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecretKey'

num = 1
start = 1
end = 1
aliquot = 'perfect'
Classify = classify(num)
ListInRange = listInRange(start, end, aliquot)


@app.route('/')
def index():
    return render_template('index.html', num = num, start = start, end = end, aliquot = 1, classify = Classify, listInRange = ListInRange)

@app.route('/send', methods=['POST'])
def send():

    if request.method == 'POST':

        num = request.form['num']
        try:
            Classify = classify(int(num))
            return render_template('index.html', num = num, classify = Classify)
        except:
            return render_template('index.html', num = num, classify = 'not an integer')

@app.route('/aliRange', methods=['GET', 'POST'])
def aliKind():

    aliquot = request.form.get['aliquot']
    return aliquot

def aliRange():

    if request.method == 'POST':

        start = request.form['start']
        end = request.form['end']
        aliquot = request.form.get['aliquot']
    
        try:
            ListInRange = listInRange(int(start), int(end), aliquot)
            return render_template('index.html', start = start, end = end, aliquot = aliquot, listInRange = ListInRange)
        except:
            return render_template('index.html', start = start, end = end, aliquot = aliquot, listInRange = 'are not integers')


if __name__ == '__main__':
    app.run(debug=True)
