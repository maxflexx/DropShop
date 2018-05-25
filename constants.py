import telebot
token = "556636621:AAFk6jxT2JNUCr1Yy0QBotmCAHIz7WGYoNc"

dataBaseUri = 'mongodb://bot:bot228@ds133550.mlab.com:33550/dropshop'

welcomeKeyBoard = telebot.types.ReplyKeyboardMarkup(True,True)
welcomeKeyBoard.row('поставщик')
welcomeKeyBoard.row('продавец')

# getNumberKeyBoard = telebot.types.ReplyKeyboardMarkup(True,False)
# getNumberKeyBoard.row('/number')

lookingKeyBoard = telebot.types.ReplyKeyboardMarkup(True,True)
lookingKeyBoard.row('ищу')

# sellingKeyBoard = telebot.types.ReplyKeyboardMarkup(True,False)
# sellingKeyBoard.row('/selling')


hideKeyBoard = telebot.types.ReplyKeyboardRemove()