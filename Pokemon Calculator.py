import random
print ("\n   P o k e m o n  C a l c u l a t o r")
print ("\n          Charizard V.S. Feraligatr")
print ("\nLevel        90            95")
print ("SAtt         205")
print ("SDef                       188")

Level = 90
SAtt = 205
SDef = 188
Power = 110
Targets = 1
Weather = 1
Badge = 1
Critical = 1,2
crit = random.choice(Critical)
r = .85, 1
ran = random.choice(r)
Stab = 1
Type = 1
Burn =  1
Other = 1
Modifier = Targets * Weather * Badge * crit * ran * Stab * Type * Burn * Other

if crit == 2:
    print("\n        CRITICAL DAMAGE")
Damage = ((((((2+Level)/5)+2)*Power*SAtt/SDef)/50)+2)*Modifier
print ("\nCharizards Damage to Feraligatr is ", Damage, "\n\n")