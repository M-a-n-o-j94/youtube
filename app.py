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

# Configure API key for Google Generative AI
genai.configure(api_key=os.getenv("MANOJ_API_KEY"))

def youtube_trans(url):
    video_id = url.split("=")[1]
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
    return response

# Streamlit app structure
st.title("YOUTUBE VIDEO TO TEXT CONVERTER")
st.subheader("UPLOAD VIDEO URL")

youtube_link = st.text_input("Enter video URL")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg")

if st.button("SUBMIT"):
    transcript = youtube_trans(youtube_link)
    if transcript:
        summary = generate_transcript(transcript)
        st.markdown("Detailed Notes:")
        st.write(summary)
    else:
        st.error("Enter a valid URL")

    

    


