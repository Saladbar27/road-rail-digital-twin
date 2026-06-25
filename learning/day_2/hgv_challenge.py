
import random

# Assignment: Refactor Your HGV Simulation

# Take the program you wrote earlier and separate the repeated logic into functions.
# For example, instead of having all the logic inside one loop, think about whether you could have functions with responsibilities like:

# generate_hgv_id()
# determine_signal_zone()
# display_hgv_information()

# You don't have to use those exact names—they're just examples.

# The goal is to make your main program read almost like English.
# For example, someone reading it should be able to follow the flow without digging into every detail.

print()

hgv_count = 10

def generate_hgv_id():
    """Generates a random ID for each HGV."""
    return random.randint(1000, 9999)

def determine_signal_zone(hgv):
    if hgv % 3 == 0:
        return 'Signal: None'
    elif hgv % 2 == 0:
        return 'Signal: Patchy'
    else:
        return 'Signal: Good'

def twin_status(hgv):
    if hgv % 3 == 0:
        return 'Twin Status: Unavailable'
    elif hgv % 2 == 0:
        return 'Twin Status: Updates Delayed'
    else:
        return 'Twin Status: Receiving Updates'


for hgv in range(1, hgv_count + 1):
    hgv_id = generate_hgv_id()
    print(f'HGV {hgv_id}')
    print(determine_signal_zone(hgv))
    print(twin_status(hgv))
    print()

print()