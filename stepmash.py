"""Usage: python stepmash.py"""
#Author: hwidth

#Editable variables
Wm = 0.0# Total amount of water in mash
r = 2.5 #ratio of water in liter per kg
T1 = 22.0 # Initial temperature of the mash (start at room temp)
T2 = 55.0 # First target temperature of the mash in celsius
T3 = 68.0 # Second target temperature of the mash in celsius
T4 = 78.0 # Third target temperature of the mash in celsius
Taw = 99.0 # Temperature of added water in celsius (assume near boiling)
G = 5.6 #Amount of grain in mash in kilos

#Do not edit below!
tc = 0.41 #Termodynamic constant in Celsius
Tw = (tc/r)*(T2-T1)+T2 # Temperature of added water
Wa = (T2-T1)*(tc*G+Wm)/(Tw-T2) # Amount of added water

print "Start temperature: ", T1, "C"
print "Grain in mash: ", G, "Kg"
print "Liter per kilo grain ratio: ", r, "l\n"

print "For", T2, "C at", r, "l per kg, add", r*G, "l", "at: ", round(Tw, 1), "C"

Wm = r*G
print "Water in mash: ", Wm, "l\n"
Wa = (T3-T2)*(tc*G+Wm)/(Taw-T3) # Amount of water added
Wm = Wm + Wa
print "For", T3, "C", "Add: ", round(Wa, 2), "l at", round(Taw, 1), "C"
print "Water in mash: ", round(Wm, 2),"l\n"

Wa = (T4-T3)*(tc*G+Wm)/(Taw-T4) # Amount of water added
Wm = Wm + Wa
print "For", T4, "C", "Add: ", round(Wa, 2), "l at", round(Taw, 1), "C"
print "Water in mash: ", round(Wm, 2), "l\n"
print "New liter per kilo grain ratio: ", round(Wm/G, 1)