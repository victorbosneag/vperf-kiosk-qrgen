import segno
import csv
from PIL import Image
import io
from card_creator import create_card

with open('teams.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			#print(f'Column names are {", ".join(row)}')
			line_count += 1
		else:
			print(f"{row[1]}")
			create_card(row[1], line_count)
			line_count += 1
