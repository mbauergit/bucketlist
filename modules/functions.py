import instaloader
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment

# Download video from instagram post
def download_instagram_video(video_url):
    L = instaloader.Instaloader()
    shortcode = video_url.split("/")[-2]  # Extract shortcode from the URL
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    L.download_post(post, target="downloads")  # Downloads to 'downloads' folder
    video_file = 'downloads/' + video_url.split("/")[-2] + '.mp4'
    return video_file

# Extract audio from the video if possible
def extract_audio(video_file):
    video = VideoFileClip(video_file)
    audio_file = video_file.replace('.mp4', '.mp3')  # Change the extension to mp3
    video.audio.write_audiofile(audio_file)
    return audio_file

def transcribe_audio(audio_file):
    # Convert mp3 to wav for compatibility
    AudioSegment.from_mp3(audio_file).export(audio_file.replace('.mp3', '.wav'), format='wav')
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file.replace('.mp3', '.wav')) as source:
        audio = recognizer.record(source)  # Read the entire audio file
    text = recognizer.recognize_google(audio)  # Use Google Web Speech API
    return text

def get_caption(video_url):
    L = instaloader.Instaloader()
    shortcode = video_url.split("/")[-2]  # Extract shortcode from the URL
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    return post.caption