from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    fake_blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(fake_blog_url)
    all_posts = response.json()
    # blog_id = response.json()['id']
    return render_template("index.html",
                           posts=all_posts)


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    post = Post(blog_id)
    post.make_post(blog_id)
    return render_template('post.html',
                           post=post)


if __name__ == "__main__":
    app.run(debug=True)
