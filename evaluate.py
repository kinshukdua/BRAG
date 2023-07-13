from ragas import evaluate
from ragas.metrics import context_relevancy, answer_relevancy
from datasets import Dataset

def evaluate_rag(question, answer, source):
    data = Dataset.from_dict({"question":[question],"answer":[answer], "contexts":[source]})
    scores = evaluate(data, metrics=[context_relevancy, answer_relevancy])
    ctx_score = scores['context_relavency']
    ans_score = scores['answer_relevancy']
    return ctx_score, ans_score