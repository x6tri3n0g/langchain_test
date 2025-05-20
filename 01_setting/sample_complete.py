import json
import openai

response = openai.Completion.create(    # Completion 사용
    engine="gpt-3.5-turbo-instruct",    # engine을 지정하고 gpt-3.5-turbo-instruct를 지정
    prompt="오늘 날씨가 매우 좋고 기분이",
    stop=".",                           # 문자가 나타나면 문장 종료
    max_tokens=100,                     # 최대 토큰 수
    n=2,                                # 생성할 문장 수
    temperature=0.5,                    # 다양성을 나타내는 매개변수
)

print(json.dumps(response, indent=2, ensure_ascii=False))

# {
#   "id": "cmpl-BZK6e5ZvLgjvCipIQexT21w2kMZki",
#   "object": "text_completion",
#   "created": 1747758468,
#   "model": "gpt-3.5-turbo-instruct:20230824-v2",
#   "choices": [
#     {
#       "text": " 좋습니다",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "stop"
#     },
#     {
#       "text": " 좋습니다",
#       "index": 1,
#       "logprobs": null,
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 18,
#     "completion_tokens": 6,
#     "total_tokens": 24
#   }
# }