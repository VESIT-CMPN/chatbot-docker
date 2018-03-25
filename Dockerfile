# our base image
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY main.py /usr/src/app/
COPY english /usr/src/app/english/
COPY templates/chat.html /usr/src/app/templates/chat.html

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/main.py"]
