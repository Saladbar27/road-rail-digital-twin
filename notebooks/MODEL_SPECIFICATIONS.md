# Objectives of the project

Project To-Do List from 07/20 Meeting:
    Input aspect for the connectivity side of the program (terminal and/or dashboard)
    Parameter for the train network
    Store timestamp and comparing to the age of information

What is the project trying to demonstrate?:
This project will test whether a connectivity-aware digital twin can make more reliable terminal decisions and reduce avoidable HGV idling emissions compared with a naive digital twin that ignores information freshness.

What does one simulation represent?:
One simulation represents a group of HGVs travelling along a simplified 60 km route toward a road–rail freight terminal. Each instance of time, the HGVs move forward, may transmit their current position, and receive an updated estimated arrival time. The terminal uses the digital twin’s reported information to make slot-allocation decisions

What does the program actually model?:
HGV:
    ID
    actual position
    reported position
    speed
    actual ETA
    reported ETA
    signal zone
    last successful update time
    information age
    assigned terminal slot
    waiting or idling time
Route:
    total length
    good-signal zones
    patchy-signal zones
    no-signal zones
    terminal at the end
Terminal:
    number of slots
    decision time
    slot assignments
Digital Twins:
    naive twin
    connectivity-aware twin

What assumptions will the first version use?:

| Parameter                        | Initial value |
| -------------------------------- | ------------: |
| Route length                     |         60 km |
| Time step                        |      1 minute |
| HGV count                        |            10 |
| HGV speed                        |       60 km/h |
| Normal update interval           |     2 minutes |
| Freshness threshold              |     5 minutes |
| Terminal slots                   |             2 |
| Decision lead time               |    10 minutes |
| Good-zone update success         |          100% |
| Patchy-zone update success       |           50% |
| No-signal update success         |            0% |
| Extra idling after poor decision |    10 minutes |

These values are preliminary assumptions used to demonstrate the model architecture. Final values will either be supported with literature or identified explicitly as scenario assumptions.

How will connectivity work?
0–20 km: Good signal
20–35 km: Patchy signal
35–45 km: No signal
45–60 km: Good signal

Good signal: An update succeeds whenever one is scheduled.
Patchy signal: An update has a 50% chance of succeeding.
No signal: No update can reach the digital twin.

What decisions will each twin make?:
The Naive Twin:
    Trusts the most recently reported position;
    Calculates an ETA from that report;
    Ignores how old the information is;
    Assigns a terminal slot based on the reported ETA.

The Intelligent Twin:
    Checks the information age;
    Recognises when the latest position may be stale;
    Avoids a firm assignment when uncertainty is too high;
    May preserve flexibility or delay the decision;
    Will request multiple updates before entering a known signal gap.

What outputs will determine success?:
    incorrect slot assignments
    stale decisions
    average information age at decision
    total HGV waiting time
    total HGV idling time
    estimated CO₂e

Avoided idling = naive idling − intelligent idling
CO₂e saved = naive CO₂e − intelligent CO₂e

