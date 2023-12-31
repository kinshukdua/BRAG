# Brance Retrieval Augmented Generation (BRAG)

This project is a chatbot to interact with a given document i.e. a knowledge source and answer questions based on it.

## Core Features

- [x] Answer user questions from document - via LangChain and vectorDBs
- [x] Prevent hallucination - via prompt engineering and answer evaluation

## Additional Features (WIP)
- [x] Evaluation of the answers - via RAGAS
- [x] Multi-lingual support - via OpenAI/Llama, speech and prompt support
- [x] Speech Compatibility (TtS and StT) - via OpenAI Whisper (offline) and gTTS
- [x] Basic GUI - Barebones HTML (only for testing)

## Architecture
![BRAG Architecture](https://github.com/kinshukdua/BRAG/blob/main/writeup/architecture.png?raw=true)

## Installation

Will be replaced with DOCKERFILE and requirements.txt

```python
pip -r requirements.txt
```

```python
python app.py
```

## Algorithm

1. Store Documents
2. Split documents into chunks
3. Process chunks as embeddings
4. Save embeddings in vector DB
5. Initialize Chat history
6. Take input via SpeechRecognition (Whisper API/Offline)
7. Convert input to embeddings
8. Use similarity search to get relevant chunks
9. Add relevant chunks to context in prompt 
10. Send prompt and history to LLM
11. Get result
12. Get metrics via RAGAS
13. Show output to user (via TTS)
14. Append output to chat history
15. Repeat 6-14

