from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables=["product"]
)

result = chat(
    [
        HumanMessage(content=prompt.format(product="ChatGPT"))
    ]
)

print(result.content)

# ChatGPT는 OpenAI에서 개발한 제품입니다. OpenAI는 인공지능 연구 및 개발을 진행하는 기업으로, ChatGPT는 그들이 개발한 대화형 인공지능 모델 중 하나입니다.