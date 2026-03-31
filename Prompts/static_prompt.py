from langchain_core.prompts import PromptTemplate


static_prompt = PromptTemplate(
    input_variables = [],
    template="I am placed with 44 lakh ctc "

)

prompt_text=static_prompt.format()
print(prompt_text)