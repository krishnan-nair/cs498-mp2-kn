from site import venv
from flask import Flask, request, render_template

app = Flask(__name__)
#seed = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    seed = 0
    if request.method == "POST":
        input = request.form['newNum']
        if input != '':
            seed = input
        

    data = {'num': str(seed)}   

    return render_template('home.html', data=data)


# Always last line of code
if __name__ == '__main__':
    app.run(debug=True)