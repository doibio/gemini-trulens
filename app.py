import sys
import streamlit as st

from test_gemini import run_gemini
# Initialize an empty list to store the conversation
conversation = []

st.title("Chatbot")

# User input
user_input = st.text_input("You: ")
resp = ''

# Create a dropdown menu with options from 1 to 100
number = st.selectbox("Number of Abstracts to be Search", [i for i in range(1, 101)])

# Append user input to the conversation
if user_input:
    resp = run_gemini(user_input, number)
    conversation.append({"user": user_input})

# Simulate a response from another file
response = resp

# Append bot response to the conversation
conversation.append({"bot": response})

# Display the conversation
abstract_counter = 1  # Initialize the counter
for turn in conversation:
    if "user" in turn:
        st.write(f"You: {turn['user']}")
    elif "bot" in turn:
        # Use markdown to make the Bot text bigger
        st.markdown("## Bot")
        # Check if the bot response is a list
        if isinstance(turn['bot'], list):
            # Loop over the list of results
            for result in turn['bot']:
                # Split the result by newline
                parts = result.split("\n")
                # Get the PMID part and make it bold
                pmid = parts[0]
                st.write(f"**{pmid}**")
                # Get the abstract part and remove the unwanted characters
                abstract = parts[1]
                abstract = abstract.replace("\n", "").replace("{", "").replace("}", "").replace(":", "").replace("[", "").replace("]", "")
                # Create a subheader for the abstract
                st.subheader(str(abstract_counter) + ". Abstract")  # Add the counter to the subheader
                # Write the abstract text
                st.write(abstract)
                # Create a gap between each abstract
                st.empty()
                abstract_counter += 1  # Increment the counter
        else:
            # Handle the case when the bot response is not a list
            st.write(response)
