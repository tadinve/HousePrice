# kiankai
from flask import Flask, render_template, request, url_for, flash, redirect
import pickle
import sklearn

app = Flask(__name__)
infile = open('model.pickle', 'rb')
model = pickle.load(infile, encoding='latin1')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sqrFeet = request.form.get('SquareFeet')
        size = request.form.get('size')
        bed = request.form.get('bed')
        bath = request.form.get('bath')
        floors = request.form.get('floors')
        l = [bed, bath, sqrFeet, size, floors]
        l = list(map(int, l))
        price = '${:,.2f}'.format(model.predict([l])[0])
        #price = sum(l)
        return render_template("home.html", price=price, sqrFeet=sqrFeet, size=size, bed=bed, bath=bath, floors=floors)
    sqrFeet = 0
    size = 0
    bed = 0
    bath = 0
    floors = 0
    return render_template("home.html", sqrFeet=sqrFeet, size=size, bed=bed, bath=bath, floors=floors)


if __name__ == '__main__':
    app.run(debug=True)
