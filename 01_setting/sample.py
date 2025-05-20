import json
import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "냉면의 원재료를 알려줘"
        },
    ],
    max_tokens=100,  # 생성할 문장의 최대 토큰 수
    temperature=1,  # 생성할 문장의 다양성을 나타내는 매개변수
    n=2,            # 생성할 문장 수
)

print(json.dumps(response, indent=2, ensure_ascii=False))

# {
#   "id": "chatcmpl-BZJxIoSEdOF8DVFOwvc0MCcZVOi5W",
#   "object": "chat.completion",
#   "created": 1747757888,
#   "model": "gpt-3.5-turbo-0125",
#   "choices": [
#     {
#       "index": 0,
#       "message": {
#         "role": "assistant",
#         "content": "냉면의 주요 원재료는 밀가루, 전분, 물, 소금입니다. 그리고 냉면 국물을 만들 때는 다양한 재료를 사용할 수 있지만, 보통은 다시고추장, 간장, 설탕, 식초, 참기름, 소금 등을",
#         "refusal": null,
#         "annotations": []
#       },
#       "logprobs": null,
#       "finish_reason": "length"
#     },
#     {
#       "index": 1,
#       "message": {
#         "role": "assistant",
#         "content": "냉면의 주요 원재료는 밀가루를 사용한 면과 육수, 양파, 오이, 김가루, 고추장, 설탕, 식초, 소금 등이 있습니다. 맛과 풍미를 높이기 위해 무, 참나물, 단무지, 양",
#         "refusal": null,
#         "annotations": []
#       },
#       "logprobs": null,
#       "finish_reason": "length"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 23,
#     "completion_tokens": 200,
#     "total_tokens": 223,
#     "prompt_tokens_details": {
#       "cached_tokens": 0,
#       "audio_tokens": 0
#     },
#     "completion_tokens_details": {
#       "reasoning_tokens": 0,
#       "audio_tokens": 0,
#       "accepted_prediction_tokens": 0,
#       "rejected_prediction_tokens": 0
#     }
#   },
#   "service_tier": "default",
#   "system_fingerprint": null
# }