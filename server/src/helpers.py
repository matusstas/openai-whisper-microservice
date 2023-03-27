import ffmpeg
import whisper
import numpy as np

from fastapi import UploadFile

from src.database import Query

def download(model_name: str, db):
    """
    Download a Whisper ASR model.
    """
    db.insert({"name": model_name, "downloaded": False})
    whisper.load_model(model_name)
    db.update({"downloaded": True}, Query().name == model_name)


# Modified
# https://github.com/openai/whisper/blob/main/whisper/audio.py
def load_audio(file: UploadFile, sr: int = 16000):
    """
    Open an audio file object and read as mono waveform, resampling as necessary.
    """
    try:
        out, _ = (
            ffmpeg.input("pipe:", threads=0)
            .output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=sr)
            .run(cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True, input=file.file.read())
        )
    except ffmpeg.Error as e:
        raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e

    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0
