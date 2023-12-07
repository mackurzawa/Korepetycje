import streamlit as st
import json


def welcome_page():
    st.title('Zadanie domowe')
    instruction_page()
    name = st.text_input('Podaj swoje imię')
    return name.lower()


def instruction_page():
    st.header('Instrukcja')
    # st.text('Wpisz swoje imię poniżej i nacisnij Enter')
    # st.text('Wypełnij luki swoimi wynikami')
    st.markdown('* Wpisz swoje imię poniżej i naciśnij Enter\n\n'
                '* Wypełnij luki w zadaniach swoimi wynikami\n\n'
                '  * Podawaj wyniki używajac tylko poniższych operatorów:\n\n'
                '  * \+ Dodawanie &emsp;&emsp;np. 3+1 = 4\n\n'
                '  * \- Odejmowanie &emsp;np. 20-3 = 17\n\n'
                '  * \* Mnożenie &emsp;np. 7*3 = 21\n\n'
                '  * / Dzielenie &emsp;np. 1/3 = 0.(6)\n\n'
                '  * () Nawiasy &emsp;np. (1+1)*2 = 4\n\n'
                '  * ^ Potęgowanie &emsp;np. 3^2 = 9\n\n'
                '  * sqrt(liczba) Pierwiastkowanie &emsp;np. sqrt(4) = 2\n\n'
                )


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
    for i_task, task in enumerate(homeworks['Homework 1']):
        st.header(f'Zadanie {i_task+1}')
        st.latex(task['Question'])
        answers.append(eval(task['Question']))
        task_inputs.append(st.text_input('Podaj odpowiedź', key=task['Question']))
        st.markdown('---')

    return st.button('Sprawdź!'), task_inputs, answers


def verify_answers(task_inputs, answers):
    overall = st.empty()
    correct_counter = 0
    for i in range(len(answers)):
        st.header(f'Zadanie {i+1}:')
        if eval(task_inputs[i]) == answers[i]:
            correct_counter += 1
            st.success(f'Super! Odpowiedź {task_inputs[i]} jest poprawna')
        else:
            st.error(f'Źle! Odpowiedź "{task_inputs[i]}" jest niepoprawna')
        st.markdown('---')
    overall.metric('Całkowity wynik:', str(correct_counter) +' z ' + str(len(answers)) + ' = ' + str(int(correct_counter/len(answers) * 100))+'%')
    if correct_counter/len(answers) == 1.:
        st.balloons()


def background_gradient():
    page_bg = """
        <style>
        [data-testid="stAppViewContainer"]{
            background-color: rgba(60, 91, 181, 1);
            background-image: linear-gradient(230deg, rgba(60, 91, 181, 1) 0%, rgba(41, 53, 86, 1) 100%);        }
        </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)


if __name__ == '__main__':
    background_gradient()
    name = welcome_page()
    if name:
        homeworks = open_database(name)
        if homeworks:
            button, task_inputs, answers = homework_page(homeworks)
            if button:
                verify_answers(task_inputs, answers)
