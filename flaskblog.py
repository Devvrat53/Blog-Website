from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Devvrat Mungekar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 24, 2020'
    },
    {
        'author': 'Himani Joshi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 23, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    #return "<h1>Home Page</h1>"
    return render_template('home.html', posts= posts)

@app.route("/about")
def about():
    #return "<h1>About Page</h1>"
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug = True)