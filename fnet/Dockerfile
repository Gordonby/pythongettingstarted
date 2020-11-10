#FROM python:3.8-slim-buster  
FROM mcr.microsoft.com/azureml/base-gpu:intelmpi2018.3-cuda10.0-cudnn7-ubuntu16.04

COPY . /app
WORKDIR /app

RUN echo $'python -V'
RUN echo $'pip -V'


RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip --use-feature=2020-resolver install  git+https://github.com/AllenCellModeling/pytorch_fnet.git --ignore-installed certifi

EXPOSE 5001 

ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 
