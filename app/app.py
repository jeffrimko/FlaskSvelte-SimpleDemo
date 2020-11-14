##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from random import randint

from flask import Flask, render_template

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

app = Flask(__name__)

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/random')
def random():
    return f"{randint(1,100)}"

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=5000)
