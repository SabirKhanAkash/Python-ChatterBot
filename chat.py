import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('Paagla Mama')

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')


while True:
    message=input('You: ')
    if message.strip()!='Bye' or message.strip()!='bye':
        reply=bot.get_response(message)
        print('Paagla Mama: ',reply)

    if message.strip()=='Bye' or message.strip()=='bye':
        print('Paagla Mama: Bye')
        break
