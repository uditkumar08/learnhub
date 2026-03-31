# LearnHub Project

## 1) Goal
- This project is a simple script to print a prompt text.
- Objective: learn sequence-wise execution and maintain a clear README with a small joke.

## 2) Folder Structure
- `BasicLLM/`: basic LLM modules
- `Prompts/static_prompt.py`: main demo script
- `requirements.txt`: dependencies

## 3) Setup 🚀
1. Create a virtual environment:
   - Windows:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 4) Run 🏃
1. Run the prompt script:
   ```bash
   python Prompts/static_prompt.py
   ```
2. Expected output:
   ```text
   I am placed with 44 lakh ctc
   ```

## 5) Example: change prompt text
- Edit the template text in `Prompts/static_prompt.py` or run this snippet:
  ```python
  from langchain_core.prompts import PromptTemplate

  static_prompt = PromptTemplate(
      input_variables=[],
      template="My package is 44 lakh CTC"
  )

  prompt_text = static_prompt.format()
  print(prompt_text)
  ```
- Then run:
  ```bash
  python Prompts/static_prompt.py
  ```
- Output:
  ```text
  My package is 44 lakh CTC
  ```
- Light joke line (one small Hindi English mix):
  - "Code runs then I celebrate; otherwise I print debug और फिर सोचता हूँ 😂"

## 6) Funny Meme 😄
> Sometimes coding feels exactly like this:

![Funny Meme](https://i.imgflip.com/4/4t0m5.jpg)

(If this URL is blocked, you can use a local meme image instead.)

## 7) Tips 💡
- Make the prompt dynamic by adding `input_variables`.
- Add step-by-step instructions in this README so your team can follow easily.

