# Latest Football Fixtures App Using a SportMonk API and RAG Pipeline

## Introduction
This project is designed to provide the latest football fixtures using the SportMonk API. The app is built using a Retrieval-Augmented Generation (RAG) pipeline to enhance data retrieval and presentation.

## Features
- Fetches latest football fixtures from SportMonk API
- Utilizes RAG pipeline for data retrieval and presentation

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have a working internet connection.
- You have `Python` installed on your machine.
-  Have docker installed
## steps to use the app
First clone the repository
```bash
git clone [https://github.com/pathwaycom/llm-app.git](https://github.com/AmanTomy/App.git)
```
Second make an image of the rep in Docker and then run it
```bash
docker build -t football/rag .
```
```bash
docker run -v "$(pwd)/data:/app/data" -p 8000:8000 --env-file .env football/rag
```
Next make write a prompt in the prompt section based on the latest football fixtures and who won.
```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/v1/pw_ai_answer' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Your prompt"
}'
```
