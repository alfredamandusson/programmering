import pyaudio  
import wave  
import os
current_working_directory = os.getcwd() 
print(current_working_directory)
#define stream chunk   
chunk = 1024  
  
#open a wav format music  
f = wave.open(r""+current_working_directory+"\\äggklocka\\klocka.mp3", "rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  
  
#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  
  
#stop stream  
stream.stop_stream()  
stream.close()  
  
#close PyAudio  
p.terminate()  