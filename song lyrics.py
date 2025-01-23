import sys
from time import sleep

def print_lyrics():
    lines = [
        ("If the world was ending, I wanna be next to you....................................", 0.1),

        ("If the party was over", 0.1),
        ("And our time on Earth was through............................", 0.1),
        ("I'd wanna hold you just for a while...........", 0.1),
        ("And die with a smile", 0.1),
        ("If the world was ending", 0.1),
        ("I wanna be next to you..............", 0.1),
    ]
    
    delays = [0.6, 0.7, 0.8, 0.7, 0.6, 0.8, 0.7, 0.6]  # Adjust delays for each line

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])  # Wait after printing each line
        print('')  # Print a new line for the next lyric

print_lyrics()

