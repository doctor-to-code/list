data = []
with open('food.txt', 'r', encoding="utf-8") as f:
	for line in f:
		data. append(line.strip())

print(data)