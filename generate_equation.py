import random


def generate_operator():
    return random.choice(['+', '-', '*', r'/'])


def generate_number_modification(number, modification_prob=.1):
    if number >= 0:
        # Apply modification
        if random.random() < modification_prob:
            # Apply power
            if random.random() < 1:
                return str(number) + '^{' + generate_number(modification_prob=0, small_number=True) + '}'
            # Apply square root
            else:
                return r'\sqrt{' + str(number) + '}'
        else:
            return str(number)
    else:
        if random.random() < modification_prob:
            return '(' + str(number) + ')^{' + generate_number(modification_prob=0, small_number=True) + '}'
        return '(' + str(number) + ')'


def generate_number(allow_zero=True, modification_prob=.1, small_number=False):
    if small_number:
        lower_limit = -3
        upper_limit = 3
    else:
        lower_limit = -10
        upper_limit = 10

    if allow_zero:
        number = random.randint(lower_limit, upper_limit)
    else:
        number = random.choice([x for x in range(lower_limit, upper_limit) if x not in [0, 1]])

    return generate_number_modification(number, modification_prob)


def generate_equation():
    component_number = random.randint(2, 4)
    equation = ''
    for i in range(component_number):
        fraction_prob = random.random()

        # Fraction
        if fraction_prob <= .75 or component_number == 1:
            equation += r'\frac{' + generate_number() +  '}{' + generate_number(allow_zero=False) + '}'
        else:
            equation += generate_number()

        # Add operator unless it is the last number
        if i < component_number - 1:
            equation += generate_operator()
    return equation


def generate_equation_page():
    import streamlit as st
    from latex2sympy2 import latex2sympy
    import sympy

    while True:
        equation = generate_equation()
        answer = latex2sympy(equation).simplify()
        if type(answer) is not sympy.core.numbers.ComplexInfinity and type(answer) is not sympy.core.numbers.NaN:
            break

    return equation, answer
    st.latex(equation)


    st.write(latex2sympy(equation).simplify())
    task_input = st.text_input('Podaj odpowiedź')

    return [task_input], [answer]
