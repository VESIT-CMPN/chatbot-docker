# our base image
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY main.py /usr/src/app/
COPY main-raw.py /usr/src/app/
COPY templates/chat.html /usr/src/app/templates/chat.html
COPY aiml /usr/src/app/aiml

# tell the port number the container should expose
#EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/main.py"]
