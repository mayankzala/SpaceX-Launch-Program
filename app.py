from flask import Flask, request, render_template, url_for, jsonify
import requests
import json
app = Flask(__name__)


@app.route('/')
def home():
    # data=r('https://api.spaceXdata.com/v3/launches?limit=100')
    data = requests.get(url='https://api.spaceXdata.com/v3/launches?limit=100')
    return render_template('index.html', data=data.json())



@app.route('/filter_by_year_<year>',methods=['POST','GET'])
def year_filter(year):
    data = requests.get(url=f'https://api.spaceXdata.com/v3/launches?limit=100&launch_year={year}')
    return jsonify(data.json())

@app.route('/filter_by_launch_<boolean>',methods=['POST','GET'])
def launch_filter(boolean):
    data = requests.get(url=f'https://api.spaceXdata.com/v3/launches?limit=100&launch_success={boolean}')
    return jsonify(data.json())
@app.route('/filter_by_land_<boolean>',methods=['POST','GET'])
def land_filter(boolean):
    data = requests.get(url=f'https://api.spacexdata.com/v3/launches?limit=100&launch_success=true&land_success={boolean}')
    return jsonify(data.json())

if __name__ == "__main__":
    app.run(debug=True)
