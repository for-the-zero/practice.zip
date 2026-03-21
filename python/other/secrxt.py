englist = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,")
numlist = list('0123456789')

def basec(char):
	global englist
	global numlist
	if char in englist:
		base_sc = englist.index(char)
		base_sc = str(base_sc)
		if len(list(base_sc)) != 2:
			base_sc = '0' * (2 - len(list(base_sc))) + base_sc
		base_sc = '0' + base_sc
		return base_sc
	elif char in numlist:
		if len(list(char)) != 2:
			char = '0' * (2 - len(list(char))) + char
		char = '1' + char
		return char
	else:
		return '200'




def ss2sc(ss):
	global englist
	ss = list(ss)
	rt = ''
	for i in ss:
		rt += basec(i)
	return rt



if __name__ == '__main__':
	print(ss2sc(input('要加密的（不支持中文，符号只支持半角逗号）：\n')))
	input()
