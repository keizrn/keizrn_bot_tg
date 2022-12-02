from sympy import sympify
from decimal import Decimal
import core.views as v

a = 0
b = 0
op = ''
expr = ''


def calc_init(user_dict):
    global a, b, op, expr
    op = user_dict["operation"]
    try:
        match user_dict['calc_type']:
            case 'decimal':
                a = Decimal(user_dict["first_num"])
                b = Decimal(user_dict["second_num"])
                return calc(), True
            case 'complex':
                a = complex(user_dict["first_num"].lower().replace('i', 'j'))
                b = complex(user_dict["second_num"].lower().replace('i', 'j'))
                return calc(), True
            case 'free':
                expr = user_dict["expression"]
                return free_calc(), True
    except:
        return 0, False


def calc():
    match op:
        case '*':
            return a * b
        case '/':
            if b == 0:
                return v.text_err(7)  # ошибка: деление на 0
            else:
                return a / b
        case '+':
            return a + b
        case '-':
            return a - b


def free_calc():
    return f'Ответ: {expr} = {sympify(expr.strip())}'