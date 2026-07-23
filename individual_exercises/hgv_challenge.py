
import random

import time

print()

KEY_SIGNAL_GOOD = 'Good'
KEY_SIGNAL_PATCHY = 'Patchy'
KEY_SIGNAL_NONE = 'None'

KEY_DECISION_DELAY = 'Delay Assignment'
KEY_DECISION_MONITOR = 'Monitor Closely'
KEY_DECISION_CONTINUE = 'Continue Normally'
KEY_DECISION_HIGH_PRIORITY = 'High Priority Review'

KEY_ID = 'ID'
KEY_SIGNAL_ZONE = 'Signal Zone'
KEY_TWIN_STATUS = 'Twin Status'
KEY_INFORMATION_AGE = 'Information Age'
KEY_DECISION = 'Decision'

KEY_ETA_MINUTES = 'ETA Minutes'
KEY_SPEED = 'Speed'
KEY_DISTANCE = 'Distance'

ROUTE_LENGTH_KM = 60 
SIMULATION_STEP_MINUTES = 1
MAX_SIMULATION_MINUTES = 180

KEY_SIMULATION_TIME = 'Simulation Time'
KEY_POSITION_KM = 'Position Km'
KEY_DISTANCE_REMAINING_KM = 'Distance Remaining Km'

# Number of HGVs in the Simulation
hgv_count = 10

# The number of minutes at which the information age is considered too old to be reliable
freshness_threshold = 5

# Empty Dictionary that will later store information on each HGV
lorries = []

def generate_hgv_id():
    """Generates a random value for the HGV ID, 1000 - 9999"""
    return random.randint(1000, 9999)

def generate_information_age():
    """Generates a random value for the HGV Information Age, 0 - 10 minutes"""
    return random.randint(0, 10)

def generate_hgv_speed():
    """Generates a random value for the HGV Speed, 50 - 60 km/h"""
    return random.randint(50, 60)

def generate_hgv_distance():
    """Generates a random value for the HGV Distance, 0 - 120 km"""
    return random.randint(0, 120)

def calculate_eta_minutes(distance, speed):
    """Calculates the arrival time in minutes based on distance and speed"""
    if speed == 0:
        return float('inf')  # Avoid division by zero
    return (distance / speed) * 60

def format_eta(time_in_minutes):
    """Formats a duration in minutes as HH:MM."""
    rounded_minutes = round(time_in_minutes)
    hours = rounded_minutes // 60
    minutes = rounded_minutes % 60
    return f"{hours:02d}:{minutes:02d}"

def determine_signal_zone(position_km):
    if position_km < 20:
        return KEY_SIGNAL_GOOD
    elif position_km < 35:
        return KEY_SIGNAL_PATCHY
    elif position_km < 45:
        return KEY_SIGNAL_NONE
    else:
        return KEY_SIGNAL_GOOD

def determine_twin_status(hgv):
    """Determines twin status based on the signal zone"""
    signal_zone = determine_signal_zone(hgv)
    if signal_zone == KEY_SIGNAL_NONE:
        return 'Unavailable'
    elif signal_zone == KEY_SIGNAL_PATCHY:
        return 'Updates Delayed'
    else:
        return 'Receiving Updates'
    
def determine_hgv_decision(hgv, information_age, eta_minutes):
    """Determines the action the twin should take based on signal zone."""
    signal_zone = determine_signal_zone(hgv)

    if information_age > freshness_threshold and eta_minutes < 30:
        return KEY_DECISION_HIGH_PRIORITY
    elif signal_zone == KEY_SIGNAL_NONE or information_age > freshness_threshold:
        return KEY_DECISION_DELAY
    elif signal_zone == KEY_SIGNAL_PATCHY:
        return KEY_DECISION_MONITOR
    else:
        return KEY_DECISION_CONTINUE

def create_hgv_dict(
    hgv_id,
    information_age,
    eta_minutes,
    distance,
    speed
):
    """Creates a dictionary containing the HGV's information."""
    signal_zone = determine_signal_zone(distance)
    twin_status = determine_twin_status(distance)
    hgv_decision = determine_hgv_decision(
    distance,
    information_age,
    eta_minutes
)

    hgv_dict = {
        KEY_ID: hgv_id,
        KEY_SIGNAL_ZONE: signal_zone,
        KEY_TWIN_STATUS: twin_status,
        KEY_INFORMATION_AGE: information_age,
        KEY_DECISION: hgv_decision,
        KEY_ETA_MINUTES: eta_minutes,
        KEY_SPEED: speed,
        KEY_DISTANCE: distance
    }

    lorries.append(hgv_dict)
    return hgv_dict

