import streamlit as st
import json
import time
import os

from latex2sympy2 import latex2sympy
from streamlit_extras.switch_page_button import switch_page

from utils import verify_answers, save_homework_to_google_sheets

HOMEWORK_NUMBER = 'No homework'
HOMEWORK_NUMBER = 'Homework 3'

def open_database(name):
    with open('homeworks.json', "r") as f:
        homeworks = json.loads(f.read())
    if name not in homeworks:
        st.warning('Błędne imię!')
        return None
    else:
        return homeworks[name]


def homework_page(homeworks):
    task_inputs = []
    answers = []
    for i_task, task in enumerate(homeworks[HOMEWORK_NUMBER]):
        st.header(f'Zadanie {i_task + 1}')
        question = task['Question']
        st.latex(question)
        answers.append(latex2sympy(question).simplify())
        task_inputs.append(st.text_input('Podaj odpowiedź', key=task['Question']))
        # Show Answers!
        # st.write(answers[-1])
        st.markdown('---')

    return st.button('Sprawdź!'), task_inputs, answers


if 'username' not in st.session_state:
    switch_page("main")
homeworks = open_database(st.session_state['username'])
if homeworks:
    if 'start_time' not in st.session_state:
        st.session_state['start_time'] = time.time()
    button, task_inputs, answers = homework_page(homeworks)
    if button:
        used_time = round(time.time() - st.session_state['start_time'])
        st.session_state['start_time'] = time.time()
        n_correct, n_all, metric = verify_answers(task_inputs, answers)
        save_homework_to_google_sheets(st.session_state['username'], HOMEWORK_NUMBER, used_time, n_correct, n_all, metric)