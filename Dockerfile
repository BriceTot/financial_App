#use python 3.8 as a base of this image
FROM python:3.8

#directory code is created and used as the working directory
WORKDIR /code

#create a new directory in code to put in it html templates
RUN mkdir templates

#create a new directory in code to put in it the css file
RUN mkdir static

RUN mkdir static/style

#copy the file containing all modules used by the app
COPY requirements.txt .

#install all modules used by the app
RUN pip install -r requirements.txt

#copy the source code of the app
COPY src/app.py .

#copy the html file in the templates directory
COPY src/prices.html ./templates

#copy the css file in the static directory
COPY src/style.css ./static/style

#run the app
CMD [ "python", "./app.py" ]