def display_hgv_information(hgv_dict):
    """Displays the generated HGV Information"""
    hgv_decision = hgv_dict[KEY_DECISION]
    print(f"HGV {hgv_dict[KEY_ID]}")
    print(f"Signal Zone: {hgv_dict[KEY_SIGNAL_ZONE]}")
    print(f"Twin Status: {hgv_dict[KEY_TWIN_STATUS]}")
    if hgv_dict[KEY_INFORMATION_AGE] == 1:
        print(f'Information Age: {hgv_dict[KEY_INFORMATION_AGE]} minute')
    else:
        print(f'Information Age: {hgv_dict[KEY_INFORMATION_AGE]} minutes')
    print(f'HGV Decision: {hgv_decision}')
    print(f'Distance from Destination: {hgv_dict[KEY_DISTANCE]} km')
    print(f'HGV Speed: {hgv_dict[KEY_SPEED]} km/h')
    print(f'ETA: {format_eta(hgv_dict[KEY_ETA_MINUTES])}')

# Main Program Loop
# for hgv in range(1, hgv_count + 1):
#     hgv_id = generate_hgv_id()
#     information_age = generate_information_age()
#     speed = generate_hgv_speed()
#     distance = generate_hgv_distance()
#     arrival_time = calculate_eta_minutes(distance, speed)

#     hgv_dict = create_hgv_dict(
#     hgv_id,
#     information_age,
#     arrival_time,
#     distance,
#     speed
# )
#     display_hgv_information(hgv_dict)
#     print()

# # Displays all HGVs in the Lorries List
# for lorry in lorries:
#     print(lorry)
#     print()

# Summary Statistics Variables
good_signal_hgv = 0
patchy_signal_hgv = 0
no_signal_hgv = 0
delayed_hgv = 0
closely_monitored_hgv = 0
continuing_normally_hgv = 0
high_priority_review_hgv = 0

# Summary Statistics
# for lorry in lorries:
#     signal_zone = lorry[KEY_SIGNAL_ZONE]
#     hgv_decision = lorry[KEY_DECISION]

#     if signal_zone == KEY_SIGNAL_GOOD:
#         good_signal_hgv += 1
#     elif signal_zone == KEY_SIGNAL_PATCHY:
#         patchy_signal_hgv += 1
#     elif signal_zone == KEY_SIGNAL_NONE:
#         no_signal_hgv += 1

#     if hgv_decision == KEY_DECISION_DELAY:
#         delayed_hgv += 1
#     elif hgv_decision == KEY_DECISION_MONITOR:
#         closely_monitored_hgv += 1
#     elif hgv_decision == KEY_DECISION_CONTINUE:
#         continuing_normally_hgv += 1
#     elif hgv_decision == KEY_DECISION_HIGH_PRIORITY:
#         high_priority_review_hgv += 1

# Variable to hold the total information age of all HGVs
total_information_age = 0

# Loop that updates the total information age variable with the information age of each HGV
# for lorry in lorries:
#     total_information_age += lorry[KEY_INFORMATION_AGE]

# Calculates the average information age for all HGVs
# average_information_age = total_information_age / len(lorries)

# delayed_hgv_num = 0
# monitored_hgv_num = 0
# good_signal_hgv_num = 0
# stale_information_hgv_num = 0

# for lorry in lorries:
#     if lorry[KEY_DECISION] == KEY_DECISION_DELAY:
#         delayed_hgv_num += 1
#     elif lorry[KEY_DECISION] == KEY_DECISION_MONITOR:
#         monitored_hgv_num += 1

#     if lorry[KEY_SIGNAL_ZONE] == KEY_SIGNAL_GOOD:
#         good_signal_hgv_num += 1

#     if lorry[KEY_INFORMATION_AGE] > freshness_threshold:
#         stale_information_hgv_num += 1

# percentage_hgv_delayed = (delayed_hgv_num / hgv_count) * 100
# monitored_hgv_percentage = (monitored_hgv_num / hgv_count) * 100
# good_signal_hgv_percentage = (good_signal_hgv_num / hgv_count) * 100
# stale_information_hgv_percentage = (stale_information_hgv_num / hgv_count) * 100

# def display_hgv_statistics():
#     """Displays a number of statistics about the HGVs in the simulation"""
#     print(f'Number of HGVs with Good Signal: {good_signal_hgv}')
#     print(f'Number of HGVs with Patchy Signal: {patchy_signal_hgv}')
#     print(f'Number of HGVs with No Signal: {no_signal_hgv}')
#     print(f'Number of HGVs Continued Normally: {continuing_normally_hgv}')
#     print(f'Number of HGVs being Closely Monitored: {closely_monitored_hgv}')
#     print(f'Number of Delayed HGVs: {delayed_hgv}')
#     print(f'Number of HGVs with High Priority Review: {high_priority_review_hgv}')
#     print(f'Average Information Age: {average_information_age} minutes')
#     print(f'Percentage of HGVs Delayed: {percentage_hgv_delayed:.2f}%')
#     print(f'Percentage of HGVs Monitored: {monitored_hgv_percentage:.2f}%')
#     print(f'Percentage of HGVs with Good Signal: {good_signal_hgv_percentage:.2f}%')
#     print(f'Percentage of HGVs with Stale Information: {stale_information_hgv_percentage:.2f}%')

