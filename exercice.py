#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	TAX_RATE = 0.15


	#Calculer le sous-total
	soustotal = 0
	for item in data:
		soustotal += item[INDEX_QUANTITY] * item[INDEX_PRICE]
	#Calculer les taxes et total

	taxes = soustotal * TAX_RATE
	total = taxes + soustotal

	#Retourner la facture formaté (sous-total, taxes, total)

	result = name
	result += "\n" + f"SOUS TOTAL {soustotal : >10.2f} $"
	result += "\n" + f"TAXES      {taxes : >10.2f} $"
	result += "\n" + f"TOTAL      {total : >10.2f} $"


	return result


def format_number(number, num_decimal_digits):

	#Séparer les parties entières et décimales
	decimaux = abs(number) % 1.0
	entiers = int(abs(number))

	# formater les décimaux
	decimauxstr = f"{decimaux :.{num_decimal_digits}f}"[1:]

	# formater les entiers
	entierstr = ""
	while entiers >= 1000:
		digits = entiers % 1000
		digitstr = f" {digits :0>3}"
		entierstr = digitstr + entierstr
		entiers //= 1000
	entierstr = str(entiers) + entierstr

	#Concaténer les deux parties
	return ("-" if number < 0 else "") + entierstr + decimauxstr

def get_triangle(num_rows):
	BORDER_CHAR = "+"
	TRIANGLE_CHAR = "A"
	triangle_width = 1 + 2 * (num_rows -1)

	toporbottom_row = "\n" + BORDER_CHAR * (triangle_width + 2)
	triangle_row = ""

	for rows in range(num_rows):
		num_triangle_chars = rows * 2 + 1
		triangle_chars = TRIANGLE_CHAR * num_triangle_chars
		triangle_line = f"{triangle_chars : ^{triangle_width}}"
		result = "\n" + BORDER_CHAR + triangle_line + BORDER_CHAR
		triangle_row += result


	return toporbottom_row + triangle_row + toporbottom_row


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-128345.678, 2))

	print(get_triangle(2))
	print(get_triangle(10))
