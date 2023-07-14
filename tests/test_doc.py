from docquery import TextQuery
import tempfile

def test_rag():
    with tempfile.NamedTemporaryFile() as temp:
        text = "The capital of XYZ is ABC\n"
        temp.write(text)
        rag = TextQuery()
        rag.ingest(temp.name)
        answer = rag.ask("What is the capital of XYZ?")['answer']
        assert "ABC" in answer
