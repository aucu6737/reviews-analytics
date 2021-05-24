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
print('留言的平均長度為', sum_len / len(data))

# 篩選 sample 1
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

# 篩選 sample 2
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])
print(good[1])
# 快寫法
good = [d for d in data if 'good' in d]
# 最外圍的[]表示創造清單
# 最前面的d表示good.append(d)的d，如果把這個d改成1，就表示包含good的留言(d)就把1裝進清單good
# for d in data是for loop，if 'good' in d是篩選條件

bad = ['bad' in d for d in data] 
# 表示問了'bad' in d，也就是問留言有沒有包含bad，有的話TRUE，沒有的話FALSE，再把TRUE或是FALSE加入bad清單
print(bad)