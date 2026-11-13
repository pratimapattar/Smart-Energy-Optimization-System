from config import *

class EnergyCalculator : 
    def __init__(self) : 
        self.cummalative_energy = 0.0

    def compute(self, ac_state) :
        if ac_state : 
            cycle_energy = RATE_ON
        else :
            cycle_energy = RATE_OFF
        
        self.cummalative_energy = self.cummalative_energy + cycle_energy

        return cycle_energy, round(self.cummalative_energy,2)
        