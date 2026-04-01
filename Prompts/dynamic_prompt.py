from langchain_core.prompts import PromptTemplate


dynamic_prompt = PromptTemplate(
    template="Write a short Paragraph about {topic} in a {style}",
    input_variables=["topic","style"]
)

prompt_text = dynamic_prompt.format(topic="Manifestation",style="real incident")

print(prompt_text)