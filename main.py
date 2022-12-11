import pathlib
from flask import Flask, render_template

root_dir = pathlib.Path().resolve()

app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template(
        'index.html',
        title = 'I am a title',
        content = '<ul><li>I</li><li>am</li><li><b>THE</b></li><li>content</li></ul>',
    )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
