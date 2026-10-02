import requests


class Post:
    def __init__(self, id):
        self.id = id
        self.title = None
        self.subtitle = None
        self.body = None

    def make_post(self, id):
        fake_blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
        response = requests.get(url=fake_blog_url)
        print(response.json())
        for post in response.json():
            if post['id'] == self.id:
                self.title = post['title']
                self.subtitle = post['subtitle']
                self.body = post['body']
        return
