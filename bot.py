import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )

def start_bot(bot, update):
    mytext = 'Привет, {}! Я простой бот и пока понимаю только комманду {}'.format(update.message.chat.first_name, '/start')
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)

def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text('Привет')

def main():
    updtr = Updater(settings.TELEGRAM_API_KEY)
    updtr.dispatcher.add_handler(CommandHandler('start', start_bot))
    updtr.dispatcher.add_handler(MessageHandler('Filters.txt', chat))
    updtr.start_polling()
    updtr.idle()

    if __name__ == '__main__':
        logging.info('Bot started')
        main()

    
