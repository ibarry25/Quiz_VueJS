from .app import app, db
from .models import Question, Questionnaire, SimpleQuestion, MultipleQuestion, get_questionnaires, get_questionnaire, get_all_questions_quiz, get_all_questions, get_question, create_questionnaire, create_question, create_simple_question, create_multiple_question, get_questions_by_type, delete_questionnaire, delete_question

from flask import jsonify, abort, request, make_response



@app.route('/quiz/api/v1.0/quiz/', methods = ['GET'])
def get_all_quiz():
    quizs = get_questionnaires()
    return jsonify(questionnaires=[ q.to_json() for q in quizs])
    #return jsonify(questionnaires=[ q.to_json() for q in get_questionnaires()])

@app.route('/quiz/api/v1.0/quiz/<int:quiz_id>', methods = ['GET'])
def get_quiz(quiz_id):
    return get_questionnaire(quiz_id).to_json()


@app.route('/quiz/api/v1.0/quiz/', methods = ['POST'])
def create_quiz():
    if not request.json or not 'name' in request.json:
        abort(400)
    q = create_questionnaire(request.json['name'])
    return q.to_json() , 201

@app.route('/quiz/api/v1.0/question/<int:quest_id>', methods = ['GET'])
def get_quest(quest_id):
    q = get_question(quest_id)
    return q.to_json()

@app.route('/quiz/api/v1.0/quiz/<int:quiz_id>/questions', methods = ['GET'])
def get_all_quest_quiz(quiz_id):
    return jsonify(questions=[ q.to_json() for q in get_all_questions_quiz(quiz_id)])

@app.route('/quiz/api/v1.0/question/', methods = ['POST'])
def create_quest():
    #if not request.json or not 'title' or not 'question' or not # 'questionnaire_id' or not 'question_type' in request.json:
    #    abort(400)
    import json
    q = request.json
    q = json.loads(q)
    print('question')
    print(q)
    question_type = q['question_type']
    match(question_type):
        case('simplequestion'):
            q = create_simple_question(q['title'], q['question_type'], q['questionnaire_id'], q['question']['first_alternative'], q['question']['second_alternative'])  
        case('multiplequestion'):
            q = create_multiple_question(q['title'], q['question_type'], q['questionnaire_id'], q['question']['first_alternative'], q['question']['second_alternative'], q['question']['third_alternative'], q['question']['fourth_alternative'])
    qstnr = get_questionnaire(q.questionnaire_id)
    qstnr.questions.append(q)
    db.session.add(qstnr)
    db.session.add(q)
    db.session.commit()

    return q.to_json() , 201

@app.route('/quiz/api/v1.0/question/<int:quest_id>', methods = ['DELETE'])
def delete_quest(quest_id):
    delete_question(quest_id)
    return jsonify( { 'result': True } )

