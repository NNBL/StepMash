import StepMash as sm
import matplotlib.pyplot as pl


if __name__ == "__main__":
    myMash = sm.StepMash()
    
    myMash.setGrainweight(5.6)
    myMash.setGraintemp(24)

    myMash.addStep(55)
    myMash.addStep(68)
    myMash.addStep(78)