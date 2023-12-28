import time

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from generate_equation import generate_equation_page
from utils import verify_answers, save_random_equation_to_google_sheets

if 'username' not in st.session_state:
    switch_page("main")
if "check_button" not in st.session_state:
    st.session_state["check_button"] = False

if "new_task_button" not in st.session_state:
    st.session_state["new_task_button"] = False


if 'equation' not in st.session_state:
    equation, answer = generate_equation_page()
    st.session_state['equation'] = equation
    st.session_state['equation_answer'] = answer

if 'start_time_equation' not in st.session_state:
    st.session_state['start_time_equation'] = time.time()

st.latex(st.session_state['equation'])
# Show answer
# st.latex(st.session_state['equation_answer'])
task_input = st.text_input('Podaj odpowiedź')


if st.button('Sprawdź'):
    st.session_state['check_button'] = True
    used_time = round(time.time() - st.session_state['start_time_equation'])
    n_correct, n_all, metric = verify_answers([task_input], [st.session_state['equation_answer'].n()])
    save_random_equation_to_google_sheets(str(st.session_state['equation']), str(st.session_state['equation_answer']), task_input, n_correct, used_time)


if st.session_state['check_button']:
    if st.button('Nowe zadanie'):
        st.session_state['check_button'] = not st.session_state['check_button']
        del st.session_state['equation']
        del st.session_state['equation_answer']
        del st.session_state['start_time_equation']
        st.rerun()
