from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Temp')
bot.set_trainer(ListTrainer)

for files in os.listdir('/usr/src/app/english/'):
    data = open('/usr/src/app/english/' + files ,'r').readlines()
    bot.train(data)

while True:
    message = input('You: ')
    if message.strip() != 'Bye' or message.strip() != 'bye':
        reply = bot.get_response(message)
        print('ChatBot: ', reply)
    if message.strip() == 'Bye' or message.strip() == 'bye':
        print ('ChatBot: Bye')
        break
