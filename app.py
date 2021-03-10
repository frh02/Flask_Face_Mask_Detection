import os
from flask import Flask, render_template
from views.users import user_blueprint

app = Flask(__name__)

app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

app.register_blueprint(user_blueprint, url_prefix="/users")

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
