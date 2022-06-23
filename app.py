
from hashlib import new
from urllib import response
import psycopg2
from flask import Flask, render_template, request, jsonify, url_for, redirect, make_response
from psycopg2 import connect, extras
from flask_qrcode import QRcode
from reportlab.pdfgen import canvas
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
import openpyxl
import csv
from io import StringIO
import datetime
import time


app = Flask(__name__, static_folder='static', template_folder='templates')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


qrcode = QRcode(app)


database = ''
host = ''
user = ''
password = ''
port = '5432'


def get_connect():
    try:
        conn = connect(
            "dbname=dbname host=host user=user password=paassword port=5432")
        print('connected')
        return conn
    except:
        print('no connected')


@app.route('/')
def index():
    """con = get_connect()
    cur = con.cursor(cursor_factory=extras.DictCursor)
    cur.execute("CREATE TABLE regEm(id serial PRIMARY KEY, matricula varchar(255) not null, name varchar(255) not null, adscription varchar(255) not null, category varchar(255) not null, nafil varchar(255) not null, cellnumber varchar(255) not null, address varchar(255) not null, created_at timestamp default current_timestamp)");
    con.commit()
    cur.close()
    con.close()
    print(con)"""
    return render_template('index.html')


@app.route('/registro', methods=['GET', 'POST'])
# @app.post('/registro')
def registro():
    error = None
    message = None
    if request.method == 'POST':
        #new_register = request.get_json()
        #matricula = new_register['matricula']
        # print(matricula)
        matricula = request.form['matricula']
        name = request.form['name']
        adscription = request.form['adscription']
        category = request.form['category']
        nafil = request.form['nafil']
        cellnumber = request.form['cellnumber']
        address = request.form['address']
        #allergies = request.form['allergies']
        if not matricula and not name and not adscription and not category and not nafil and not cellnumber and not address:
            error = 'Hay campos vacíos, favor de verificar...'
            print(error)
        else:
            try:
                con = get_connect()
                cur = con.cursor(cursor_factory=extras.DictCursor)
                cur.execute("INSERT INTO regEm(matricula, name, adscription, category, nafil, cellnumber, address) VALUES(%s, %s, %s, %s, %s, %s, %s);",
                            (matricula, name.upper(), adscription.upper(), category.upper(), nafil, cellnumber, address.upper()))
                con.commit()
                cur.close()
                con.close()
                message = 'Registro exitoso'
                # print("Success")
            except:
                print("Not success")
        return redirect(url_for('listado'))
        # return render_template('registro.html', error=error, message=message)

    return render_template('registro.html', error=error, message=message)
    # return jsonify({'msg': 'Success'})


@app.route('/listado', methods=['GET'])
def listado():
    con = get_connect()
    cur = con.cursor(cursor_factory=extras.DictCursor)
    cur.execute("SELECT * FROM regem;")
    ctx = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return render_template('listado.html', ctx=ctx)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    try:
        con = get_connect()
        cur = con.cursor()
        cur.execute("DELETE FROM regem WHERE id = %s", (id,))
        con.commit()
        cur.close()
        con.close()

        print("Registro borrado")

    except:
        print("no se pudo borrar")
    return redirect(url_for('listado'))



def validate_date(d):
    date1 = datetime.datetime.strptime(d, "%Y-%m-%d")
    #print(date1)
    #print(type(date1))
    #date1m = datetime.datetime(date1)
    #print(date1m)
    date2 = datetime.datetime(2008,7,25)
    #print(type(date2))
    #print(date2)
    date3 = datetime.datetime(2016,7,25)
    if date1 < date2 or date1 > date3:
        print("fuera de rango")
        return True
    #print("%s, %s ,%s", date1, date2, date3)





@app.route('/registroH/<int:id>', methods=['GET', 'POST'])
def registroH(id):
    error = None
    if request.method == 'GET':
        return render_template('registroH.html')
    elif request.method == 'POST':
        name = request.form['name']
        bdate = request.form['bdate']
        print(validate_date(bdate))
        if validate_date(bdate) == True:
            error = "Fecha fuera de Rango"
            return render_template('errors.html', error=error)
            #return redirect(url_for('listado'))
        print(bdate)

        tblood = request.form['tblood']
        allergies = request.form['allergies']

        con = get_connect()
        cur = con.cursor(cursor_factory=extras.DictCursor)
        cur.execute("INSERT INTO regben(regem_id, name, bdate, tblood, allergies) VALUES(%s, %s, %s, %s, %s);",
                    (id, name.upper(), bdate, tblood.upper(), allergies.upper()))
        con.commit()
        cur.close()
        con.close()
        return redirect(url_for('listadoH'))
        #return render_template('registroH.html')


@app.route('/listadoH', methods=['GET'])
def listadoH():
    title = 'Liastado Registro Hijos'
    con = get_connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM regben;")
    ctx = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return render_template('listadoH.html', ctx=ctx, title=title)


@app.route('/deleteH/<int:id>', methods=['GET', 'POST'])
def deleteH(id):
    if request.method == 'POST':
        con = get_connect()
        cur = con.cursor()
        cur.execute('DELETE FROM regben WHERE id = %s', (id,))
        con.commit()
        cur.close()
        con.close()
    return redirect(url_for('listadoH'))


@app.route('/qrcode/<int:id>', methods=['GET', 'POST'])
def qrcode(id):
    con = get_connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM regem INNER JOIN regben ON regem.id = regben.regem_id;")
    ctx = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    #pdf = canvas.Canvas('vale.pdf')
    #pdf.setFont("Helvetica", 12)
    #pdf.drawString(50, 20, "hola")
    # pdf.save()
    # print(ctx)
    return render_template('vale.html', ctx=ctx)


@app.route('/export_excel', methods=['GET', 'POST'])
def export_excel():
    si = StringIO()
    cw = csv.writer(si)
    con = get_connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM regben;")
    rows = cur.fetchall()
    cw.writerow([i[0] for i in rows])
    cw.writerows(rows)
    response = make_response(si.getvalue())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'inline; filename=reporteHijos.csv'
    return response


if __name__ == '__main__':
    app.run(debug=True)
