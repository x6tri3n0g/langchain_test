import time
import langchain
from langchain.cache import InMemoryCache
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

langchain.llm_cache = InMemoryCache()

chat = ChatOpenAI()
start = time.time()
result = chat([
    HumanMessage(content="안녕하세요!"),
])

end = time.time()
print(result.content)
print(f"실행 시간: {end - start}초")

start = time.time()
result = chat([
    HumanMessage(content="안녕하세요!"),
])

end = time.time()
print(result.content)
print(f"실행 시간: {end - start}초")

# 안녕하세요! 무엇을 도와드릴까요? 😊
# 실행 시간: 1.118678092956543초
# 안녕하세요! 무엇을 도와드릴까요? 😊
# 실행 시간: 0.0006499290466308594초