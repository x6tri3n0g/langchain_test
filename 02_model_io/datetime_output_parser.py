from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser

from langchain.schema import HumanMessage

output_parser = DatetimeOutputParser()

chat = ChatOpenAI(model="gpt-3.5-turbo",)

prompt = PromptTemplate.from_template("{product}의 출시일을 알려주세요. {format_instructions}")

formatted_prompt = prompt.format(
    product="iPhone8",
    format_instructions=output_parser.get_format_instructions()
)

result = chat(
    [
        HumanMessage(content=formatted_prompt),
    ]
)

output = output_parser.parse(result.content)

print(output)

# 2017-09-22 08:00:00