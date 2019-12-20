FROM python

COPY server.py server.py

CMD ["python", "server.py"]