import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader #,PyPDFium2Loader commenting for future
from langchain.chains.question_answering import load_qa_chain
from integrations import llm, embeddings

class TextQuery:
    def __init__(self, file_path) -> None:
        self.embeddings = embeddings
        # I prefer MarkdownHeaderTextSplitter over RecursiveCharacterTextSplitter
        #self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50,separators=["#", "##", "###","\n\n", "\n", "(?<=\. )", " ", ""])
        self.text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on =
                                                        [
                                                            ("#", "Header 1"),
                                                            ("##", "Header 2"),
                                                            ("###", "Header 3"),
                                                        ])
        self.llm = llm
        self.chain = None
        self.db = None

    def ask(self, question: str) -> str:
        if self.chain is None:
            response = "Please, add a document."
        else:
            docs = self.db.get_relevant_documents(question)
            response = self.chain.run(input_documents=docs, question=question)
        return response

    def ingest(self, file_path: os.PathLike) -> None:
        loader = TextLoader(file_path)
        documents = loader.load()
        splitted_documents = self.text_splitter.split_text(documents.page_content)
        self.db = Chroma.from_documents(splitted_documents, self.embeddings).as_retriever()
        self.chain = load_qa_chain(self.llm, chain_type="stuff")

    def forget(self) -> None:
        self.db = None
        self.chain = None
