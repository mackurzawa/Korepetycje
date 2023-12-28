import streamlit as st
from generate_equation import generate_equation_page
from main import verify_answers

if 'random_equation' not in st.session_state:
    st.session_state['generate_random_equation'] = False
    equation, answer = generate_equation_page()
    st.session_state['random_equation'] = equation
    st.session_state['random_equation_answer'] = answer
if 'generate_random_equation' in st.session_state:
    if st.session_state['generate_random_equation']:
        equation, answer = generate_equation_page()
        st.session_state['random_equation'] = equation
        st.session_state['random_equation_answer'] = answer

st.latex(st.session_state['random_equation'])
st.latex(st.session_state['random_equation_answer'])
task_input = st.text_input('Podaj odpowiedź')
check_button = st.button('Sprawdź')
if check_button:
    n_correct, n_all, metric = verify_answers([task_input], [st.session_state['random_equation_answer']])
    temp_button = st.button('Nowe zadanie')
    if temp_button:
        st.rerun()
        raise ValueError
        print('ej')
        equation, answer = generate_equation_page()
        st.session_state['generate_random_equation'] = True
        st.session_state['random_equation'] = equation
        st.session_state['random_equation_answer'] = answer
