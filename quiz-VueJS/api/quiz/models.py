from .app import db
from flask import url_for, jsonify


class Questionnaire(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return "<Questionnaire (%d) %s>" % (self.id, self.name)

    def to_json(self):
        json_questionnaire = {
            'url': url_for('get_quiz', 
                quiz_id=self.id, _external=True),
            'name': self.name,
            'questions': [ q.desc() for q in self.questions ]
            
        }
        return json_questionnaire

class Question(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String(120))
    question_type = db.Column(db.String(12))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire",
        backref=db.backref("questions", 
        lazy="dynamic"))

    def __repr__(self):
        return "<Question (%d) %s>" % (self.id, self.title)

    def to_json(self):
        json_quest = {
            'url': url_for('get_quest',quest_id=self.id, _external=True),
            'questionnaire_url': url_for('get_quiz'
                , quiz_id=self.questionnaire_id,
                 _external=True),
            'title': self.title,
            'question_type': self.question_type,
            'question': self.content()
            }
        return jsonify(json_quest)

    def desc(self):
        json_quest = {
            'url': url_for('get_quest',quest_id=self.id, _external=True),
            'title': self.title,
            }
        return json_quest
    
    __mapper_args__ = {
        'polymorphic_identity': 'question',
        'with_polymorphic': '*',
        "polymorphic_on": question_type
    }

class SimpleQuestion(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    first_alternative = db.Column(db.String(120))
    second_alternative = db.Column(db.String(120))

    def content(self):
        quest = dict()
        quest['first_alternative'] = self.first_alternative
        quest['second_alternative'] = self.second_alternative
        return quest

    __mapper_args__ = {
        'polymorphic_identity': 'simplequestion',
        'with_polymorphic': '*',
        "polymorphic_load": "inline"
    }

class MultipleQuestion(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    first_alternative = db.Column(db.String(120))
    second_alternative = db.Column(db.String(120))
    third_alternative = db.Column(db.String(120))
    fourth_alternative = db.Column(db.String(120))

    def content(self):
        quest = dict()
        quest['first_alternative'] = self.first_alternative
        quest['second_alternative'] = self.second_alternative
        quest['third_alternative'] = self.third_alternative
        quest['fourth_alternative'] = self.fourth_alternative
        return quest

    __mapper_args__ = {
        'polymorphic_identity': 'multiplequestion',
        'with_polymorphic': '*',
        "polymorphic_load": "inline"
    }

def get_questionnaires():
    return Questionnaire.query.all()

def get_questionnaire(quiz_id):
    return Questionnaire.query.get_or_404(quiz_id)

def get_all_questions_quiz(quiz_id):
    return Question.query.get_or_404(quiz_id)

def get_all_questions():
    return Question.query.all()

def get_question(id):
    return Question.query.get_or_404(id)

def create_questionnaire(name):
    questionnaire = Questionnaire(name=name)
    db.session.add(questionnaire)
    db.session.commit()
    return questionnaire

def create_question(title, question_type, questionnaire_id, **kwargs):
    question = Question(title=title, question_type=question_type, 
        questionnaire_id=questionnaire_id)
    db.session.add(question)
    db.session.commit()
    return question

def create_simple_question(title, question_type, questionnaire_id, 
    first_alternative, second_alternative):
    question = SimpleQuestion(title=title, question_type=question_type, 
        questionnaire_id=questionnaire_id, 
        first_alternative=first_alternative, 
        second_alternative=second_alternative)
    db.session.add(question)
    db.session.commit()
    return question

def create_multiple_question(title, question_type, questionnaire_id, 
    first_alternative, second_alternative, third_alternative, 
    fourth_alternative):
    question = MultipleQuestion(title=title, question_type=question_type, 
        questionnaire_id=questionnaire_id, 
        first_alternative=first_alternative, 
        second_alternative=second_alternative, 
        third_alternative=third_alternative, 
        fourth_alternative=fourth_alternative)
    db.session.add(question)
    db.session.commit()
    return question

def get_questions_by_type(question_type):
    return Question.query.filter_by(question_type=question_type).all()

def delete_questionnaire(quiz_id):
    questionnaire = get_questionnaire(quiz_id)
    db.session.delete(questionnaire)
    db.session.commit()

def delete_question(quest_id):
    question = get_question(quest_id)
    db.session.delete(question)
    db.session.commit()
