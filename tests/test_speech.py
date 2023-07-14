from speech import SpeechProcessor
import filecmp

def test_speech():
    engine = SpeechProcessor()
    text = "What is PAN?"
    file1 = engine.speak(text)
    assert filecmp.cmp(file1, "speech_test.mp3")

def test_speech_multilang():
    engine = SpeechProcessor()
    text = "PAN क्या है?"
    file1 = engine.speak(text)
    assert filecmp.cmp(file1, "speech_multilang_test.mp3")

def test_listen():
    engine = SpeechProcessor()
    detected_text = engine.listen("speech_test.mp3")
    assert "what is pan" in detected_text.lower()

def test_listen_multilang():
    engine = SpeechProcessor()
    detected_text = engine.listen("speech_multilang_test.mp3")
    assert "क्या है" in detected_text.lower()

