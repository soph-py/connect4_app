FROM python:3.10
COPY . /Connect4_app
RUN make /Connect4_app
CMD ["python", "Connect4_app/main.py", "Connect4_app/config_files/connect4.txt"]