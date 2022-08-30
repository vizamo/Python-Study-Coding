import yaml
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
try:
    opened_from = 'remote'
    db = yaml.load(open('/app/src/db.yaml'))
    localdb_file = '/app/src/local_db.txt'
    app.config['MYSQL_HOST'] = db['mysql_host']
    app.config['MYSQL_USER'] = db['mysql_user']
    app.config['MYSQL_PASSWORD'] = db['mysql_password']
    app.config['MYSQL_DB'] = db['mysql_db']
except FileNotFoundError:
    opened_from = 'local'
    localdb_file = 'local_db.txt'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'vitali'
    app.config['MYSQL_PASSWORD'] = 'Localdb21'
    app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_details = request.form
        name = user_details['name']
        email = user_details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        if opened_from == 'local':
            data_migration(opened_from + "post", name, email)
        return redirect('/users')
    return render_template('index.html')


@app.route('/users')
def users():
    data_migration(opened_from)
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM users")
    if result_value > 0:
        user_details = cur.fetchall()
        print(render_template('users.html', user_details=user_details))
        return render_template('users.html', user_details=user_details)


def data_migration(o_from, name="", email=""):
    if o_from == 'localpost':
        with open(localdb_file, 'a') as db_file:
            db_file.write(f"{name}, {email}\n")
    elif o_from == 'remote':
        with open(localdb_file, 'r') as db_file:
            for line in db_file:
                cur = mysql.connection.cursor()
                name, email = line.strip().split(', ')
                cur.execute("SELECT * FROM users WHERE name = %s and email = %s", (name, email))
                d = cur.fetchall()
                if len(d) == 0:
                    cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
                    mysql.connection.commit()
                    cur.close()


if __name__ == '__main__':
    app.run(debug=True)
