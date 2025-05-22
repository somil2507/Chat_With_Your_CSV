import streamlit as st
import pandas as pd
from pandasai.llm.local_llm import LocalLLM
from pandasai import SmartDataframe

def chat_with_csv(df, query):
    try:
        llm = LocalLLM(
            api_base="http://localhost:11434/v1",
            model="phi"  # You can try 'phi', 'llama2:7b', 'llama3', or 'codellama:7b-python'
        )

        pandas_ai = SmartDataframe(df, config={
            "llm": llm,
            "enable_cache": False,
            "verbose": True
        })

        response = pandas_ai.chat(query)
        print("LLM Response:", response)
        return response

    except Exception as e:
        return f"An error occurred: {e}"


st.set_page_config(layout='wide')
st.title("Welcoming You To Chat With Your CSV")

input_csvs = st.sidebar.file_uploader("Upload your CSV file(s)", type=['csv'], accept_multiple_files=True)

if input_csvs:
    selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)

    st.info("CSV uploaded successfully")
    data = pd.read_csv(input_csvs[selected_index])
    st.dataframe(data.head(3), use_container_width=True)

    st.info("Chat Below")
    input_text = st.text_area("Enter your query about the data")

    if input_text:
        if st.button("Chat with CSV"):
            st.info("Your Query: " + input_text)
            result = chat_with_csv(data, input_text)
            st.success(result)