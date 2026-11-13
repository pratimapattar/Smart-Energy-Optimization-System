import time
from sensor import SensorSimulation
from decision_engine import DecisionEngine
from calculation import EnergyCalculator
from logger import DataLogger

#allocating memory for the class
sensor = SensorSimulation()
engine = DecisionEngine()
calculate = EnergyCalculator()
logger = DataLogger()

print("Sensor Simulation started....\n")

ac_state = False

try : 
    while True:
        data = sensor.get_data(ac_state)
        ac_state, reason = engine.decide(data)
        cycle_energy, cummalative_energy = calculate.compute(ac_state)

        record = {
        "temperature" : data["temperature"],
        "humidity" : data["humidity"],
        "occupancy" : data["occupancy"],
        "hour" : data["hour"],
        "ac_state" : ac_state,
        "reason" : reason,
        "cycle_energy" : cycle_energy,
        "cummalative_energy" : cummalative_energy
        }

        logger.store(record)

        print("\n")
        print(f"Temperature : {data['temperature']}")
        print(f"Humidity : {data['humidity']}")
        print(f"Occupancy : {data['occupancy']}")
        print(f"Hour : {data['hour']}")
        print("---------------------------")
        if ac_state :
            print(f"AC ON")
            print(f"Reason : {reason}")
        else :
            print(f"AC OFF")
            print(f"Reason : {reason}")
        print(f"Energy calulated per cycle : {cycle_energy}")
        print(f"Cummulative Energy : {cummalative_energy}")
        time.sleep(2)

except KeyboardInterrupt :
    print("\n" + "-" *75)
    print("Simulation is stopping..!!!")
    print(f"Total Energy Consumed : {cummalative_energy} units")
    print(f"Simulation is stopping after {logger.count()} cycles")