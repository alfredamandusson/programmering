import winsound
import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds")
        time.sleep(1)

print("hello")



countdown(10)

winsound.Beep(440, 500)
winsound.PlaySound(".wav", winsound.SND_FILENAME)
