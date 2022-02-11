from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'marleymariecornbread'


@app.route('/')
def index():
    if 'userVisits' not in session:
        session['userVisits'] = 1
    else:
        session['userVisits'] += 1
    return render_template('index.html')



@app.route('/destroy_session')
def destroy():
    if 'userVisits' in session:
        session.clear()
    return render_template('index.html')


@app.route('/count_two')
def countTwo():
    if 'userVisits' not in session:
        session['userVisits'] = 1
    else:
        session['userVisits'] += 2
    return render_template('index.html')


if __name__=="__main__":
        app.run(debug=True)
