class Gear:
	pins = []
	
	def __init__(self, parts):
		self.pins = parts
		
	def synchronize(self, index):
		if index >= 0 and index < len(self.pins):
			aux_end = self.pins[0:index]
			del self.pins[0:index]
			self.pins.extend(aux_end)
				
	def rotate(self):
		self.synchronize(1)

	def getpin(self, index):
		answer = -1
		if index >= 0 and index < len(self.pins):
			answer = self.pins[index]
		return answer		

class CypherMachine:	
	engine_wheel_1 = None
	engine_wheel_2 = None
	chi_wheels = []
	psi_wheels = []
	
	def __init__(self, wheel_1, wheel_2, psi_wheels, chi_wheels):
		self.engine_wheel_1 = wheel_1
		self.engine_wheel_2 = wheel_2
		self.psi_wheels = psi_wheels
		self.chi_wheels = chi_wheels
		
	def _rotate_wheels(self):
		self.engine_wheel_1.rotate()
		if self.engine_wheel_1.getpin(0) == "1":			
			self.engine_wheel_2.rotate()
		self._rotate(self.chi_wheels)
		if self.engine_wheel_2.getpin(0) == "1":
			self._rotate(self.psi_wheels)
		
	def _rotate(self, wheels):
		for wheels in wheels:
			wheels.rotate()
	
	def _get_first_bit(self, gears):
		bits = []
		for gear in gears:
			bits.append(gear.getpin(0))
		return bits		
	
	def _xor(self, bits_1, bits_2, bits_3):
		result = []
		for index in range(0, len(bits_1)):
			xor_1 = "0" if bits_1[index] == bits_2[index] else "1"
			xor_2 = "0" if xor_1 == bits_3[index] else "1"
			result.append(xor_2)
			self._rotate_wheels()
		return result
	
	def _change_bits(self, bits):
		segment = 5
		new_bits = ""
		for index in range(0, len(bits), segment):			
			psi_bits = self._get_first_bit(self.psi_wheels)
			chi_bits = self._get_first_bit(self.chi_wheels)
			code = bits[index : index + segment]
			
			print("BITS: \t\t\t{0}\n> PSI INICIO: {1} \n> CHI_INICIO: {2}" .format(code, chi_bits, psi_bits))
			
			new_code = self._xor(code, psi_bits, chi_bits)
			
			print("> CODIGO:     {0}\n" .format(new_code))
			
			new_bits += (''.join(new_code))
		return new_bits
	
	def cipher(self, text):
		coder_machine = CoderMachine()
		code = coder_machine.code(text)
		new_text = ""
		
		print("> Codigo: {0}" .format(code))
		
		if code != -1:
			new_code = self._change_bits(code)			
			new_text = coder_machine.decode(new_code)
			
			print("> Nuevo Codigo: {0}\n\n\t Nuevo texto: {1}" .format(new_code, new_text))
						
		return new_text
	
	def decipher(self, text):
		coder_machine = CoderMachine()
		code = coder_machine.code(text)
		new_text = ""
		
		print("> Codigo: {0}" .format(code))
		
		if code != -1:
			new_code = self._change_bits(code)			
			new_text = coder_machine.decode(new_code)
			
			print("> Nuevo Codigo: {0}\n\n\t Nuevo texto: {1}" .format(new_code, new_text))
						
		return new_text

class CoderMachine:
	
	# key "#" indicates the figures symbols (index 0 of baudot_code variable) and key "*" indicates the letters symbols (index 1 of baudot_code variable)
	keys = [
	["#", "*"],
	["11111", "11011"]	
	]
	baudot_symbols = [
	['-', '?', ':', '¿', '3', '%', '@', '_', '8', ';', '(', ')', '.', ',', '9', '0', '1', '4', "'", '5', '7', '=', '2', '/', '6', '+', '\r', '\n', ' '],
	['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '\r', '\n', ' ']
	]
	
	baudot_codes = ["11000", "10011", "01110", "10010", "10000", "10110", "01011", "00101", "01100", "11010", "11110", "01001", "00111", "00110", "00011", "01101", "11101", "01010", "10100", "00001", "11100", "01111", "11001", "10111", "10101", "10001", "00010", "01000", "00100"]
	coding_mode = -1  # codification mode is 0: letters. 1: figures. it will change when the symbol is in first or second position of baudote_code variable
	work_mode = None # work_mode variable indicates if the machine is coding(True) or decoding(False)
	result = "" # this variable returns coded text or binariy values
	
	def __init__(self):
		pass
		
	def config_default_values(self):
		self.coding_mode = -1
		self.result = "";
	
	def _configure_mode_coding(self, symbol):
		aux_symbols = (self.baudot_symbols[0])[:]
		aux_symbols.extend(self.baudot_symbols[1])
		result = -1
		if symbol in aux_symbols:
			result = 0 if aux_symbols.index(symbol) < len(self.baudot_symbols[0]) else 1
			self._set_coding_mode(result)
		return result
		
	def _set_coding_mode(self, new_config):
		if self.coding_mode != new_config and new_config != -1:
			index_key = 1 if self.work_mode else 0
			self.result += (self.keys[index_key])[new_config]
			#print(self.result)
		self.coding_mode = new_config
	
	def _search_for_code(self, symbol):
		code = -1
		config = self._configure_mode_coding(symbol)
		if config != -1:
			index = self.baudot_symbols[self.coding_mode].index(symbol)
			code = self.baudot_codes[index]
		return code	
	
	def code(self, text):
		self.work_mode = True
		for symbol in text:
			code = self._search_for_code(symbol)
			if code == -1:
				self.result = -1
				print("ERROR: '{0}' no es permitido" .format(symbol))
				break
			self.result += code
		coded_text = self.result
		self.config_default_values()
		return coded_text
		
	def _search_for_symbol(self, code):
		result = -1
		if code in self.keys[1]:
			self._set_coding_mode(self.keys[1].index(code))
			result = ""
		else:
			symbols = self.baudot_symbols[self.coding_mode]
			if code in self.baudot_codes:
				result = symbols[self.baudot_codes.index(code)]
		return result
	
	def decode(self, code_text):
		self.work_mode = False
		text = ""
		code_list, segment = [], 5
		code_list.extend(code_text)
		for index in range(0, len(code_list), segment):
			code = ''.join(code_list[index : (index + segment)])
			symbol = self._search_for_symbol(code)
			if symbol == -1:
				text = symbol
				print("ERROR: '{0}' no es permitido" .format(code))
				break
			text += symbol
		return text
				
	
	def __str__(self):
		state = "\n > variables" 
		state += ("\n coding_mode: " + str(self.coding_mode))
		state += ("\n work_mode: " + str(self.work_mode))
		state += ("\n result: " + str(self.result))
		return state
