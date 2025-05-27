from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables=["product"]
)

prompt_json = prompt.save("prompt.json")

# ./prompt.json 파일 생성
# {
#     "input_variables": [
#         "product"
#     ],
#     "output_parser": null,
#     "partial_variables": {},
#     "template": "{product}\ub294 \uc5b4\ub290 \ud68c\uc0ac\uc5d0\uc11c \uac1c\ubc1c\ud55c \uc81c\ud488\uc778\uac00\uc694?",
#     "template_format": "f-string",
#     "validate_template": true,
#     "_type": "prompt"
# }