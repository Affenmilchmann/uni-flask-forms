from pprint import pprint
from . import htmltags as tag

questions = [
    'what is your name?',
    'do you like pizza?',
    'how are you?'
]

def survey_quastions():
    uniq_prime = 2347
    fields = list()
    for i in range(len(questions)):
        fields.append(
            tag.label(questions[i], for_ = (i + 1) * uniq_prime)
        )
        fields.append(
            tag.input_(id_ = (i + 1) * uniq_prime, type_ = 'text')
        )
    fields.append(
        tag.label('Do you like this page?', for_='rateus') + tag.input_(id='rateus', type_='checkbox')
    )
    return tag.form(fields)

if __name__ == '__main__':
    print(survey_quastions())