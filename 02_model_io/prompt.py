from langchain import PromptTemplate

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables=["product"]
)

print(prompt.format(product="ChatGPT"))
print(prompt.format(product="아이폰"))

# ChatGPT는 어느 회사에서 개발한 제품인가요?
# 아이폰는 어느 회사에서 개발한 제품인가요?