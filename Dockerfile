FROM python:3.11-slim
WORKDIR /app
COPY server.py .
RUN pip install mcp fastmcp mysql-connector-python
CMD ["python", "server.py"]
