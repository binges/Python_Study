#!/usr/bin/env python3
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from conf import config
from core import main


#$ 设置一个标记位，标记位数等于总的回合数
round_num = config.ROUND
#$ 设置一个标记，标记等游戏的回合数，循环一次数值加1
num = 1
$$ 使用总的回合数循环，没次循环数值减1，数值等0的时候循环结束，也代表游戏结束
while round_num:
	print("第%s回合"%num)
	#$ 判断玩家输入的数字是否存在随机数列表中，这里使用int() 是因为函数处理玩数据return回来的数据类型是str，所以要使用int转换为整数型，才能判断是否存在随机数列表中。
	if int(main.player.shoot()) in main.keeper.defense():
		#$ 如果在，相当于守门员把球接住，守门员得分值加1
		main.k1.fraction += 1
		print("对不起，球被接住")
		print("%s,得分:%s    %s,得分:%s" %(main.p1.name,main.p1.fraction,main.k1.name,main.k1.fraction))
	else:
		#$ 如果不在，相当于球进了，玩家得分值加1
		print("good，球进了")
		main.p1.fraction += 1
		print("%s,得分:%s    %s,得分:%s" %(main.p1.name,main.p1.fraction,main.k1.name,main.k1.fraction))
	#$ 一个回合，总回合数减1，直到结果为0
	round_num -= 1
	#$ 一个回合，游戏的回合数加1
	num += 1
else:
	#$ 判断两个人的得分情况，如果玩家的得分大于守门员，代表玩家赢
	if main.p1.fraction > main.k1.fraction :
		print("good,你赢了")
	#$ 如果玩家得分小于守门员，代表守门员赢
	elif main.p1.fraction < main.k1.fraction :
		print("很遗憾,你输了")
	#$ 如果得分相等，平局，这里考虑到有可能总的回合数设置的为偶数，会出现得分相等的情况
	else:
		print("不错，平局")





