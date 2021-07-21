FROM python:buster

RUN pip3 install --upgrade pip
RUN pip3 install cherrypy
RUN pip3 install nltk
RUN pip3 install numpy
RUN pip3 install sklearn
RUN pip3 install cherrypy_cors

