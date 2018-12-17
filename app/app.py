#Basic PythonFlask App. http://127.0.0.1:5000/

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
  school_count = 500
  return render_template('index.html', count=school_count)

if __name__ == '__main__':
    app.run(debug=True)