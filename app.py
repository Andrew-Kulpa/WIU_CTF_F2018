import hashlib
import json
with open('app_config.json') as json_data_file:
    data = json.load(json_data_file)
flag_found = False
expected_digest = hashlib.sha512(data["password"].encode()).hexdigest()

while flag_found != True:
	mystring = input('Enter Flag: ')
	hash_object = hashlib.sha512(mystring.encode())
	input_digest = hash_object.hexdigest()
	if (input_digest == expected_digest):
		print("You win!\n")
		flag_found = True
	else:
		print("Try Again.\n")
	
input('Press Enter to exit.')