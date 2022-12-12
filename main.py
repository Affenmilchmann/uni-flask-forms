import pathlib
from flask import Flask, render_template

import src.htmltags as htag

root_dir = pathlib.Path().resolve()

app = Flask(__name__)
    
@app.route('/')
def index():
    blist = htag.tag('b', 'unordered list')
    bsublist = htag.tag('b', 'ordered sublist')
    sublist = htag.ol(['i', 'am', 'an', bsublist], style='"color: red"')
    list = htag.ul(['i', 'am', 'an', blist, sublist], style='"color: blue"')
    return render_template(
        'index.html',
        title = 'I am a title',
        content = list,
    )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
