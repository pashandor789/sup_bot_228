import telebot

bot = telebot.TeleBot('5035371288:AAEfOQ16CHbvd4AG6uvkFPCGxjvAT8CcRis')


@bot.message_handler(commands=['stats'])
def get_stats(message):
    bot.send_message(message.chat.id,
                     "Кол-во людей в чате: " + str(bot.get_chat_member_count(message.chat.id)) + "\n" + "Кол-во "
                                                                                                        "админов "
                                                                                                        "в чате: "
                                                                                                        "" +
                     str(len(bot.get_chat_administrators(message.chat.id))))



@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id,
                     "Хай! Бот обладает следующим функционалом:" + "\n \n" + "Если введешь сначала в "
                                                                                        "сообщении одну "
                                                                                        "из "
                                                                                        "команд:" + "\n" + "/ban" + "\n"
                     + "/unban" + "\n" + "/makeadmin" + "\n" + "а потом user_id через пробел одного из участников, "
                                                               "то с пользователем произойдут соответствующие "
                                                               "изменения.")


@bot.message_handler(commands=['ban'], content_types=['text'])
def ban_user(message):
    bot.ban_chat_member(message.chat.id, user_id=int(message.text[5:]))


@bot.message_handler(commands=['unban'], content_types=['text'])
def unban_user(message):
    bot.unban_chat_member(message.chat.id, user_id=int(message.text[5:]))


@bot.message_handler(content_types=['left_chat_member'])
def getting_people_out_of_chat(message):
    bot.send_message(message.chat.id, text='Пока друг!')


@bot.message_handler(content_types=['new_chat_members'])
def getting_people_in_chat(message):
    bot.send_message(message.chat.id, text='Добро пожаловать в чат! Для '
                                           'взаимодействия введи команду /start')


@bot.message_handler(commands=['leave'])
def making_bot_leave(message):
    bot.send_message(message.chat.id, "Пока ребяты!")
    bot.leave_chat(message.chat.id)


bot.polling(none_stop=True, interval=0)
