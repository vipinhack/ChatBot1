from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from langchain.document_loaders import GoogleDriveLoader
import os
os.environ['OPENAI_API_KEY'] = "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"
os.environ['SERPAPI_API_KEY'] = "87e0c15e92f885fc4af42b9bfcc163950f4f67be3f38f27c9eb212a1b2293fd1"


loader = GoogleDriveLoader(document_ids=["197HTcrNluCVH5bSrl5HzRZjWqeRtPavr9oinaS9r7tc"])


docs = loader.load()



