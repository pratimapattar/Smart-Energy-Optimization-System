from config import *

class DecisionEngine :
    def __init__(self) :
        self.ac_state = False #assuming ac is off state
        self.reason   = ""

    def decide(self,data) :
        temp  = data["temperature"]
        humi  = data["humidity"]
        occup = data["occupancy"]
        hour  = data["hour"]

        #calculate upper and lower threshold values
        upper = DEFAULT_THRESHOLD + DEFAULT_BUFFER
        lower = DEFAULT_THRESHOLD - DEFAULT_BUFFER

        #rule 1 : Room empty
        if occup == 0 :
            self.ac_state = False
            self.reason   = "Room empty -> AC OFF"
        #rule 2 : outside operation hours
        elif hour < DEFAULT_OP_START or hour >DEFAULT_OP_END :
            self.ac_state = False
            self.reason   = "Outside the working hour -> AC OFF"
        #rule 3 : high temp -> temperature > upper threshold
        elif temp > upper :
            self.ac_state = True
            self.reason   = "Temp high -> AC ON"
        #rule 4 : low temp -> temperature < lower threshold
        elif temp < lower :
            self.ac_state = False
            self.reason   = "Temp low -> AC OFF"
        #rule 5 : hystersis ( hold state)
        else :
            self.reason = "Within band -> Hold" 

        return self.ac_state, self.reason
