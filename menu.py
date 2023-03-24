import telegram
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# from telegram.ext import(
#     CallbackContext
# )
from key_buttons import tele_button, lose_button

def first_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(tele_button[0])],
        [telegram.KeyboardButton(tele_button[1])],
    ])

    return telegram.ReplyKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=False
        )


def lose_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(lose_button[0])],
        [telegram.KeyboardButton(lose_button[1])],
        [telegram.KeyboardButton(lose_button[2])],
        [telegram.KeyboardButton(lose_button[3])],
        [telegram.KeyboardButton(lose_button[4])]
    ])

    return telegram.ReplyKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=False
        )


# def lose_inline_menu(update: Update, context: CallbackContext):
#     keyboard = [
#         [
#             InlineKeyboardButton('day-1', callback_data='python_day_1'),
#             InlineKeyboardButton('day-2', callback_data='python_day_2'),
#         ],
#         [InlineKeyboardButton('day-3', callback_data='python_day_3'),
#         InlineKeyboardButton('day-4', callback_data='python_day_4')],

#         [InlineKeyboardButton('day-5', callback_data='python_day_5'),
#         InlineKeyboardButton('day-6', callback_data='python_day_6')],

#         [InlineKeyboardButton('day-7', callback_data='python_day_7')]
#     ]
#     return telegram.InlineKeyboardMarkup(keyboard)
