import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Custom CSS styles
st.markdown(
    f"""
    <style>
    body {{
        background-color: #f5f5f5; /* Light Grey */
        font-family: Arial, sans-serif;
    }}
    .stTextInput input {{
        background-color: #ffffff; /* White */
        color: #000000; /* Black */
        border: 2px solid #cccccc; /* Light Grey */
        border-radius: 5px;
        padding: 10px;
    }}
    .stTextInput label {{
        color: #000000; /* Black */
    }}
    .stButton button {{
        background-color: #008CBA; /* Dark Blue */
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
    }}
    .stSuccess {{
        background-color: #4CAF50; /* Green */
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px;
    }}
    .stWarning {{
        background-color: #FF5722; /* Orange */
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# Application Title
st.title("Text Similarity Calculator")

# Text Input
text1 = st.text_area("Enter Text 1:", "", key="text1")
text2 = st.text_area("Enter Text 2:", "", key="text2")

# Text Cleaning Function
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    return text

if st.button("Calculate Similarity"):
    if not text1 or not text2:
        st.warning("Please enter both texts.")
    else:
        # Clean the text
        text1 = clean_text(text1)
        text2 = clean_text(text2)

        # Create TF-IDF vectors
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([text1, text2])

        # Calculate Cosine Similarity
        cosine_sim = (cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0])*100

        # Show Result
        st.success(f"Similarity between texts: {cosine_sim:.2f}%")



