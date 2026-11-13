from config import *
import random
from datetime import datetime
#defining sensor simulation class
class SensorSimulation :
    def __init__(self) :
        #ac will start with the initial temperature (28 c)
        self.last_temp = TEMP_INIT
    def _clamp(self, temp, min_temp, max_temp) :
        #checking the current temperature is in boundary of 18 to 40 c
        return max(min_temp, min(max_temp, temp))

    def _next_temperature(self, ac_state) :
        #generating the drift value depends on the ac state
        if ac_state :
            drift = random.uniform(DRIFT_AC_ON_MIN,DRIFT_AC_ON_MAX)
        else :
            drift = random.uniform(DRIFT_AC_OFF_MIN,DRIFT_AC_OFF_MAX)

        #calculate the next temp
        new_temp = self._clamp(self.last_temp + drift, TEMP_MIN, TEMP_MAX)
        self.last_temp = new_temp
        #using the round library to avoid thr extra floating values
        return round(self.last_temp, 1)

    def get_data(self, ac_state) :
        return {
            "temperature" : self._next_temperature(ac_state),
            "humidity" : round(random.uniform(HUMUDITY_MIN, HUMIDITY_MAX), 1),
            "occupancy" : random.choices([1,0], weights = [70,30]) [0],
            "hour" : datetime.now().hour
        }