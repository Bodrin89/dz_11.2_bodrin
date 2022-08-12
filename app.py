
from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

FILE_CANDIDATES = 'candidates.json'
array_candidates = load_candidates_from_json(FILE_CANDIDATES)

app = Flask(__name__)


@app.route('/')

def index():
    user_data = array_candidates
    candidates = render_template('list.html', user_data=user_data)
    return f'{candidates}'


@app.route('/search/<candidate_name>')

def search_name_candidate(candidate_name):
    user = get_candidates_by_name(array_candidates, candidate_name)
    count = len(user)
    found_candidates = render_template('search_name.html', count=count, user=user)
    return f'{found_candidates}'


@app.route('/id/<int:user_id>')

def go_id_candidate(user_id):
    user_ = get_candidate(array_candidates, user_id)
    name_user = user_['name']
    position_user = user_['position']
    foto_user = user_['picture']
    skills_user = user_['skills']
    data_user = render_template('single.html', name_user=name_user, position_user=position_user,
                                foto_user=foto_user, skills_user=skills_user)
    return f'{data_user}'


@app.route('/skill/<skill_name>')

def search_skills(skill_name):
    array_skills = get_candidates_by_skill(array_candidates, skill_name)
    count_skills = len(array_skills)

    found_skills = render_template('search_skills.html', array_skills=array_skills, count_skills=count_skills)
    return f'{found_skills}'


if __name__ == '__main__':
    app.run()
