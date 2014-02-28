class StepMash():
    def __init__(self):
        self.Wm = 0.0# Total amount of water in mash
        self.r = 2.5 #ratio of water in liter per kg
        self.T1 = 22.0 # Initial temperature of the mash (start at room temp)
        self.temps = []
        self.Taw = 99.0 # Temperature of added water in celsius (assume near boiling)
        self.G = 2.5 #Amount of grain in mash in kilos
        self.tc = 0.41 #Termodynamic constant in Celsius
        #self.Tw = (self.tc/self.r)*(T2-T1)+T2 # Temperature of added water
        #self.Wa = (T2-T1)*(tc*G+Wm)/(Tw-T2) # Amount of added water
    
    def setGrainweight(self, weight):
        self.G = weight
        
    def setGraintemp(self, temp):
        self.T1 = temp
        
    def addstep(self, step):
        self.temps.append(step)
     
    def __str__(self):
        return str([temp for temp in self.temps])

if __name__ == "__main__":
    myMash = StepMash()

    myMash.setGrainweight(5.6)
    myMash.setGraintemp(21)
    
    myMash.addstep(56)
    myMash.addstep(64)
    myMash.addstep(73)
    
    print myMash