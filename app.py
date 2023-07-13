from flask import Flask, request, jsonify, send_file, render_template
import os

app = Flask(__name__)
uploaded_file = None

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_file
    file = request.files['file']
    if file:
        file.save(f"/uploads/{file.filename}")
        uploaded_file = f"/uploads/{file.filename}"
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error'})

@app.route('/chat', methods=['POST'])
def chat():
    if uploaded_file:
        # Process chat request and generate response
        user_input = request.json['input']
        # Perform chatbot logic and generate response_text
        response_text = 'This is a dummy response.'

        return jsonify({'response': response_text})
    else:
        return jsonify({'status': 'error', 'message': 'File not uploaded'})

@app.route('/chat-voice', methods=['POST'])
def chat_voice():
    if uploaded_file:
        # Process voice input and generate audio response
        # Placeholder for processing audio and generating audio response
        # response_audio = process_voice(request.audio)

        # Assuming the generated audio response is stored as a file
        response_audio_file = 'response_audio.mp3'

        return send_file(response_audio_file, mimetype='audio/mpeg')
    else:
        return jsonify({'status': 'error', 'message': 'File not uploaded'})

@app.route('/delete', methods=['POST'])
def delete_file():
    global uploaded_file

    if uploaded_file:
        # Delete the uploaded file
        os.remove(uploaded_file)
        uploaded_file = None
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error', 'message': 'File not found'})

if __name__ == '__main__':
    app.run()