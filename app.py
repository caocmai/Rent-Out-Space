from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template("index.html")

@app.route('/product_page')
def about():
    """Return homepage."""
    return render_template("product_page.html")

@app.route('/sign_up')
def sign_up():
    """Return homepage."""
    return render_template("sign_up.html")


@app.route('/login')
def login():
    """Return homepage."""
    return render_template("login.html")

@app.route('/about')
def about_page():
    """Return homepage."""
    return render_template("about.html")

@app.route('/featured')
def featured():
    """Return homepage."""
    return render_template("featured.html")

@app.route('/search')
def search():
    """Return homepage."""
    return render_template("search.html")

if __name__ == '__main__':
    app.run(debug=True)