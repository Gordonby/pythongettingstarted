FROM python:3.8-slim-buster  

COPY . /app
WORKDIR /app

RUN echo $'python -V'
RUN echo $'pip -V'

RUN pip install -r requirements.txt

EXPOSE 5001 

ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 
