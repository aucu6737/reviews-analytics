#文字計數
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # % 在Python裡是求餘數的意思，例如1001 % 1000 = 1, 7 % 3 = 1, 6 % 4 = 2
			print(len(data))		
print('檔案讀取完了，總共有', len(data), '筆資料')

print(data[0])

wc = {} # wc = word count
for d in data:
	words = d.split() # split可以用' '來表示要用空格切，也可以不指定，預設就會是用空格切，而且不會因為多個空格被切出來的狀況
	for word in words:
		 if word in wc: # 也可以用not in
		 	wc[word] += 1 # 該字的出現次數+1
		 else:
		 	wc[word] = 1 # 把新出現的字word加入wc字典，=1表示第一次出現，也是防當機
for word in wc: # 這個word是指字典wc裡的key，每一個word就是每個key，value為計數
	if wc[word] > 1000000: # 因為字太多了，所以只印出現大於1000000次的字
		print(word, wc[word]) # 印出字典中每個字及其計數
# 字串裡面也會有空字串，是因為留言中有使用多個空格
print(len(wc)) # 印出字典裡總共有多少字
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字?')
	if word =='q':
		break
	elif word not in wc:
		print('這個字沒有出現過喔!')
	else:
		print(word, '出現過的次數為', wc[word], '次')
print('感謝使用本查詢功能!')

# 選取多行再按ctrl+/表示註解調