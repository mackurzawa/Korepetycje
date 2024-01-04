import streamlit as st
from credentials import credentials


def verify_answers(task_inputs, answers):
    overall = st.empty()
    correct_counter = 0
    for i in range(len(answers)):
        st.header(f'Zadanie {i + 1}:')
        try:
            user_answer = round(eval(task_inputs[i].replace(',', '.')), 2)
        except:
            user_answer = None
        true_answer = round(eval(str(answers[i])), 2)
        if user_answer == true_answer:
            correct_counter += 1
            st.success(f'Super! Odpowiedź "{task_inputs[i]}" jest poprawna')
        else:
            st.error(f'Źle! Odpowiedź "{task_inputs[i]}" jest niepoprawna')
        st.markdown('---')
    overall.metric('Całkowity wynik:', str(correct_counter) + ' z ' + str(len(answers)) + ' = ' + str(
        int(correct_counter / len(answers) * 100)) + '%')
    if correct_counter / len(answers) == 1.:
        st.balloons()
    return str(correct_counter), str(len(answers)), str(int(correct_counter / len(answers) * 100)) + '%'


def save_homework_to_google_sheets(name, set_name, used_time, n_correct, n_all, metric):
    import pandas as pd
    from datetime import datetime
    import gspread

    url = r'https://docs.google.com/spreadsheets/d/11Guq49VaHAvK5fMcs31tacBNQhTya4zGyvzIoazd9f0/edit#gid=0'

    # gc = gspread.service_account(filename='service-account.json')
    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open_by_url(url)
    worksheet = sh.worksheet("Homework submissions")

    data = pd.DataFrame(worksheet.get_all_records())
    data.loc[len(data)] = [str(datetime.now()), name, set_name, used_time, n_correct, n_all, metric]
    worksheet.update([data.columns.values.tolist()] + list(data.values.tolist()))


def save_random_equation_to_google_sheets(equation, answer, user_answer, is_correct, used_time):
    import pandas as pd
    from datetime import datetime
    import gspread

    url = r'https://docs.google.com/spreadsheets/d/11Guq49VaHAvK5fMcs31tacBNQhTya4zGyvzIoazd9f0/edit#gid=0'

    gc = gspread.service_account(filename='service-account.json')
    sh = gc.open_by_url(url)
    worksheet = sh.worksheet("Random equation submissions")

    data = pd.DataFrame(worksheet.get_all_records())
    data.loc[len(data)] = [str(datetime.now()), st.session_state['username'], equation, answer, user_answer, is_correct, used_time]
    worksheet.update([data.columns.values.tolist()] + list(data.values.tolist()))
