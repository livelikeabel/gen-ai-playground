from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

load_dotenv()

llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'), temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
chain = LLMChain(llm=llm, prompt=prompt)

res = chain.run("colorful socks")
print(res)
