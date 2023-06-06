FROM python:3.7
COPY . /app
WORKDIR /app
EXPOSE 8000
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]