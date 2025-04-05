import gradio as gr
import whisper
import subprocess
import os

def check_dependencies():
    """Check if ffmpeg is available"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def transcribe_audio(audio_file):
    """Transcribe audio file using Whisper"""
    if not check_dependencies():
        return "Error: ffmpeg not found. Please install ffmpeg and add it to PATH"
    
    if not os.path.exists(audio_file):
        return "Error: Audio file not found"
        
    try:
        # Load the Whisper model
        model = whisper.load_model("base")
        
        # Perform transcription
        result = model.transcribe(audio_file)
        
        if not result or "text" not in result:
            return "Error: Transcription failed to produce output"
            
        return result["text"]
        
    except Exception as e:
        return f"Transcription error: {str(e)}"

def create_interface():
    """Create the Gradio interface"""
    audio_input = gr.Audio(
        sources=["upload", "microphone"],
        type="filepath",
        label="Upload or Record Audio"
    )
    
    output_text = gr.Textbox(
        label="Transcription Output",
        placeholder="Transcription will appear here..."
    )
    
    return gr.Interface(
        fn=transcribe_audio,
        inputs=audio_input,
        outputs=output_text,
        title="Audio Transcription App",
        description="Upload an audio file or record audio to transcribe",
        cache_examples=False
    )

def main():
    if not check_dependencies():
        print("Warning: ffmpeg not found. Please install ffmpeg for audio processing.")
    
    interface = create_interface()
    interface.launch(share=False)

if __name__ == "__main__":
    main()