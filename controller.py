#kiankai
from flask import Flask, render_template, request, url_for, flash, redirect
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        infile = open('model.pickle','rb')
        model = pickle.load(infile,encoding='latin1')
        
        sqrFeet= request.form.get('SquareFeet')
        size=  request.form.get('size')
        bed =   request.form.get('bed')
        bath =   request.form.get('bath')
        floors = request.form.get('floors')
        l = [sqrFeet,size,bed,bath,floors]
        price = model.predict([l])[0]
        return render_template("home.html",price=price,sqrFeet=sqrFeet,size=size,bed=bed,bath=bath,floors=floors)
    sqrFeet= 0
    size=  0
    bed =  0
    bath =  0
    floors = 0
    return render_template("home.html",sqrFeet=sqrFeet,size=size,bed=bed,bath=bath,floors=floors)


import pickle
import sklearn


if __name__ == '__main__':
    infile = open('model.pickle','rb')
    model = pickle.load(infile,encoding='latin1')
    app.run(debug=True)
