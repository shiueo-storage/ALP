import gradio as gr
import openai

openai.api_key = "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"


def generate_text_gpt(input_string, max_length):
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=input_string,
                                        temperature=0,
                                        max_tokens=max_length,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0)
    answer = response.choices[0]['text']
    return (answer)


def greet(name, max_e):
    result4 = generate_text_gpt(name, max_e)
    return result4


demo = gr.Interface(
    fn=greet,
    inputs=["text", gr.Slider(0, 100)],
    outputs=["text"],
)
demo.launch()
