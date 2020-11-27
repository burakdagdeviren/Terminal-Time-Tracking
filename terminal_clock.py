import pyfiglet
from datetime import datetime, timedelta
import os
from time import sleep
from tqdm import tqdm

# Definitions
t2 = timedelta(hours=18, minutes=00, seconds=00)
t3 = timedelta(hours=9, minutes=00, seconds=00)
out_of_scope = "N/A"
ascii_none = pyfiglet.figlet_format(out_of_scope)
prog_bar = tqdm(total=1080, position=0, leave=False)
prog_counter = 0


try:
    while True:
        os.system('cls')
        now = datetime.now()
        start = datetime.now().time()

        # Format current time
        t1 = timedelta(hours=start.hour, minutes=start.minute,
                       seconds=start.second)

        # find remaining duration
        time_left = t2 - t1
        time_left_string = str(time_left)
        time_left_string = time_left_string[:-3]

        # Progress Bar Conter if time is above 09.00
        if t1 >= t3 and t1 <= t2:

            sub_seconds = time_left.seconds / 30
            remain_time = (1080 - sub_seconds) + prog_counter
            remain_time_rounded = round(remain_time)
            prog_counter += 1

        # Strip current Time
        current_time = now.strftime("%H:%M")

        # Generate ASCII strings
        ascii_clock = pyfiglet.figlet_format(current_time)
        ascii_left = pyfiglet.figlet_format(time_left_string)

        # Print the clock
        print("Current Time ========")
        print(ascii_clock)

        # Check to see if time is > 18:00
        if t2 > t1:
            print("Time Left ===========")
            print(ascii_left)
            print("========================")

            # setup the progress bar
            prog_bar.set_description("Progress:".format(remain_time_rounded))

            # check to see if it is the first run
            if prog_counter == 1:
                prog_bar.update(remain_time_rounded)
            else:
                prog_bar.update(1)

        elif t2 < t1:  # edit this line for more control
            print("Time Left ===========")
            print(ascii_none)
            print("========================")

        # Wait 1 minute
        sleep(30)

except KeyboardInterrupt:
    prog_bar.close()
    print("\ndone...")
