#!/usr/bin/env python3
import os,sys,random
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from conf import config

class role(object):
	"""
	父类，定义了，name和得分
	"""
	def __init__(self,name):
		self.name = name

class player(role):
	"""
	玩家的类，继承了role父类
	"""
	def __init__(self,name,fraction):
		#$ 继承父类的name，自己独有的属性fraction
		super(player,self).__init__(name)
		self.fraction = fraction

	def shoot():
		#$ 让玩家输入一个一定范围内的数字，起始值是1，结束值使用的是配置文件中的游戏难度系数
		player_num = input("请输入1-%s 中的一个数字:" %config.DIFFICULTY)
		return player_num

class keeper(role):
	"""
	守门员的类，继承了role父类
	"""
	def __init__(self,name,fraction):
		#$ 继承父类的name，自己独有的属性fraction
		super(keeper,self).__init__(name)
		self.fraction = fraction

	def defense():
		#$ 守门员数量，可以有多名守门员，另外一个作用是设置循环的次数，每次循环随机生成一个数字，次数减1，等于0的时候循环结束
		n = config.KEEPER_NUM
		#$ 设置一个随机数的列表，考虑到可能会有多名守门员
		keeper_num = []
		#$ 开始循环
		while n:
			#$ 把随机生成的数字添加到随机数列表中
			keeper_num.append(random.randint(1,config.DIFFICULTY))
			#$ 循环一次，循环次数减1，直到为0
			n -= 1
			#$ 循环结束把随机数列表 return 回去
		return keeper_num

#$ 玩家输入姓名
name = input("请输入您的姓名:")
#$ 守门员，随机生成一个大写字母当作守门员的name
name1 = chr(random.randint(65,90))
#$ 实例化 守门员
k1 = keeper(name1,0)
#$ 实例化 玩家
p1 = player(name,0)






