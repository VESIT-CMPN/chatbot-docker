# chatbot-docker
A machine learning chatbot is implemented in python and hosted on docker.

#### A web implementation of Chatbot using Flask.

### Requirements:
Flask==0.12
aiml==0.8.6

## Local Setup:
 1. Ensure that Python, Flask, SQLAlchemy, nginx and aiml are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *main.py*
 3. Chat will be live at [http://localhost:5000/](http://localhost:5000/)

### Deploying steps
Build the image
docker build -t sanjanamoghe/chatbot

Run the image
docker run --rm -p 5000:5000 --name chatbot sanjanamoghe/chatbot
Pushing the image on Docker


Pulling from Docker
docker run --rm -p 5000:5000 --name chatbot sanjanamoghe/chatbot


Run
docker run --rm -p 5000:5000 --name chatbot sanjanamoghe/chatbot


## License
This source is free to use, but docker does have a license.



## Group members
Prashant Dombale 15
Mohnish Katware 30 
Tanvi Kulkarni 36
Sanjana Moghe 43
Mahak Pancholi 51
Shreesh Rao 58
