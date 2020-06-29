# -*- coding:utf-8 -*-

import random
import time

def main():
	portions_of_pizza = int(input("Ingrese la cantidad de rebanadas de pizza: "))
	
	if portions_of_pizza < 1:
		print("Se acabaron las rebanadas :'(")
	else:
		total = portions_of_pizza
		while portions_of_pizza != 0:
			time.sleep(3)
			random_number_of_discount = random.randint(1, portions_of_pizza)

			portions_of_pizza = portions_of_pizza - random_number_of_discount

			print("Ya comieron {} rebanadas de pizza.".format(random_number_of_discount))
			if portions_of_pizza == 0:
				print("Ya no quedan rebanadas de pizza :(")
				break
			else:
				print("Quedan {} de {} rebanadas de pizza, apresurate!!!".format(portions_of_pizza, total))


if __name__ == '__main__':
	main()