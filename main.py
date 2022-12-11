import pathlib
from flask import Flask, render_template

import src.htmlgen as hgen

root_dir = pathlib.Path().resolve()

app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template(
        'index.html',
        title = 'I am a title',
        content = hgen.html_list([
            'i',
            'am',
            'a',
            hgen.html_element('b', 'list'),
            hgen.html_list(
                ['i',
                 'am',
                 'a',
                 hgen.html_element('b', 'sublist'),
                ],
                style = '"color: red"'
            )
        ]),
    )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
