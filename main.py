import streamlit as st
import pandas as pd
import ast  # For literal_eval

# Load the CSV file from the correct path
csv_path = "D:/New folder/New folder (2)/final_file.csv"
df = pd.read_csv(csv_path)


# Function to transform short_answer column
def transform_short_answer(short_answer):
    try:
        short_answer_list = ast.literal_eval(short_answer)
        if not short_answer_list:  # If the list is empty, return "none"
            return "none"
        return ', '.join([f"short_answer{i + 1}" for i in range(len(short_answer_list))])
    except (SyntaxError, ValueError):
        return short_answer


# Sidebar filter options
filter_yes_no_none = st.sidebar.selectbox("Filter by Yes/No/None", ["All", "YES", "NO", "NONE"])

# Apply filters
filtered_df = df.copy()
if filter_yes_no_none != "All":
    filtered_df = filtered_df[filtered_df['yes_no_answer'] == filter_yes_no_none]

# Display the entire dataset with transformed short answer column
st.title("CSV Data Explorer")
df['short_answer_display'] = df['short_answer'].apply(transform_short_answer)
st.dataframe(df[['document_title', 'question_text', 'short_answer_display', 'yes_no_answer']])

# Sidebar filter for Document Title (applies to the Filtered Dataset)
filter_document_title = st.sidebar.selectbox("Filter by Document Title",
                                             ["All"] + list(filtered_df['document_title'].unique()))
if filter_document_title != "All":
    filtered_df = filtered_df[filtered_df['document_title'] == filter_document_title]

# Create a new column for the transformed short answer in the filtered dataset
filtered_df['short_answer_display'] = filtered_df['short_answer'].apply(transform_short_answer)

# Display the Filtered Dataset with question_text column included
st.title("Filtered Dataset")
st.dataframe(filtered_df[['document_title', 'question_text', 'short_answer_display', 'yes_no_answer']])
