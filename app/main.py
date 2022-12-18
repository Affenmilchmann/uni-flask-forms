import pathlib
from os import environ
from json import dump, load
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

import src.filehandle as fhandle

root_dir = str(pathlib.Path().resolve())
survey_data_dir = root_dir + "/survey_data"
data_file = root_dir + "/data/answers.json"

app = Flask(__name__)

def merge_dicts(data_dict, ans_dict: dict):
    ans_dict = list(ans_dict)
    data_dict['0'].append(min(max(10, int(ans_dict[0][1])), 100))
    for k, v in ans_dict[1:]:
        if '_' in k:
            par, chld = k.split('_')
        else:
            par, chld = k, v
        print(par, chld)
        data_dict[par][int(chld)] += 1
    return data_dict
         
def get_answers() -> dict:
    with open(data_file, 'r', encoding='utf-8') as f:
        return load(f)

def add_answer(ans):
    prev_data = get_answers()
    if not prev_data:
        prev_data = {
            '0': [],
            '1': [0] * 10,
            '2': [0] * 10,
            '3': [0] * 10,
            '4': [0] * 10,
            '5': [0] * 10,
        }
    merge_dicts(prev_data, ans)
    with open(data_file, 'w', encoding='utf-8') as f:
        dump(prev_data, f, indent=2, ensure_ascii=False)
        
def form_stats():
    stats = get_answers()
    if not stats:
        return [['No answers yet!'], ['']]
    stat_data = [[], []]
    actual_questions = fhandle.load_questions(survey_data_dir)
    for i, (k, v) in enumerate(stats.items()):
        print(i, k, v)
        stat_data[0].append(actual_questions[i]['question'])
        stat_data[1].append(v)
        
    stat_data[1][0] = "Avg: " + str(round(sum(map(int, stat_data[1][0])) / len(stat_data[1][0]), 2))
        
    for i in range(1, len(stat_data[0])):
        stat_data[0][i] = actual_questions[i]['question']
        summ = max(sum(stat_data[1][i]), 1)
        print("#"*20, "\n", stat_data[1][i], f"sum: {summ} len: {len(actual_questions[i]['options'])}\n", "#"*20)
        stat_data[1][i] = [int(round(100 * stat_data[1][i][int(k)] / summ, 0)) for k in range(len(actual_questions[i]['options']))]
        print(stat_data[1][i])
        
    return stat_data

@app.route('/', methods=('GET',))
def index():
    return render_template(
        'index.html',
    )
    
@app.route('/form', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        form_dict = request.form.items()
        try:
            for i in set(range(5)).difference(set([3])): 
                if not str(i) in request.form: raise AttributeError(str(request.form.to_dict()) + 'missing' + str(i))
            add_answer(form_dict)
        except AttributeError as e:
            return render_template(
                'form.html',
                q_data=fhandle.load_questions(survey_data_dir),
                error=str(e)
            )
        return redirect("/thank")
    
    elif request.method == 'GET':
        return render_template(
            'form.html',
            q_data=fhandle.load_questions(survey_data_dir),
            error=''
        )

@app.route('/stat', methods=('GET',))
def stat():
    return render_template(
        'stat.html',
        stat_data = form_stats(),
        questions = [key['options'] for key in fhandle.load_questions(survey_data_dir)[1:]]
    )
    
@app.route('/thank', methods=('GET',))
def thank():
    return render_template(
        'thank.html',
    )

if __name__ == '__main__':
    #database_initialization_sequence()
    app.run(debug=True, host='0.0.0.0')