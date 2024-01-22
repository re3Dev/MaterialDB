from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///materials.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    properties = db.Column(db.String(200))

    def __repr__(self):
        return f'<Material {self.name}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    results = Material.query.filter(Material.name.contains(search_query)).all()
    return render_template('search_results.html', results=results)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)