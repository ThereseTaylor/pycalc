FROM python:3.x
WORKDIR /pycalc
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
ENTRYPOINT ["python3", "pycalc.py"]



