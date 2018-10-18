#!/usr/bin/python3

import textfsm
import sys
import re


# Open the template file, and initialise a new TextFSM object with it.
template_file = sys.argv[1]
fsm = textfsm.TextFSM(open(template_file))


# Read stdin until EOF, then pass this to the FSM for parsing.
input_data = open('raw.install').read()
fsm_results = fsm.ParseText(input_data)

print(fsm_results)

for i in fsm_results:
    print(i)



#pattern = re.compile(r"(.*)\.\n\[#*|.*\]\s+(\d+)\%\s+\-\-\s+([A-Z]+)", re.MULTILINE)
pattern = re.compile(r"(.*)\.\n\[#*|.*\]\s+(\d+)\%\s+\-\-\s+([A-Z]+)", re.MULTILINE)


s = pattern.findall(input_data)

step= []

for index, item in enumerate(s):
    if item[0]:
        if s[int(index+1)][1] and s[int(index+1)][2]:
            #  on va chercher les valeurs pour la deuxieme ligne grace a lindex. 
            #  puis on ajoute le non de letape, le pourcentage et l'etat 
            #  crade, faudrait vraiment faire mieux!! #
            step.append((item[0], s[int(index+1)][1], s[int(index+1)][2]))

print(step)
