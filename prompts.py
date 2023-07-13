# modified rag prompt for multilingual support
# see for original https://github.com/hwchase17/langchain/blob/master/langchain/chains/conversational_retrieval/prompts.py
from langchain.prompts.prompt import PromptTemplate

_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in the Follow Up Input language only.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Always answer the question in the language of the question.

{context}

Question: {question}
Helpful Answer:"""
rag_multilingual_prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
