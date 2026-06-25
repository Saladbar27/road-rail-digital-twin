
import random

# imagine there are 10 HGVs traveling toward a rail terminal
# each HGV should have:
# an ID number
# a signal status
# an estimated arrival time
# you can make the arrival time something simple like:
# 5 minutes, 10 minutes, 15 minutes, ...
# using arithmetic.
# Your output might look something like:

# HGV 1

# Signal: Good
# Estimated arrival: 5 minutes
# Twin status: Receiving updates

# For every third HGV:

# Signal: None
# Twin status: No updates available

# For every second HGV (that isn't every third):
# Signal: Patchy
# Twin status: Updates delayed

# Otherwise:

# Signal: Good
# Twin status: Receiving updates

# No user input is necessary—you can hardcode the number of HGVs to keep the focus on the logic.

hgv_count = 10

for hgv in range(1, hgv_count + 1):
    hgv_id = random.randint(1000, 9999)
    print('HGV', hgv_id)
    if hgv % 3 == 0:
        print('Signal: None')
        print('Twin Status: Unavailable')
        print()
    elif hgv % 2 == 0:
        print('Signal: Patchy')
        print('Twin Status: Updates Delayed')
        print()
    else:
        print('Signal: Good')
        print('Twin Status: Receiving Updates')
        print()
