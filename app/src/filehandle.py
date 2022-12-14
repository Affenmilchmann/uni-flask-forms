from json import load

def load_questions(data_dir):
    data_file = "test_survey.json"
    with open(f"{data_dir}/{data_file}", 'r', encoding='utf-8') as f:
        return load(f)