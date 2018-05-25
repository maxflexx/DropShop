import telebot
import constants
import dataBaseRequests
bot = telebot.TeleBot(constants.token)
@bot.message_handler(commands=['start'])
def handle_start(message):
    who = dataBaseRequests.whoIsUser(message.from_user.id)
    if(who == None):
        bot.send_message(message.from_user.id, "Добро пожаловать в @dropShopingHelperBot," +" @" + message.from_user.username + "\nУкажите кто Вы, Поставщик или Продавец", reply_markup=constants.welcomeKeyBoard)
        return
    if(who == 'seller'):
        bot.send_message(message.from_user.id,
                         "Вы зарегистрированы как продавец, теперь вы можете отправлять объявления",
                         reply_markup=constants.lookingKeyBoard)
        return
    if(who == 'provider'):
        bot.send_message(message.from_user.id,"Мы пришлём Вам новые объявления, как только они появятся у нас!")
        return

#@bot.message_handler(commands=['поставщик'])
def handle_provider(message):
    who = dataBaseRequests.whoIsUser(message.from_user.id)
    if(who == None):

        bot.send_message(message.from_user.id,"Вы зарегистрированы как поставщик, теперь вам будут приходить объявления",reply_markup=constants.hideKeyBoard)
        dataBaseRequests.insertNewUser(" @" + message.from_user.username, 'provider',message.from_user.id)
    else:
        bot.send_message(message.from_user.id,"Вы уже зарегистрированы, поэтому не можете менять свою роль")


#@bot.message_handler(commands=['продавец'])
def handle_seller(message):
    who = dataBaseRequests.whoIsUser(message.from_user.id)
    if (who == None):
        bot.send_message(message.from_user.id,"Вы зарегистрированы как продавец, теперь вы можете отправлять объявления",reply_markup=constants.lookingKeyBoard)
        dataBaseRequests.insertNewUser(" @" + message.from_user.username,'seller',message.from_user.id)
    else:
        bot.send_message(message.from_user.id,"Вы уже зарегистрированы, поэтому не можете менять свою роль")

#@bot.message_handler(commands=['ищу'])
def handle_lookingFor(message):
    who = dataBaseRequests.whoIsUser(message.from_user.id)
    if (who == 'seller'):
        bot.send_message(message.from_user.id,"Вставьте фото.\nПод фото укажите описание")
    else:
        bot.send_message(message.from_user.id, "Ошибка!")

@bot.message_handler(content_types=['photo'])
def handle_publishingAd(message):
    who = dataBaseRequests.whoIsUser(message.from_user.id)
    if (who == 'seller'):
        if(message.caption!= None and len(message.caption)<=30):
            bot.send_photo(message.from_user.id, message.photo[0].file_id,message.caption+'\nОбращаться к @'+message.from_user.username)
            dataBaseRequests.echoToProviders( message.photo[0].file_id,message.caption+'\nОбращаться к @'+message.from_user.username)
        else:
            bot.send_message(message.from_user.id, "Описание не должно превышать 30 символов")
    else:
        bot.send_message(message.from_user.id, "Ошибка!")

@bot.message_handler(content_types=['text'])
def handle_commands(message):
    if(message.text=='поставщик'):
        handle_provider(message)
        return
    if (message.text == 'продавец'):
        handle_seller(message)
        return
    if (message.text == 'ищу'):
        handle_lookingFor(message)
        return

if __name__ == "__main__":
    print("Starting bot..")
    bot.polling(none_stop=True,interval=0)