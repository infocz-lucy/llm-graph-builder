from langchain_text_splitters import TokenTextSplitter
from langchain.docstore.document import Document
from langchain_community.graphs import Neo4jGraph
import logging
import os
from src.document_sources.youtube import get_chunks_with_timestamps

logging.basicConfig(format="%(asctime)s - %(message)s", level="INFO")


class CreateChunksofDocument:
    def __init__(self, pages: list[Document], graph: Neo4jGraph):
        self.pages = pages
        self.graph = graph

    def split_file_into_chunks(self):
        """
        문서 목록을 고정된 크기의 청크로 분할

        Args:
            pages: 분할할 페이지 목록입니다. 각 페이지는 텍스트 문자열의 목록입니다.

        Returns:
            각각 langchain Document인 청크의 목록입니다.         
        """
        logging.info("Split file into smaller chunks")
        # number_of_chunks_allowed = int(os.environ.get('NUMBER_OF_CHUNKS_ALLOWED'))
        text_splitter = TokenTextSplitter(chunk_size=200, chunk_overlap=20)
        if 'page' in self.pages[0].metadata:
            chunks = []
            for i, document in enumerate(self.pages):
                page_number = i + 1
                for chunk in text_splitter.split_documents([document]):
                    chunks.append(Document(page_content=chunk.page_content, metadata={'page_number':page_number}))    
        
        elif 'length' in self.pages[0].metadata:
            chunks_without_timestamps = text_splitter.split_documents(self.pages)
            chunks = get_chunks_with_timestamps(chunks_without_timestamps, self.pages[0].metadata['source'])
        else:
            chunks = text_splitter.split_documents(self.pages)
        return chunks