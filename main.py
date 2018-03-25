from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    bot = ChatBot('Temp')
    bot.set_trainer(ListTrainer)

    for files in os.listdir('/usr/src/app/english/'):
        data = open('/usr/src/app/english/' + files ,'r').readlines()
        bot.train(data)

	# kernel now ready for use
	while True:
	    if message == "bye":
	        exit()
	    else:
	        bot_response = bot.get_response(message)
	        # print bot_response
	        return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
