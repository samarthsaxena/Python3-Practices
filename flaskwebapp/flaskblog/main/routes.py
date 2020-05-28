from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint('main', __name__)


"""posts = [
    {
        "author": 'Samarth Saxena',
        'title': 'Blog Post 1',
        'content': 'First Post content.',
        'date_posted': '11/05/2019'
    },
    {
        'author': 'Alex Parish',
        'title': 'Blog Post 2',
        'content': 'Second Post content.',
        'date_posted': '12/05/2019'
    },
    {
        'author': 'Steve Rogers',
        'title': 'Blog Post from Captain America',
        'content': 'Third Post content.',
        'date_posted': '13/05/2019'
    },
    {
        'author': 'Bruce Wayne',
        'title': 'Blog Post etc tec',
        'content': 'fourth Post content.',
        'date_posted': '12/05/2019'
    }

]
"""

# For number of posts visible in one page
PER_PAGE_POSTS: int = 5


@main.route('/test')
def hello():
    return render_template('testpage.html')


@main.route("/")
@main.route('/home')
def home():
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    # To show the most recent post at the beginning,
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=PER_PAGE_POSTS)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

