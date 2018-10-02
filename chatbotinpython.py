#Import ChatterBot,the Python library to generate automated responses to a user’s input. Download the package here: https://chatterbot.readthedocs.io/en/stable/setup.html

from chatterbot import ChatBot

#Import ListTrainer class, which allows a chatbot to be trained using a list of strings where the list represents a conversation

from chatterbot.trainers import ListTrainer

#Import os module for file, directory, and path manipulations
import os

#Define a bot

bot=ChatBot('Bot')

#Set the trainer to train the bot, we are using the ListTrainer class in the set_trainer method

bot.set_trainer(ListTrainer)

#Loading the file: Chatterbot corpus, a machine readable multilingual dialog corpus. This module is used to quickly train ChatterBot to respond to various inputs in different languages. We are using os module to access to directory where the chatterbot corpus is located.

for files in os.listdir('C:/Users/VIRID/Anaconda/chatterbot-corpus-1.1.2.tar/dist/chatterbot-corpus-1.1.2/chatterbot_corpus/data/english/'):

#Open the data (We will use same path), and we will use readlines() method to read the data  

    data=open('C:/Users/VIRID/Anaconda/chatterbot-corpus-1.1.2.tar/dist/chatterbot-corpus-1.1.2/chatterbot_corpus/data/english/'+files,'r').readlines()

#Training the bot with the data loaded in the script

bot.train(data)

#While the training is completed, we need to give inputs from the user, by using input function. The reply will be from the bot using get_response. We will print the reply from the bot. If the user's input is a 'Bye', then the bot finishes the chat. If the user's input is different from Bye, then the bot will keep the conversation going on.

while True:
 message=input('You:')
 if message.strip()!= 'Bye':
 reply=bot.get_response(message)
 print('ChatBot :', reply)
 
 if message.strip()== 'Bye':
 print('ChatBot:Bye')
 break
