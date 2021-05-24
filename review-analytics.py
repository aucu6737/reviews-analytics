data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # % 在Python裡是求餘數的意思，例如1001 % 1000 = 1, 7 % 3 = 1, 6 % 4 = 2
			print(len(data))		
print('檔案讀取玩了，總共有', len(data), '筆資料')

sum_len = 0 # 創造一個用來累積留言程度的項目
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))