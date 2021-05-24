data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # % 在Python裡是求餘數的意思，例如1001 % 1000 = 1, 7 % 3 = 1, 6 % 4 = 2
			print(len(data))		
print(len(data))
print(data[0])
print('---------------')
print(data[1])