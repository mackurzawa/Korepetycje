import streamlit as st


def welcome_page():
    st.title('Zadanie domowe')
    instruction_page()
    name = st.text_input('Podaj swoje imię')
    return name.lower()


def instruction_page():
    st.header('Instrukcja')
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
    if len(name) > 0: st.session_state['username'] = name
    from streamlit_extras.switch_page_button import switch_page

    if name:
        col_b1, col_b2 = st.columns([1, 1])
        homework_button = col_b1.button('Zadanie Domowe', use_container_width=True)
        generate_button = col_b2.button('Wygeneruj równanie', use_container_width=True)

        if homework_button:
            switch_page('Zadanie-domowe')
        if generate_button:
            switch_page('Wygeneruj-równanie')
