FROM registry.liquid.int.tdk.dk/base-tdc-images/python:v1
#RUN pip install bottle 
COPY app/ /app/
WORKDIR /app

EXPOSE 8080
CMD python code.py
