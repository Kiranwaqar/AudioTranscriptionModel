# Audio Transcription Project

This project uses OpenAI's Whisper model to transcribe audio files. It provides a simple interface where users can upload or record audio to get the transcription. The application is built using Python with the Gradio library for the user interface and Whisper for audio transcription.

## Features
- Upload or record audio to transcribe
- Real-time transcription using Whisper
- Error handling for missing dependencies like ffmpeg
- Simple and intuitive user interface built with Gradio

## Installation

To run this project locally, follow the steps below:

### 1. Clone the Repository

git clone https://github.com/Kiranwaqar/AudioTranscriptionModel.git

### 2. Create a Virtual Environment (Optional but Recommended)

python -m venv env
venv\Scripts\activate

### 3. Install Dependencies

Install the required Python packages:

pip install -r requirements.txt

### 4. Run the Application
After installing the dependencies, run the application using the following command:

python audiotranscript.py

This will launch a Gradio interface in your browser where you can upload or record audio and view the transcription. 
