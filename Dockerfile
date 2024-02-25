FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
CMD ["python3", "calculator.py"]



