from datetime import time

def extract_fibbo_params(hour: time):
    minute_str = f"{hour.minute:02d}"
    seed_one = int(minute_str[0])
    seed_two = int(minute_str[1])
    count = hour.second

    return seed_one, seed_two, count