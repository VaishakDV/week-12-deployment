# Week 12 - India Knowledge Assistant (Deployed)

A live AI chatbot about Indian geography, culture, history,
and current affairs. Deployed on Hugging Face Spaces.

## Live Demo
https://huggingface.co/spaces/Vaishak27/India-knowledge-assistant

## What it does
- Answers questions about Indian geography, culture, and history
- Maintains conversation memory across the session
- Includes clickable example prompts
- Powered by Claude Haiku via Anthropic API

## What I learned
- Gradio — building web UIs for AI apps in Python
- Hugging Face Spaces — free deployment with public URL
- Managing secrets safely in deployed apps
- Git remotes — pushing to multiple repositories
- requirements.txt for cloud deployment
- Difference between local prototype and deployed product

## Tech Stack
- Claude Haiku (Anthropic API)
- Gradio (web interface)
- Hugging Face Spaces (free hosting)

## How to run locally
1. Clone the repo
2. Create virtual environment and activate it
3. pip install anthropic gradio python-dotenv
4. Create .env with your ANTHROPIC_API_KEY
5. python app.py
6. Open http://127.0.0.1:7860