# Runs the display_hgv_statistics function to show the summary statistics of the HGVs
# display_hgv_statistics()

print()

position_km = 0
distance_remaining_km = ROUTE_LENGTH_KM - position_km

# speed_kmh = generate_hgv_speed()
speed_kmh = 60

distance_per_minute = speed_kmh / 60

distance_travelled = (
    speed_kmh / 60
) * SIMULATION_STEP_MINUTES

position_km += distance_travelled

hgv_id = generate_hgv_id()

journey_history = []

def simulate_hgv_journey(hgv_id, speed_kmh):
    """Simulates one HGV travelling to the terminal."""

    simulation_time = 0
    position_km = 0.0
    journey_history = []

    distance_remaining_km = ROUTE_LENGTH_KM - position_km
    signal_zone = determine_signal_zone(position_km)
    eta_minutes = calculate_eta_minutes(
        distance_remaining_km,
        speed_kmh
    )

    journey_history.append({
        KEY_ID: hgv_id,
        KEY_SIMULATION_TIME: simulation_time,
        KEY_POSITION_KM: position_km,
        KEY_DISTANCE_REMAINING_KM: distance_remaining_km,
        KEY_SPEED: speed_kmh,
        KEY_SIGNAL_ZONE: signal_zone,
        KEY_ETA_MINUTES: eta_minutes
    })

    while (
        position_km < ROUTE_LENGTH_KM
        and simulation_time < MAX_SIMULATION_MINUTES
    ):
        simulation_time += SIMULATION_STEP_MINUTES

        distance_travelled = (
            speed_kmh / 60
        ) * SIMULATION_STEP_MINUTES

        position_km += distance_travelled
        position_km = min(position_km, ROUTE_LENGTH_KM)

        distance_remaining_km = (
            ROUTE_LENGTH_KM - position_km
        )

        signal_zone = determine_signal_zone(position_km)

        eta_minutes = calculate_eta_minutes(
            distance_remaining_km,
            speed_kmh
        )

        journey_history.append({
            KEY_ID: hgv_id,
            KEY_SIMULATION_TIME: simulation_time,
            KEY_POSITION_KM: round(position_km, 2),
            KEY_DISTANCE_REMAINING_KM: round(
                distance_remaining_km,
                2
            ),
            KEY_SPEED: speed_kmh,
            KEY_SIGNAL_ZONE: signal_zone,
            KEY_ETA_MINUTES: eta_minutes
        })

    if position_km < ROUTE_LENGTH_KM:
        print(
            f"Warning: HGV {hgv_id} did not reach the terminal."
        )
    
    return journey_history

journey_history = simulate_hgv_journey(hgv_id, speed_kmh)

for journey_state in journey_history:
    print(journey_state)
    time.sleep(0.2)

    simulation_time = journey_state[KEY_SIMULATION_TIME]

    if simulation_time % 5 == 0:
        print(
            f"Time: "
            f"{journey_state[KEY_SIMULATION_TIME]} min | "
            f"Position: {journey_state[KEY_POSITION_KM]} km | "
            f"Distance Remaining: {journey_state[KEY_DISTANCE_REMAINING_KM]} km | "
            f"Speed: {journey_state[KEY_SPEED]} km/h | "
            f"Signal Zone: {journey_state[KEY_SIGNAL_ZONE]} | "
            f"ETA: {journey_state[KEY_ETA_MINUTES]} min"
        )

def replay_journey(journey_history, delay_seconds = 0.2):
    """Displays an already-calculated journey gradually"""
    for state in journey_history:
        print(
            f"Time: {state[KEY_SIMULATION_TIME]} min | "
            f"Position: {state[KEY_POSITION_KM]} km | "
            f"Distance Remaining: {state[KEY_DISTANCE_REMAINING_KM]} km | "
            f"Speed: {state[KEY_SPEED]} km/h | "
            f"Signal Zone: {state[KEY_SIGNAL_ZONE]} | "
            f"ETA: {state[KEY_ETA_MINUTES]} min"
        )
        time.sleep(delay_seconds)

replay_journey(journey_history)

print()

final_state = journey_history[-1]
print("Final State:")
print(final_state)