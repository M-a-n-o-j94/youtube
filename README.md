<img width="608" alt="image" src="https://github.com/user-attachments/assets/a00ce9c6-385b-42bf-a224-0920563c6828">

🎥 YouTube Video to Text Converter: AI-Powered Summarizer 🚀
Convert any YouTube video into easy-to-read text and summaries with this AI-powered web app. The app extracts transcripts from public YouTube videos and uses Google Generative AI (Gemini API) to summarize the content into concise points. It's simple, fast, and efficient — making video content more accessible and easy to digest!
🌟 Key Features
🎬 YouTube Transcript Extraction: Fetch complete transcripts from any public YouTube video with the click of a button.
💡 AI-Powered Summarization: Leverage Google's Generative AI to turn long video transcripts into succinct, actionable summaries.
🚀 User-Friendly Interface: Built using Streamlit, the app offers an intuitive interface for seamless user experience.


🎨 Custom Design: Enjoy a clean and modern look with customized CSS for styling.
1. Environment Setup
We load sensitive information like API keys using .env files to keep the project secure.
2. YouTube Transcript Extraction
The YouTubeTranscriptApi library is used to fetch the transcript by simply passing the YouTube video URL. The video ID is extracted, and the transcript is fetched and formatted as a single string.
3. AI-Powered Summarization
The Generative AI (Gemini API) from Google is used to process the transcript and summarize the content into concise points.
4. Interactive User Interface
Built using Streamlit, users can easily input the video URL, fetch the transcript, and generate a summary.


🎨 Custom Styling with CSS
To make the app visually appealing, we added some custom CSS for styling buttons, background colors, and summary display boxes. This makes the UI clean and modern.

🌐 Future Enhancements
Video Embedding: Allow users to play videos directly within the app.
Multi-language Support: Extend transcript extraction and summarization to support multiple languages.
Downloadable Summaries: Add an option to download the generated summaries as text files or PDFs.

👨‍💻 Contributing
Feel free to fork this repository, make your changes, and submit a pull request. Let’s make video content more accessible together!


🎥 Demo
Check out the live demo hosted on Streamlit Share: YouTube to Text Converter Demo
🤝 Acknowledgments
Special thanks to the following resources that made this project possible:

Streamlit - For providing an amazing web app framework.
Google Generative AI - For powerful AI-based summarization.
YouTubeTranscriptApi - For seamless YouTube transcript extraction.
