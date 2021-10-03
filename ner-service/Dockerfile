###############################################
# Base Image
###############################################
FROM python:3.9.7 as python-base
RUN pip3 install spacy fastapi uvicorn
RUN python -m spacy download en_core_web_sm
#WORKDIR /usr/src/app
COPY ./src /src/
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]


# docker rm ner-service
# docker rmi ner-service
# docker build -t ner-service .
# docker run --name ner-service -it ner-service
# docker start ner-service