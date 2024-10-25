import pyaudio
import numpy as np
import webbrowser

# declare PyAudio object and stream object
p = pyaudio.PyAudio()
stream = p.open(
    rate=44100,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=2048
)

# get the constant audio stream
volume = 0
while volume <= 400:    # can change threshold here. this is some arbitrary value through playing around
    data = stream.read(2048)
    processed_data = np.frombuffer(data, dtype=np.int16)
    volume = np.abs(processed_data).mean()
    print(volume)
    
# here, we already received the required clap/audio signal
query = "sexy girls in bikini"
search_url = f"https://www.google.com/search?tbm=isch&q={query}"
webbrowser.open(search_url)