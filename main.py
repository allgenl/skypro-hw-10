from flask import Flask
import json

with open("candidates.json", 'r', encoding="utf-8") as file:
    candidates = json.load(file)

app = Flask(__name__)


@app.route('/')
def page_index():
    all_candidates = ""
    for i in range(len(candidates)):
        if i == 0:
            all_candidates = (f"Имя кандидата: {candidates[i]['name']}\n")
            all_candidates += (f"Позиция кандидата: {candidates[i]['position']}\n")
            all_candidates += (f"Навыки: {candidates[i]['skills']}\n\n")
        elif i == len(candidates) - 1:
            all_candidates += (f"Имя кандидата: {candidates[i]['name']}\n")
            all_candidates += (f"Позиция кандидата: {candidates[i]['position']}\n")
            all_candidates += (f"Навыки: {candidates[i]['skills']}")
        else:
            all_candidates += (f"Имя кандидата: {candidates[i]['name']}\n")
            all_candidates += (f"Позиция кандидата: {candidates[i]['position']}\n")
            all_candidates += (f"Навыки: {candidates[i]['skills']}\n\n")
    return f'''<pre>{all_candidates}</pre>'''


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    if 0 < uid < len(candidates) + 1:
        candidate = f"<img src='{candidates[uid - 1]['picture']}'>\n\n<pre>"
        candidate += (f"Имя кандидата: {candidates[uid - 1]['name']}\n")
        candidate += (f"Позиция кандидата: {candidates[uid - 1]['position']}\n")
        candidate += (f"Навыки: {candidates[uid - 1]['skills']}</pre>")
        return candidate
    else:
        return '''
        <pre>Пользователь с данным id отсутствует</pre>
        '''


app.run()