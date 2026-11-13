# Smart Energy Optimization System

## Project Overview
The **Smart Energy Optimization System** is a Python-based simulation project that demonstrates intelligent air-conditioning (AC) control for energy-efficient building management.
The system simulates environmental parameters such as temperature, humidity, room occupancy, and operating hours. 
Based on predefined decision-making rules, it automatically determines whether the AC should be switched ON or OFF.
It also calculates energy consumption for each simulation cycle, maintains cumulative energy usage, and stores simulation records for monitoring.

## Project Objectives
- Simulate environmental conditions inside a room.
- Implement automatic AC control using predefined decision rules.
- Reduce unnecessary energy consumption when the room is unoccupied or outside operating hours.
- Calculate energy consumption for each simulation cycle.
- Maintain cumulative energy consumption throughout the simulation.

## Features
- **Temperature Simulation:** Generates changing room temperature values.
- **Humidity Simulation:** Generates simulated humidity readings.
- **Occupancy Monitoring:** Simulates whether the room is occupied or empty.
- **Operating Hour Monitoring:** Checks whether the current time falls within configured operating hours.
- **Intelligent AC Control:** Uses temperature thresholds, occupancy, and operating hours to control AC operation.
- **Hysteresis Control:** Prevents unnecessary frequent switching of the AC when temperature is within the defined threshold range.
- **Energy Calculation:** Calculates energy consumption for every simulation cycle.
- **Cumulative Energy Monitoring:** Maintains the total energy consumed during the simulation.
- **Data Logging:** Stores simulation records for monitoring.

## Technologies Used
- **Programming Language:** Python 3
- **Development Environment:** Linux
- **Execution:** Linux Terminal
- **Libraries:** Python Standard Library (`random`, `datetime`, `time`)

## Python Concepts Used
- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Functions and Methods
- Conditional Statements
- Loops
- Dictionaries
- Lists
- Modules and Packages
- Exception Handling
- Random Number Generation
- Importing and Using Modules

## Project Structure
```text
Smart-Energy-Optimization-System/
│
├── src/
│   ├── main.py
│   ├── sensor.py
│   ├── decision_engine.py
│   ├── calculation.py
│   ├── logger.py
│   └── config.py
│
├── Documentation.txt
├── README.md
└── .gitignore
```

## Working Principle
The system operates through the following stages:
1. **Sensor Simulation:** Generates temperature, humidity, occupancy, and current hour values.
2. **Decision Engine:** Evaluates the simulated data using predefined rules.
3. **AC Control:** Determines whether the AC should be ON or OFF.
4. **Energy Calculation:** Calculates energy consumed during each cycle.
5. **Data Logging:** Stores the environmental readings, AC status, decision reason, and energy details.
6. **Continuous Simulation:** Repeats the process at regular intervals until the user stops execution.

## AC Decision-Making Rules
The Decision Engine follows these rules:
| Condition | AC State |
|---|---|
| Room is unoccupied | OFF |
| Outside operating hours | OFF |
| Temperature is above the upper threshold | ON |
| Temperature is below the lower threshold | OFF |
| Temperature is within the threshold range | Maintains previous state |
The system uses a threshold and buffer value to implement hysteresis control.

**Default Configuration:**
- Temperature threshold: 26°C
- Buffer: 1.5°C
- Upper threshold: 27.5°C
- Lower threshold: 24.5°C
- Operating hours: 6:00 AM to 11:00 PM
These values can be modified in `config.py`.

## Energy Calculation
Energy consumption is calculated based on the AC operating state.
- AC ON: 2.0 units per cycle
- AC OFF: 0.1 units per cycle
The system calculates the energy consumed during each cycle and updates the cumulative energy consumption.
These are simulation values configured in `config.py`, not measurements from a physical AC unit.

## How to Run the Project
### 1. Clone the Repository
```bash
git clone https://github.com/pratimapattar/Smart-Energy-Optimization-System.git
```
### 2. Navigate to the Project Directory
```bash
cd Smart-Energy-Optimization-System
```
### 3. Run the Application
```bash
python3 src/main.py
```
The simulation starts and continuously displays the environmental readings, AC operating state, decision reason, and energy consumption.
Press `Ctrl + C` to stop the simulation.

## Sample Output
```text
Sensor Simulation started....

Temperature : 29.4
Humidity : 58.7
Occupancy : 1
Hour : 14
---------------------------
AC ON
Reason : Temp high -> AC ON
Energy calculated per cycle : 2.0
Cumulative Energy : 2.0

Temperature : 27.8
Humidity : 64.2
Occupancy : 1
Hour : 14
---------------------------
AC ON
Reason : Within band -> Hold
Energy calculated per cycle : 2.0
Cumulative Energy : 4.0
```
*Sample values are illustrative; actual readings vary because environmental parameters are simulated.*

## Learning Outcomes
Through this project, I gained practical experience in:
- Developing a Python application using modular programming.
- Implementing object-oriented programming concepts.
- Generating simulated environmental sensor data.
- Designing rule-based decision-making logic.
- Understanding hysteresis control.
- Calculating and tracking cumulative energy consumption.
- Managing data using Python dictionaries and lists.
- Handling continuous execution and keyboard interruption.
- Debugging and testing a multi-module Python application.

## Project Scope
This project is currently implemented as a software-based simulation. Physical sensors, AC hardware integration, and a graphical monitoring dashboard are not included in this implementation.

## Author
**Pratima C Pattar**
