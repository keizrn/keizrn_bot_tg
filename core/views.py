
bot_tg_wrong={0:'😕 Я еще только учусь понимать людей, поэтому попробуй написать /help',
              1:'🤖 Мой процессор не обрабатывает буквы, только цифры! ❌'
                '🔃 Перезапустите калькулятор командой /calc',
              2:'Выбрано неверное арифметическое действие ❌',
              3:'Выбран неверный вид калькулятора ❌',
              4:'Неверная команда, попробуйте еще раз'
              }

def welcome_message(username):
    return f'''👋 Привет, {username}! 
Я джуниор телеграм бот.

'''

'''С помощью меня ты можешь работать с такими выражениями как:
* Рациональные (например: 2 + 2)
* Комплексные (например: 1+2j + 3+4j)
* Свободные (например: (1+2)-3*4)
Еще я умею находить сумму двух полиномов'''


def welcome_message2(username):
    return f'''Напиши:
📋 /help - чтобы узнать список доступных команд
🌤 /weather - узнать погоду в вашем городе
🧮 /calc - чтобы запустить числовой калькулятор
⚙ /poly - чтобы найти сумму полиномов'''


def help_message():
    return f'''Доступные команды:
🚀 /start - Начало работы
🌤 /weather - узнать погоду в вашем городе
🧮 /calc - Запуск меню выбора вида калькулятора
⚙ /poly - Запуск расчета суммы двух полиномов
📋 /help - Узнать о доступных командах
🤷 /about - Получить информацию о боте'''


def about_message():
    return f'''💡 Данный бот был создан...
Над ботом работали:
@proDreams - Иван Ашихмин
@stela_kristina - Кристина Большакова
@keizrn - Наталья Кейзер'''


def wrong_value_message():
   return f'😕 Я еще только учусь понимать людей, поэтому попробуй написать /help'


def wrong_input():
    return '''🤖 Мой процессор не обрабатывает буквы, только цифры! ❌
🔃 Перезапустите калькулятор командой /calc'''


def end_calc():
    return f'''Расчёт завершён ✅.
Выберите /start или /calc'''


def end_poly():
    return f'''Расчёт завершён ✅.
Выберите /start или /poly'''


def got_operator(operator):
    return f'''Вы выбрали арифметическое действие {operator}.
Введите первое число:'''


def chosen_rational():
    return f'''Вы выбрали калькулятор рациональных чисел.
Выберите операцию:'''


def chosen_complex():
    return f'''Вы выбрали калькулятор комплексных чисел.
Выберите операцию:'''


def chosen_freeform():
    return f'''Вы выбрали калькулятор свободных выражений.
Введите выражение, например "(1+2)-3*4" :'''


def wrong_operator():
    return 'Выбрано неверное арифметическое действие ❌'


def wrong_calc_type():
    return 'Выбран неверный вид калькулятора ❌'


def choose_calc_type():
    return 'Выберите какие числа будем считать'


def enter_second_num():
    return 'Введите второе число:'


def start_poly():
    return 'Вы выбрали калькулятор для сложения полиномов\n' \
           'Пример: 5x3 + x2 + 4x + 99 = 0'


def first_poly():
    return 'Введите первый полином: '


def second_poly():
    return 'Введите второй полином: '


def end_weather():
    # Сообщение при окончании вывода
    return 'Рад был помочь. До встречи 🫶🏻'


def choose_weather_type():
    # Сообщение при выборе меню погода
    return 'Выберите тип поиска: по городу или по геолокации..\n' \
           '❗️ ВНИМАНИЕ функция "По геолокации" работает только на смартфоне 📱📲 при включенной геолокации 📡'


def wrong_weather_type():
    # Сообщение при неверном выборе меню погода
    text_err(4)    #return 'Неверная команда, попробуйте еще раз'


def chosen_city():
    # Сообщение при выборе поиска по городу
    return 'Введите название города на русском языке..\nНажмите /start, чтобы выйти.'


def chosen_geo():
    # Сообщение при выборе поиска по гео
    return 'Проверьте, включена ли у вас геолокация\n' \
           'Если вы посылаете запрос с компьютера, то данная функция недоступна\n' \

def text_err(num_1): 
    return(bot_tg_wrong[num_1])
