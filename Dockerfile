FROM python

WORKDIR /app

RUN pip install aiogram

COPY . .

CMD ["python", "bot_xs.py"]