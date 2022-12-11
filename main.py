import pathlib
from flask import Flask, render_template

import src.htmlgen as hgen

root_dir = pathlib.Path().resolve()

app = Flask(__name__)
    
@app.route('/')
def index():
    blist = hgen.html_element('b', 'list')
    bsublist = hgen.html_element('b', 'sublist')
    sublist = hgen.html_list(['i', 'am', 'a', bsublist], style='"color: red"')
    list = hgen.html_list(['i', 'am', 'a', blist, sublist], style='"color: blue"')
    return render_template(
        'index.html',
        title = 'I am a title',
        content = list,
    )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
