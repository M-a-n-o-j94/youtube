import streamlit as st 
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

import google.generativeai  as genai 
import os
from youtube_transcript_api import YouTubeTranscriptApi 
# from the public video url it transcibes the entire video



genai.configure(api_key=os.getenv ("Manoj-Api-Key"))

import streamlit as st 
from dotenv import load_dotenv
import google.generativeai  as genai 
import os
from youtube_transcript_api import YouTubeTranscriptApi 

# Load environment variables
load_dotenv() 
google_api=os.getenv("Manoj-Api-Key")
# Configure API key for Google Generative AI
genai.configure(api_key=google_api)

def youtube_trans(youtube_link):
    video_id = youtube_link.split("=")[1]
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for i in transcript_text:
        result += i['text'] + " "
    return result

def generate_transcript(transcript):  # Transcript to summary
    prompt = f'''You are a YouTube video summarizer.
    The transcript passed is: {transcript}.
    Analyze the entire video and provide
    a summary in point form.'''
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


# Custom CSS for background color and text style
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            transition-duration: 0.4s;
            border-radius: 12px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .header-text {
            color: #4a4a4a;
            font-size: 28px;
            font-weight: bold;
        }
        .summary-box {
            background-color: #fff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .summary-box {
            animation: fadeIn 2s ease;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app structure
st.title("YOUTUBE VIDEO TO TEXT CONVERTER")
st.subheader("UPLOAD VIDEO URL")

youtube_link = st.text_input("Enter video URL")
# Import PIL to handle local image files
from PIL import Image
# Open and display the image
if youtube_link:
    image = Image.open(r"C:\Users\Manoj bhyravajosula\Downloads\maxresdefault.jpg")
    st.image(image, caption="Local Image", use_column_width=True)



if st.button("SUBMIT"):
    with st.spinner("Transcribing and generating summary..."):
        transcript = youtube_trans(youtube_link)
        if transcript:
            result = generate_transcript(transcript)
            st.markdown("<div class='summary-box'><strong>Detailed Notes:</strong></div>", unsafe_allow_html=True)
            st.write(result)
        else:
            st.error("Enter a valid URL")




image = Image.open(r"C:\Users\Manoj bhyravajosula\Downloads\future-artificial-intelligence-robot-network-system-background_432372-88.avif")
st.image(image, caption="Local Image", use_column_width=True)

    


