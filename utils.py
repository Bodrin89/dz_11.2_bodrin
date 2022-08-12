
import json

FILE = 'candidates.json'
def load_candidates_from_json(all_candidates):

    """возвращает список всех кандидатов"""

    with open(all_candidates, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(list_candidates, candidate_id):

    """возвращает одного кандидата по его id"""

    for item in list_candidates:
        if candidate_id == item['id']:
            return item
    return f'No candidate id:{candidate_id}'


def get_candidates_by_name(list_candidates, candidate_name):

    """возвращает кандидатов по имени"""
    person = []
    for item in list_candidates:
        if candidate_name.strip().lower() in item['name'].strip().lower():
            person.append(item)
    return person


def get_candidates_by_skill(list_candidates, skill_name):

    """возвращает кандидатов по навыку"""

    result_skills = []

    for item in list_candidates:
        if skill_name.strip().lower() in (item["skills"]).split():
            result_skills.append(item)
    return result_skills

