import time
# https://www.youtube.com/watch?v=L34k-fUTHnI

def set_alarm(alarm_time, sound_file):
    while True:
        current_time = time.strftime(,time.localtime())
        if current_time == alarm_time:
            print("Alarm! Klockan är", alarm_time)
            
        time.sleep(1)

def main():
    alarm_time = input(" (08:15:52): ")
    set_alarm(alarm_time, sound_file)

if __name__ == "__main__":
    main()


# välj hur många sekunder 
# räkna ner - slinga
# sov 1 sek
# skriv ut tiden som är kvar