from flask import Flask
import json

with open("candidates.json", 'r', encoding="utf-8") as file:
    candidates = json.load(file)

app = Flask(__name__)


@app.route('/')
def page_index():
    """
    Показывает список всех кандидатов
    :return: Список всех кандидатов
    """
    for i in range(len(candidates)):
        if i == 0:  # в самом начале создаётся строка all_candidates
            all_candidates = (f"Имя кандидата: {candidates[i]['name']}\n")
            all_candidates += (f"Позиция кандидата: {candidates[i]['position']}\n")
            all_candidates += (f"Навыки: {candidates[i]['skills']}\n\n")
        else:
            all_candidates += (f"Имя кандидата: {candidates[i]['name']}\n")
            all_candidates += (f"Позиция кандидата: {candidates[i]['position']}\n")
            all_candidates += (f"Навыки: {candidates[i]['skills']}\n\n")
    return f'''<pre>{all_candidates}</pre>'''


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """
    Показывает информацию о конкретном кандидате
    :param uid: id кандидата
    :return: Картинка, имя, позиция и навыки кандидата
    """
    if 0 < uid < len(candidates) + 1:  # проверяет, есть ли кандидат с таким id
        candidate = f"<img src='{candidates[uid - 1]['picture']}'>\n\n<pre>"
        candidate += (f"Имя кандидата: {candidates[uid - 1]['name']}\n")
        candidate += (f"Позиция кандидата: {candidates[uid - 1]['position']}\n")
        candidate += (f"Навыки: {candidates[uid - 1]['skills']}</pre>")
        return candidate
    else:
        return '''
        <pre>Пользователь с данным id отсутствует</pre>
        '''


@app.route("/skill/<skill>")
def page_skill(skill):
    '''
    Поиск кандидатов с необходимым навыком
    :param skill: Навык, который ищем
    :return: Список кандидатов
    '''
    candidates_with_skill = ""
    for i in range(len(candidates)):
        if skill.lower() in candidates[i]["skills"].lower():
            candidates_with_skill += (f"Имя кандидата: {candidates[i]['name']}\n")
            candidates_with_skill += (f"Позиция кандидата: {candidates[i]['position']}\n")
            candidates_with_skill += (f"Навыки: {candidates[i]['skills']}\n\n")
    if candidates_with_skill != "":
        return f'''<pre>{candidates_with_skill}</pre>'''
    else:
        return "<pre>Кандидатов с таким навыком нет</pre>"


app.run()
