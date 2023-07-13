import speech_recognition as sr
from gtts import gTTS

class SpeechProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        # Create a temp file to store the audio
        audio_buffer = f"temp{hash(text)}.mp3"
        output = gTTS(text=text, slow = False)
        output.save(audio_buffer)
        # Reset the buffer to the beginning

        return audio_buffer

    def listen(self, audio_file):
        # Extract sample rate and sample width from the audio file
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)  # read the entire audio file
        try:
            text = self.recognizer.recognize_whisper(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError:
            return "Could not connect to the speech recognition service"
        
