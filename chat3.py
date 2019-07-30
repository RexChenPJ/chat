lines = []
#讀取檔案
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

#當有資料是相連的，利用清單分割取出人名
#字串也能當成清單
for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(name)