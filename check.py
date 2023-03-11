import random

from telegram import bot


# def get_ints():
#     """
#     Проверка на ввод числа
#     """
#     while True:
#         try:
#             num = int(input('value = '))
#             return num
#         except ValueError:
#             print('Ошибка. Ожидалось вещественное число.')
#
#
# def test_division(x, y):
#     """Проверка деление на 0 """
#     except ZeroDivisionError:
#          bot.send_message(update.chat.id, 'На ноль делить нельзя')
#
def check_real_number(update, num):
    while True:
        try:
            num = int(update.message.text)

            return num
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')


def check_operation(update, operations):
    while True:
        try:
            oper = update.message.text
            return oper
        except ValueError:
            return update.message.reply_text('Введите число: ')
    # try:
    #     x = update.text
    #     string = compile(x, 'string', 'eval')
    #     c = eval(string)
    #     bot.send_message(update.chat.id, f"{update.text} = {c}")
    # except ZeroDivisionError:
    #     bot.send_message(update.chat.id, 'На ноль делить нельзя')
    # except SyntaxError:
    #     bot.send_message(update.chat.id, 'Я понимаю только цифры')
    # except NameError:
    #     bot.send_message(update.chat.id,
    #                      random.choice(seq=['Я понимаю только цифры', "Я тебя не понял", "Ты о чем?"]))

# @bot.message_handler(func=lambda message: True)
# def calc(message, _):
#     try:
# x = message.text
# string = compile(x, 'string', 'eval')
# c = eval(string)
# bot.send_message(message.chat.id, f"{message.text} = {c}")
# except ZeroDivisionError:
#     bot.send_message(message.chat.id, 'На ноль делить нельзя')
# except SyntaxError:
#     bot.send_message(message.chat.id, 'Я понимаю только цифры')
# except NameError:
#     bot.send_message(message.chat.id,
#                      random.choice(seq=['Я понимаю только цифры', "Я тебя не понял", "Ты о чем?"]))
