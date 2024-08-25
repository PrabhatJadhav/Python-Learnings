import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils.mcq_questions as mcq_questions
from classes.question import Question

questions = [
    Question(mcq_questions.programming_questions[0],'b'),
    Question(mcq_questions.programming_questions[1],'a'),
    Question(mcq_questions.programming_questions[2],'b')
]
score=0

def run_test(questions):
    
    for question in questions:
        user_answer=input(question.prompt + "\n" +"Your Answer: ")
        if(user_answer == question.answer):
            global score
            score+=1
            
run_test(questions)
            
print("You got ", score, "/",len(questions))
        

