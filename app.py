from distutils.log import debug
from flask import Flask, redirect, render_template, request, url_for
# from flask_mysqldb import MySQL
app = Flask(__name__)

#configure db
# app.config['MYSQL_HOST'] = ''
# app.config['MYSQL_USER'] = ''
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = ''

@app.route('/', methods=['GET', 'POST'])
def login1():
    # if request.method == 'POST':
        #fetch from data
        # userDetails = request.form
        # name =  userDetails['username']
        # password = userDetails['password']
    return render_template('login1.html')

@app.route('/admindashboard',methods=['GET', 'POST'])
def admindashboard():
    return render_template('admindashboard.html')

@app.route('/candidates',methods=['GET', 'POST'])
def candidates():
    return render_template('candidates.html')

@app.route('/exam',methods=['GET', 'POST'])
def exam():
    return render_template('exam.html')

@app.route('/prof',methods=['GET', 'POST'])
def prof():
    return render_template('prof.html')

@app.route('/resultadmin',methods=['GET', 'POST'])
def resultadmin():
    return render_template('resultadmin.html')

@app.route('/login_admin',methods=['GET', 'POST'])
def login():
    return render_template('login_admin.html')

@app.route('/login_candidate',methods=['GET', 'POST'])
def login_candi():
    return render_template('login_candidate.html')
if __name__ == "__main__":
    app.run(debug=True)