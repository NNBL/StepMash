class StepMash():
    def __init__(self):
        self.Wm = 0 # Total amount of water in mash
        self.r = 2.5 #ratio of water in liter per kg
        self.steps = [22,] # Initial temperature of the mash (start at room temp)
        self.wateramount = []
        self.watertemp = []
        self.Temp_of_added_water = 99.0 # Temperature of added water in celsius (assume near boiling)
        self.G = 2.5 #Amount of grain in mash in kilos
        self.tc = 0.41 #Termodynamic constant in Celsius

    def setGrainweight(self, weight):
        self.G = weight

    def setGraintemp(self, temp):
        self.steps[0] = temp

    def setWatertemp(self, temp):
        self.Temp_of_added_water = temp

    def addStep(self, step):
        if len(self.steps) == 1:
            strikewater = self.temp_of_added_water(self.steps[0], step)
            self.watertemp.append(round(strikewater, 1))
            self.wateramount.append(round((step-self.steps[0])*(self.tc*self.G+sum(self.wateramount))/(strikewater-step), 2)) # Amount of added water
        else:
            self.watertemp.append(self.Temp_of_added_water)
            self.wateramount.append(round((step-self.steps[-1])*(self.tc*self.G+sum(self.wateramount))/(self.Temp_of_added_water-step), 2)) # Amount of water added
        self.steps.append(step)

    def temp_of_added_water(self, T1, T2):
        Tw = (self.tc/self.r)*(T2-T1)+T2 # Temperature of added water
        return Tw

    def __str__(self):
        return "Start temperature: %sC\nGrain in mash: %sKg\nLiter per kilo grain ratio: %sl\n" % (self.steps[0], self.G, self.r)

if __name__ == "__main__":
    myMash = StepMash()

    myMash.setGrainweight(5.6)
    myMash.setGraintemp(24)

    myMash.addStep(55)
    myMash.addStep(68)
    myMash.addStep(78)

    print myMash.watertemp
    print myMash.wateramount, str(sum(myMash.wateramount))+"L"
