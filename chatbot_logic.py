from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch
import os

# Create a new chat bot named Carl
bot = ChatBot('SchoolChatBot', logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not understand.',
        'maximum_similarity_threshold': 0.85  # Adjust the threshold as needed
    }
])

# Get the current directory of this script
current_directory = os.path.dirname(os.path.realpath(__file__))

# Path to the updated school.yml file
corpus_file = os.path.join(current_directory, 'data', 'library.yml')

# Set up the trainer
trainer = ChatterBotCorpusTrainer(bot)

# Train the chat bot with the updated school.yml file
trainer.train(corpus_file)

# Function to get chatbot response
def get_response(input_text):
    response = bot.get_response(input_text)
    return str(response)