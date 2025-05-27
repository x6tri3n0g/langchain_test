from langchain.prompts import load_prompt

prompt = load_prompt("prompt.json")

print(prompt.format(product="ChatGPT"))
print(prompt.format(product="아이폰"))

# ChatGPT는 어느 회사에서 개발한 제품인가요?
# 아이폰는 어느 회사에서 개발한 제품인가요?