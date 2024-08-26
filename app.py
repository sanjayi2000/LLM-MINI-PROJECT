import streamlit as st
from groq import Groq

# Initialize Groq client with your API key
api_key = "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"
client = Groq(api_key=api_key)

# Function to get a writing prompt from Groq API
def get_writing_prompt(client, genre, length, prompt_type):
    """
    Generate a writing prompt based on user preferences using Groq API.
    
    Args:
    - genre (str): The genre of the writing prompt.
    - length (str): The desired length of the prompt.
    - prompt_type (str): The type of writing prompt.
    
    Returns:
    - str: The generated writing prompt or error message.
    """
    # Prepare messages for the API based on user input
    messages = [
        {"role": "system", "content": "You are a writing prompt generator."},
        {"role": "user", "content": f"Generate a {length} {genre} prompt of type {prompt_type}."}
    ]
    
    try:
        # Call the Groq API to get a response
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192", 
            temperature=1, 
            max_tokens=2048, 
            top_p=1, 
            stop=None,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI
st.set_page_config(
    page_title="Daily Writing Prompts Generator",
    page_icon=":pencil:",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("Daily Writing Prompts Generator")
st.write("Select your preferences below to generate a daily writing prompt.")

# Sidebar for user input
with st.sidebar:
    genre = st.selectbox("Genre", ["Fantasy", "Science Fiction", "Romance", "Mystery", "Poetry", "Non-fiction"])
    length = st.selectbox("Length", ["Short", "Medium", "Long"])
    prompt_type = st.selectbox("Type of Prompt", ["Story Starter", "Personal Reflection", "Poetic Line"])

# Button to generate a prompt
if st.button("Generate Prompt"):
    prompt = get_writing_prompt(client, genre, length, prompt_type)
    st.write("### Your Writing Prompt:")
    st.write(prompt)

    # Option to save the prompt
    if st.button("Save Prompt"):
        with open("prompts.txt", "a") as f:
            f.write(f"{prompt}\n")
        st.success("Prompt saved successfully!")

