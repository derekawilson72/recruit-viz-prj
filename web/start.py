import sys
import sqlite3

from flask import Flask, jsonify
from flask import render_template
from flask import Response
app = Flask(__name__)

DATABASE = "../recruit.db"

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def query_db(query):

    result_dict = {}

    try:
        connection = sqlite3.connect(DATABASE)

        cursor = connection.cursor()
        cursor.execute(query)
        result_dict = dictfetchall(cursor)

    except sqlite3.OperationalError as e:
        print("Db operation error", e)
        result_dict["error"] = str(e)
    except:
        e = sys.exc_info()[0]
        print("An error occurred with the database", e)
        result_dict["error"] = str(e)
    else:
        cursor.close()
        connection.close()

    return result_dict


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scattermatrix')
def scatterMatrix():
    return render_template('scatterMatrix.html')


@app.route('/api/max_income', methods=['GET'])
def api_test():

    result_dict = query_db("select gender, max(income) as max_income from customer group by gender")
    # print(result_dict)

    return jsonify({'data': result_dict})

@app.route('/api/scatterMatrixData', methods=['GET'])
def scatterMatrixData():
    
    xml = """species,sepal length,sepal width,petal length,petal width,gender
setosa,5.1,3.5,1.4,0.2,1
setosa,4.9,3,1.4,0.2,1
setosa,4.7,3.2,1.3,0.2,0
versicolor,7,3.2,4.7,1.4,1
versicolor,6.4,3.2,4.5,1.5,1
versicolor,6.9,3.1,4.9,1.5,0
virginica,6.5,3,5.2,2,0
virginica,6.2,3.4,5.4,2.3,0
virginica,5.9,3,5.1,1.8,0
"""
    qry="select gender, education_id,economic_stability,is_exerciser,income  from customer limit 1000;"
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(qry)
    result_dict = dictfetchall(cursor)
    
    resp = jsonify({"data":result_dict})
    #resp=Response(xml, mimetype='text/csv')
    return resp

    





if __name__ == '__main__':
    app.run()
