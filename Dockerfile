FROM python:latest
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 3000
ENTRYPOINT ["python"]
CMD ["src/app.py"]