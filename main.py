from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import(
    CallbackContext,
    Updater,
    PicklePersistence,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CommandHandler
)
from cred import TOKEN
from menu import first_menu_keyboard, lose_menu_keyboard
from key_buttons import tele_button, lose_button


def start(update: Update, context: CallbackContext): 
    update.message.reply_text(   
        f'''Добрый день!
            Путь к вашей мечте начинается прямо сейчас!
            Выберите желаемое вами действие , {update.effective_user.username}''',
            reply_markup = first_menu_keyboard()
    )


def resive_lose_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''Перед тем как вы начнете,просим вас прочитать ниже написанный тект!
        Похудение, рассчитанное не на короткий, а на длительный период, по правилам должно идти постепенно,
        без резкого обрыва калорийности. Поэтому если вы сейчас питаетесь на ~2500 калорий, то резко снижать
        ежедневный калораж до 1500 ккал не рекомендуется. Рекомендуем уменьшать суточную калорийность постепенно
        (по 200-300 ккал еженедельно), чтобы избежать проблем со здоровьем или срывов с диеты.
        Выберите ваш ежедневный рацион на неделю:''',
        reply_markup = lose_menu_keyboard()
    )

LOSE = tele_button[0]

def resive_gain_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''Перед тем как вы начнете,просим вас прочитать ниже написанный тект!
        В среднем человеку с недостаточной массой тела необходимо увеличить потребление 
        калорий на 200-1000 ккал в день. Все зависит от цели. Если мужчина или женщина 
        хотят набирать вес постепенно, пусть и медленно, достаточно увеличить суточную 
        калорийность на 200-300 ккал. Для ускоренного получения результата калораж должен
        возрасти на 700-1000 ккал.
        Советую вам посмотреть фото и видео ниже'''
    )

    update.message.reply_photo(
       photo=open ('image/gait.jpg', 'rb')
    )

    update.message.reply_text('https://youtu.be/8pYV4nBfSTI')

    



GAIT = tele_button[1]

def resive_main_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Возвращаемся на главное меню",
        reply_markup = first_menu_keyboard()
    )

BACK = lose_button[4]  

