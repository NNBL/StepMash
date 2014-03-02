import StepMash as sm
import matplotlib.pyplot as pl


if __name__ == "__main__":
    myMash = sm.StepMash()
    
    myMash.setGrainweight(5.6)
    myMash.setGraintemp(24)

    myMash.addStep(50)
    myMash.addStep(68)
    myMash.addStep(78)
    for i in xrange(len(myMash.steps)):
        if i == 0:
            pl.plot(i,myMash.steps[i],"o")
        else:
            label = str(myMash.wateramount[i-1])+"L @ "+str(myMash.watertemp[i-1])+"C"
            pl.plot(i,myMash.steps[i],"o", label=label)
    pl.title("Step mash water schedule")
    pl.xlabel("step #")
    pl.ylabel("temperature")
    pl.grid()
    pl.legend(loc="lower right")
    pl.show()