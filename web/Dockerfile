FROM python:3
WORKDIR /home/anand/learning_curve
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "app.py" ]
