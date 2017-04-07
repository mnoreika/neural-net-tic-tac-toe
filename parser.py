import json

with open("net_des.in") as file:
	description = json.load(file)

	print (description['nr_layers'])