def lose_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='python_day_1'),
            InlineKeyboardButton('day-2', callback_data='python_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='python_day_3'),
        InlineKeyboardButton('day-4', callback_data='python_day_4')],

        [InlineKeyboardButton('day-5', callback_data='python_day_5'),
        InlineKeyboardButton('day-6', callback_data='python_day_6')],

        [InlineKeyboardButton('day-7', callback_data='python_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите день:",
        reply_markup=reply_markup
    )

def inline_button(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('day-1', callback_data='python_day_1'),
        InlineKeyboardButton('day-2', callback_data='python_day_2'),
    ],
    [InlineKeyboardButton('day-3', callback_data='python_day_3'),
    InlineKeyboardButton('day-4', callback_data='python_day_4')],

    [InlineKeyboardButton('day-5', callback_data='python_day_5'),
    InlineKeyboardButton('day-6', callback_data='python_day_6')],

    [InlineKeyboardButton('day-7', callback_data='python_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    if query.data == 'python_day_1':
        context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/Ux2mvwmWKUA',
           reply_markup=reply_markup
        )


    keyboard = [
    [
        InlineKeyboardButton('day-1', callback_data='python_day_1'),
        InlineKeyboardButton('day-2', callback_data='python_day_2'),
    ],
    [InlineKeyboardButton('day-3', callback_data='python_day_3'),
    InlineKeyboardButton('day-4', callback_data='python_day_4')],

    [InlineKeyboardButton('day-5', callback_data='python_day_5'),
    InlineKeyboardButton('day-6', callback_data='python_day_6')],

    [InlineKeyboardButton('day-7', callback_data='python_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == 'python_day_2':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'https://youtu.be/x0ZRqDG0I-I',
            reply_markup=reply_markup
        )
    keyboard = [
    [
        InlineKeyboardButton('day-1', callback_data='python_day_1'),
        InlineKeyboardButton('day-2', callback_data='python_day_2'),
    ],
    [InlineKeyboardButton('day-3', callback_data='python_day_3'),
    InlineKeyboardButton('day-4', callback_data='python_day_4')],

    [InlineKeyboardButton('day-5', callback_data='python_day_5'),
    InlineKeyboardButton('day-6', callback_data='python_day_6')],

    [InlineKeyboardButton('day-7', callback_data='python_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == 'python_day_3':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'https://youtu.be/orf8ox7UI80',
            reply_markup=reply_markup
        )

    keyboard = [
    [
        InlineKeyboardButton('day-1', callback_data='python_day_1'),
        InlineKeyboardButton('day-2', callback_data='python_day_2'),
    ],
    [InlineKeyboardButton('day-3', callback_data='python_day_3'),
    InlineKeyboardButton('day-4', callback_data='python_day_4')],

    [InlineKeyboardButton('day-5', callback_data='python_day_5'),
    InlineKeyboardButton('day-6', callback_data='python_day_6')],

    [InlineKeyboardButton('day-7', callback_data='python_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == 'python_day_4':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'https://youtu.be/upMh5gYo5bI',
            reply_markup=reply_markup
        )

    keyboard = [
    [
        InlineKeyboardButton('day-1', callback_data='python_day_1'),
        InlineKeyboardButton('day-2', callback_data='python_day_2'),
    ],
    [InlineKeyboardButton('day-3', callback_data='python_day_3'),
    InlineKeyboardButton('day-4', callback_data='python_day_4')],

    [InlineKeyboardButton('day-5', callback_data='python_day_5'),
    InlineKeyboardButton('day-6', callback_data='python_day_6')],

    [InlineKeyboardButton('day-7', callback_data='python_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == 'python_day_5':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'https://youtu.be/WNMxm-sYr5g',
            reply_markup=reply_markup
        )

    keyboard = [
    [
        InlineKeyboardButton('day-1', callback_data='python_day_1'),
        InlineKeyboardButton('day-2', callback_data='python_day_2'),
    ],
    [InlineKeyboardButton('day-3', callback_data='python_day_3'),
    InlineKeyboardButton('day-4', callback_data='python_day_4')],

    [InlineKeyboardButton('day-5', callback_data='python_day_5'),
    InlineKeyboardButton('day-6', callback_data='python_day_6')],

    [InlineKeyboardButton('day-7', callback_data='python_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == 'python_day_6':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'https://youtu.be/VQMAAO-_7K8',
            reply_markup=reply_markup
        )

    keyboard = [
    [
        InlineKeyboardButton('day-1', callback_data='python_day_1'),
        InlineKeyboardButton('day-2', callback_data='python_day_2'),
    ],
    [InlineKeyboardButton('day-3', callback_data='python_day_3'),
    InlineKeyboardButton('day-4', callback_data='python_day_4')],

    [InlineKeyboardButton('day-5', callback_data='python_day_5'),
    InlineKeyboardButton('day-6', callback_data='python_day_6')],

    [InlineKeyboardButton('day-7', callback_data='python_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == 'python_day_7':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'https://youtu.be/o7SiKpNg7RY',
            reply_markup=reply_markup
        )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1200_day_1'),
            InlineKeyboardButton('day-2', callback_data='1200_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1200_day_3'),
        InlineKeyboardButton('day-4', callback_data='1200_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1200_day_5'),
        InlineKeyboardButton('day-6', callback_data='1200_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1200_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1200_day_1':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/i5hgSpw6rro',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1200_day_1'),
            InlineKeyboardButton('day-2', callback_data='1200_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1200_day_3'),
        InlineKeyboardButton('day-4', callback_data='1200_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1200_day_5'),
        InlineKeyboardButton('day-6', callback_data='1200_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1200_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1200_day_2':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/35ZsZVfVQHA',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1200_day_1'),
            InlineKeyboardButton('day-2', callback_data='1200_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1200_day_3'),
        InlineKeyboardButton('day-4', callback_data='1200_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1200_day_5'),
        InlineKeyboardButton('day-6', callback_data='1200_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1200_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1200_day_3':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/JHfu-sQBS5g',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1200_day_1'),
            InlineKeyboardButton('day-2', callback_data='1200_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1200_day_3'),
        InlineKeyboardButton('day-4', callback_data='1200_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1200_day_5'),
        InlineKeyboardButton('day-6', callback_data='1200_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1200_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1200_day_4':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/QfCOdN96VWc',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1200_day_1'),
            InlineKeyboardButton('day-2', callback_data='1200_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1200_day_3'),
        InlineKeyboardButton('day-4', callback_data='1200_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1200_day_5'),
        InlineKeyboardButton('day-6', callback_data='1200_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1200_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1200_day_5':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/sAVeTupAGUU',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1200_day_1'),
            InlineKeyboardButton('day-2', callback_data='1200_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1200_day_3'),
        InlineKeyboardButton('day-4', callback_data='1200_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1200_day_5'),
        InlineKeyboardButton('day-6', callback_data='1200_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1200_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1200_day_6':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/pmuK-PFounA',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1200_day_1'),
            InlineKeyboardButton('day-2', callback_data='1200_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1200_day_3'),
        InlineKeyboardButton('day-4', callback_data='1200_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1200_day_5'),
        InlineKeyboardButton('day-6', callback_data='1200_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1200_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1200_day_7':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/LZAqyPYglwM',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1000_day_1'),
            InlineKeyboardButton('day-2', callback_data='1000_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1000_day_3'),
        InlineKeyboardButton('day-4', callback_data='1000_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1000_day_5'),
        InlineKeyboardButton('day-6', callback_data='1000_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1000_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1000_day_1':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/rXy1p60Tfmw',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1000_day_1'),
            InlineKeyboardButton('day-2', callback_data='1000_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1000_day_3'),
        InlineKeyboardButton('day-4', callback_data='1000_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1000_day_5'),
        InlineKeyboardButton('day-6', callback_data='1000_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1000_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1000_day_2':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/TMQ78yrAddM',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1000_day_1'),
            InlineKeyboardButton('day-2', callback_data='1000_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1000_day_3'),
        InlineKeyboardButton('day-4', callback_data='1000_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1000_day_5'),
        InlineKeyboardButton('day-6', callback_data='1000_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1000_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1000_day_3':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/aGmsCrVt49I',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1000_day_1'),
            InlineKeyboardButton('day-2', callback_data='1000_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1000_day_3'),
        InlineKeyboardButton('day-4', callback_data='1000_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1000_day_5'),
        InlineKeyboardButton('day-6', callback_data='1000_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1000_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1000_day_4':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/31mjy3-qz8w',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1000_day_1'),
            InlineKeyboardButton('day-2', callback_data='1000_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1000_day_3'),
        InlineKeyboardButton('day-4', callback_data='1000_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1000_day_5'),
        InlineKeyboardButton('day-6', callback_data='1000_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1000_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1000_day_5':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/rXy1p60Tfmw',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1000_day_1'),
            InlineKeyboardButton('day-2', callback_data='1000_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1000_day_3'),
        InlineKeyboardButton('day-4', callback_data='1000_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1000_day_5'),
        InlineKeyboardButton('day-6', callback_data='1000_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1000_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1000_day_6':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/TMQ78yrAddM',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1000_day_1'),
            InlineKeyboardButton('day-2', callback_data='1000_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1000_day_3'),
        InlineKeyboardButton('day-4', callback_data='1000_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1000_day_5'),
        InlineKeyboardButton('day-6', callback_data='1000_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1000_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '1000_day_7':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/aGmsCrVt49I',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='800_day_1'),
            InlineKeyboardButton('day-2', callback_data='800_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='800_day_3'),
        InlineKeyboardButton('day-4', callback_data='800_day_4')],

        [InlineKeyboardButton('day-5', callback_data='800_day_5'),
        InlineKeyboardButton('day-6', callback_data='800_day_6')],

        [InlineKeyboardButton('day-7', callback_data='800_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard) 
    if query.data == '800_day_1':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/HgRxe8JQqgs',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='800_day_1'),
            InlineKeyboardButton('day-2', callback_data='800_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='800_day_3'),
        InlineKeyboardButton('day-4', callback_data='800_day_4')],

        [InlineKeyboardButton('day-5', callback_data='800_day_5'),
        InlineKeyboardButton('day-6', callback_data='800_day_6')],

        [InlineKeyboardButton('day-7', callback_data='800_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '800_day_2':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/r_RRYgd8Pcw',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='800_day_1'),
            InlineKeyboardButton('day-2', callback_data='800_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='800_day_3'),
        InlineKeyboardButton('day-4', callback_data='800_day_4')],

        [InlineKeyboardButton('day-5', callback_data='800_day_5'),
        InlineKeyboardButton('day-6', callback_data='800_day_6')],

        [InlineKeyboardButton('day-7', callback_data='800_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '800_day_3':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/kvt5xNOcnC0',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='800_day_1'),
            InlineKeyboardButton('day-2', callback_data='800_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='800_day_3'),
        InlineKeyboardButton('day-4', callback_data='800_day_4')],

        [InlineKeyboardButton('day-5', callback_data='800_day_5'),
        InlineKeyboardButton('day-6', callback_data='800_day_6')],

        [InlineKeyboardButton('day-7', callback_data='800_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '800_day_4':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/JiOcuYMbKpA',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='800_day_1'),
            InlineKeyboardButton('day-2', callback_data='800_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='800_day_3'),
        InlineKeyboardButton('day-4', callback_data='800_day_4')],

        [InlineKeyboardButton('day-5', callback_data='800_day_5'),
        InlineKeyboardButton('day-6', callback_data='800_day_6')],

        [InlineKeyboardButton('day-7', callback_data='800_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '800_day_5':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/pIeDWEkCV4E',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='800_day_1'),
            InlineKeyboardButton('day-2', callback_data='800_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='800_day_3'),
        InlineKeyboardButton('day-4', callback_data='800_day_4')],

        [InlineKeyboardButton('day-5', callback_data='800_day_5'),
        InlineKeyboardButton('day-6', callback_data='800_day_6')],

        [InlineKeyboardButton('day-7', callback_data='800_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '800_day_6':
       context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/n2Fjyu_NhUE',
           reply_markup=reply_markup
       )

    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='800_day_1'),
            InlineKeyboardButton('day-2', callback_data='800_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='800_day_3'),
        InlineKeyboardButton('day-4', callback_data='800_day_4')],

        [InlineKeyboardButton('day-5', callback_data='800_day_5'),
        InlineKeyboardButton('day-6', callback_data='800_day_6')],

        [InlineKeyboardButton('day-7', callback_data='800_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if query.data == '800_day_7':
        context.bot.send_message(
           update.effective_chat.id,
           text = 'https://youtu.be/OMPETu_gnNY',
           reply_markup=reply_markup
        )






DAY1 = lose_button[0]

def lose2_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1200_day_1'),
            InlineKeyboardButton('day-2', callback_data='1200_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1200_day_3'),
        InlineKeyboardButton('day-4', callback_data='1200_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1200_day_5'),
        InlineKeyboardButton('day-6', callback_data='1200_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1200_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите день:",
        reply_markup=reply_markup
    )



KAL1200 = lose_button[1]


def lose3_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='1000_day_1'),
            InlineKeyboardButton('day-2', callback_data='1000_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='1000_day_3'),
        InlineKeyboardButton('day-4', callback_data='1000_day_4')],

        [InlineKeyboardButton('day-5', callback_data='1000_day_5'),
        InlineKeyboardButton('day-6', callback_data='1000_day_6')],

        [InlineKeyboardButton('day-7', callback_data='1000_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите день:",
        reply_markup=reply_markup
    )



KAL1000 = lose_button[2]


def lose4_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('day-1', callback_data='800_day_1'),
            InlineKeyboardButton('day-2', callback_data='800_day_2'),
        ],
        [InlineKeyboardButton('day-3', callback_data='800_day_3'),
        InlineKeyboardButton('day-4', callback_data='800_day_4')],

        [InlineKeyboardButton('day-5', callback_data='800_day_5'),
        InlineKeyboardButton('day-6', callback_data='800_day_6')],

        [InlineKeyboardButton('day-7', callback_data='800_day_7')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите день:",
        reply_markup=reply_markup
    )


KAL800 = lose_button[3]

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOSE),
    resive_lose_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(GAIT),
    resive_gain_menu
))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    resive_main_menu
))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(DAY1),
    lose_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KAL1200),
    lose2_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KAL1000),
    lose3_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KAL800),
    lose4_inline_menu
))



updater.dispatcher.add_handler(CallbackQueryHandler(inline_button))
updater.start_polling()  
updater.idle()