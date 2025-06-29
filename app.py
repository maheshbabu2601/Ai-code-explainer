!pip install --upgrade openai

import openai
from openai import OpenAI

client = OpenAI(api_key="your_api_key")  # Replace with your actual key

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, who won the World Cup in 2018?"}
    ]
)

print(response.choices[0].message.content)

import streamlit as st
import openai

st.set_page_config(page_title="AI Code Explainer", layout="centered")

# Title
st.title("🤖 AI Code Explainer")
st.write("Paste your code below and click **Explain** to understand what it does.")

# OpenAI API key input
api_key = st.text_input("🔑 Enter your OpenAI API key:", type="password")

# Language selector
language = st.selectbox("Select programming language:", ["Python", "JavaScript", "Java", "C++", "Other"])

# Code input box
code = st.text_area("📄 Paste your code here:", height=300)

# Button to trigger explanation
if st.button("🔍 Explain Code"):
    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not code.strip():
        st.error("Please paste some code.")
    else:
        with st.spinner("Generating explanation..."):
            try:
                openai.api_key = api_key

                prompt = f"Explain the following {language} code in detail with line-by-line comments and time/space complexity:\n\n{code}"

                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3,
                    max_tokens=1000
                )

                explanation = response["choices"][0]["message"]["content"]
                st.success("✅ Code Explanation:")
                st.markdown(f"```\n{explanation}\n```")
            except Exception as e:
                st.error(f"Error: {str(e)}")
