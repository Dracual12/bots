FROM python

WORKDIR /app

RUN pip install Pillow

RUN pip install aiogram

RUN pip install torchvision

RUN pip install translate


COPY . .

CMD ["python", "main.py"]