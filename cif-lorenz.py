import sys, file_mang
from classes import CoderMachine, CypherMachine, Gear
			
PATH_CONFIG = "config-cif-lorenz.txt"
WHEELS_NUMBER = 12

def _create_gears(configs):
	gears = []
	for line in configs:
		pins = []
		pins.extend(line)
		pins.remove('\n')
		gears.append(Gear(pins))
	return gears

if __name__ == '__main__':
			
	#cypherMachine = CypherMachine(None, None, None, None)
	#print(cypherMachine.cypher("4"))
	
	configs = file_mang.getLinesFile(PATH_CONFIG)
	gears = _create_gears(configs)
	if len(gears) == WHEELS_NUMBER:
		cypherMachine = CypherMachine(gears[0], gears[1], gears[2:7], gears[7:12])
		ciphered_text = cypherMachine.decipher("FR")
		print(ciphered_text)
		cypherMachine = CypherMachine(gears[0], gears[1], gears[2:7], gears[7:12])
		deciphered_text = cypherMachine.decipher(ciphered_text)
		
		


