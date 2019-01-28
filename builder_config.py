import file_mang
import random


def _generate_config(counter, result):
	assert len(result) > 0
	if counter == 0:
		result.append("\n")
		return
	else:
		next_number = "1" if int(result[len(result) - 1]) == 0 else "0"
		result.append(next_number)
		_generate_config(counter - 1, result)

if __name__ == '__main__':
	num_keys = [61, 37, 43, 47, 51, 53, 59, 41, 31, 29, 26, 23]
	configs = []
	for number in num_keys:
		first_bit = random.randint(0, 1)
		config = [str(first_bit)]
		_generate_config((number * 2) - 1, config)
		configs.append(''.join(config))
		print("{0} > length {1}" .format(config, len(config)))
	print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><\n{0}" .format(configs))
	file_mang.createAndWrite("config-cif-lorenz.txt", configs)
		
		

