from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    streaming=True,
    callbacks=[
        StreamingStdOutCallbackHandler(),
    ]
)

response = chat([
    HumanMessage(content="맛있는 스테크 굽는 법을 알려주세요"),
])

# 아래 내용이 streaming으로 출력됨
# 1. 스테이크를 냉장고에서 꺼내어 냉동 해동시킨다. 미리 해동시키지 않으면 스테이크가 고르게 익지 않을 수 있으니 주의해야 한다.
# 2. 팬을 중불로 예열한다. 팬을 예열할 때 식용유를 적당히 두르고 팬을 예열하면 고기가 덜 붙어 익게 된다.
# 3. 스테이크에 소금과 후추를 고루 뿌려준다. 소금과 후추는 고기의 맛을 더해주는 중요한 재료이다.
# 4. 팬에 스테이크를 넣고 한쪽 면을 2~3분 정도씩 익힌다. 한쪽 면이 익었을 때는 뒤집어서 다른 한쪽도 익힌다.
# 5. 스테이크를 뒤집을 때는 뒤집는 동작을 조심해야 한다. 갑자기 뒤집으면 고기의 수분이 증발하여 건조해질 수 있다.
# 6. 고기가 익은 정도는 고객의 취향에 따라 익히면 된다. 레어, 미디움, 웰던 등 다양한 익힘 정도가 있으니 원하는 정도로 익혀서 차례를 즐기면 된다.
# 7. 스테이크를 접시에 담아 1~2분 정도 쉬게 한 뒤 서빙하면 된다. 고기가 쉬면서 내부 열이 고르게 퍼지기 때문에 더 맛있게 먹을 수 있다.
# 이렇게하여 맛있는 스테이크를 굽는 법을 알려드렸습니다. 맛있는 식사 되시길 바랍니다!% 