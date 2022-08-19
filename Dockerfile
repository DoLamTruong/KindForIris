FROM python:3.7-slim-buster
COPY app.py app.py
COPY requierment.txt requierment.txt
COPY iris.mdl iris.mdl
RUN python3 -m pip install -r requierment.txt
EXPOSE 1080
CMD [ "python", "app.py" ]
