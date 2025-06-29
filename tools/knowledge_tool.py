from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.tools import Tool

# 简化示例，不包含文档加载部分
def doc_qa(query):
    return "这是对文档的模拟回答：" + query

knowledge_tool = Tool(
    name="KnowledgeBaseTool",
    func=doc_qa,
    description="根据上传文档进行问答。例如：'解释Transformer原理'"
)