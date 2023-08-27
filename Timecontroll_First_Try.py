import time
import datetime

def start_create_timestamp():
    start_timestamp = int(time.time())
    return start_timestamp



def end_create_timestamp():
    time.sleep(62)
    end_timestamp = int(time.time())
    return end_timestamp


def timestamp_difference(timestamp_start, timestamp_end):
    time_difference = timestamp_end - timestamp_start
    hours = time_difference // 3600  # 1 Stunde = 3600 Sekunden
    minutes = (time_difference % 3600) // 60
    return hours, minutes


# Beispielaufruf der Funktion
start_timestamp = start_create_timestamp()
end_timestamp = end_create_timestamp()
hours, minutes = timestamp_difference(start_timestamp, end_timestamp)


print("Timestamps start", start_timestamp)
print("Timestamp end", end_timestamp)
print("Differenz:", hours, "Stunden", minutes, "Minuten")