from langchain.llms import OpenAI
llm = OpenAI(openai_api_key="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", temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))
