import gradio as gr
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

conversation_history = []


def chat(user_message, history):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        system="""You are a helpful AI assistant with expertise in 
Indian geography, culture, history, and current affairs. 
Answer questions clearly and accurately.""",
        messages=conversation_history
    )

    assistant_message = response.content[0].text

    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


demo = gr.ChatInterface(
    fn=chat,
    title="India Knowledge Assistant",
    description="Ask me anything about Indian geography, culture, history, and current affairs.",
    examples=[
        "What is the significance of the Ganges river?",
        "Tell me about the Taj Mahal.",
        "What are the major classical dance forms of India?",
        "Explain the significance of Diwali.",
    ],
)

if __name__ == "__main__":
    demo.launch()