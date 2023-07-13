import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader #,PyPDFium2Loader commenting for future
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from integrations import llm, embeddings
from prompts import rag_multilingual_prompt

class TextQuery:
    def __init__(self) -> None:
        self.embeddings = embeddings
        # I prefer MarkdownHeaderTextSplitter over RecursiveCharacterTextSplitter
        # self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50,separators=["#", "##", "###","\n\n", "\n", "(?<=\. )", " ", ""])
        self.text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on =
                                                        [
                                                            ("#", "Header 1"),
                                                            ("##", "Header 2"),
                                                            ("###", "Header 3"),
                                                        ])
        self.llm = llm
        self.rag = None
        self.db = None
        # Can be saved for restarting
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.history = []

    def ask(self, question: str) -> str:
        if self.rag is None:
            response = "Please, add a document."
        else:
            result = self.rag({"question": question, "chat_history": self.history})
            response = result["answer"]
            self.history.append((question, response))
            
        return response

    def ingest(self, file_path: os.PathLike) -> None:
        loader = TextLoader(file_path)
        documents = loader.load()
        splitted_documents = self.text_splitter.split_text(documents.page_content)
        self.db = Chroma.from_documents(splitted_documents, self.embeddings).as_retriever()
        self.rag = ConversationalRetrievalChain.from_llm(self.llm,self.db,self.memory,combine_docs_chain_kwargs={'prompt': rag_multilingual_prompt})

    def forget(self) -> None:
        self.db = None
        self.rag = None
