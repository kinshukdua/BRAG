from flask import Flask, request, jsonify, send_file, render_template
import os
from docquery import TextQuery
from speech import SpeechProcessor
from evaluate import evaluate_rag

app = Flask(__name__)
uploaded_file = None

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_file
    print(request)
    file = request.files['file']
    if file:
        file.save(f"{file.filename}")
        uploaded_file = f"{file.filename}"
        rag.ingest(uploaded_file)
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error'})

@app.route('/chat', methods=['POST'])
def chat():
    if uploaded_file:
        # Process chat request and generate response
        user_question = request.json['input']
        answer, source = rag.ask(user_question)
        ctx_score, ans_score = evaluate_rag(user_question, answer, source)
        # Perform chatbot logic and generate response_text
        return jsonify({'response': answer,"context_score":ctx_score,"answer_score":ans_score})
    else:
        return jsonify({'status': 'error', 'message': 'File not uploaded'})

@app.route('/chat-voice', methods=['POST'])
def chat_voice():
    audio_file = request.files['audio_files']
    if uploaded_file:
        audio_file.save(f"{audio_file.filename}")
        parsed_question = speech_engine.listen(audio_file.filename)
        answer, source = rag.ask(parsed_question)
        response_file = speech_engine.speak(answer)
        response_file = 'response_audio.mp3'
        return send_file(response_file, mimetype='audio/mpeg')
    else:
        return jsonify({'status': 'error', 'message': 'Something went wrong with the speech engine'})

@app.route('/delete', methods=['POST'])
def delete_file():
    global uploaded_file

    if uploaded_file:
        # Delete the uploaded file
        os.remove(uploaded_file)
        # remove conversations
        rag.forget()
        uploaded_file = None
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error', 'message': 'File not found'})

if __name__ == '__main__':
    speech_engine = SpeechProcessor()
    rag = TextQuery()
    app.run()
