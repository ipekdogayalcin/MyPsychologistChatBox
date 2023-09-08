import openai
import gradio
import time

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a psychologist"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = None

    while response is None or 'choices' not in response:
        time.sleep(2)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="My Psychologist")

demo.launch(share=True)
