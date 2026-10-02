from flask import Flask, render_template
import random
import time
import requests

app = Flask(__name__)

gender_api_url = 'https://api.genderize.io'
age_api_url = 'https://api.agify.io'


@app.route('/')
def hello_world():  # put application'templates code here
    return render_template('index.html')


@app.route('/guess/<name>')
def predict_gender(name):
    params = {
        "name": name
    }
    gender_response = requests.get(url=gender_api_url,
                                   params=params)
    age_response = requests.get(url=age_api_url,
                                params=params)
    gender = gender_response.json()['gender']
    prob = gender_response.json()['probability']
    age = age_response.json()['age']
    return render_template('templates/guess.html',
                           name=name,
                           gender=gender,
                           prob=prob,
                           age=age)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('templates/blog.html',
                           posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
