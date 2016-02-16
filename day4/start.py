#!/usr/bin/env python3
import re

#$ 加减的函数
def JiaJian(data):
	while True:
		if data.__contains__('+-') or data.__contains__("++") or data.__contains__('-+') or data.__contains__("--"):
			#$ 加减为减
			data = data.replace('+-','-')
			#$ 加加为加
			data = data.replace('++','+')
			#$ 减加为减
			data = data.replace('-+','-')
			#$ 减减为加
			data = data.replace('--','+')

		else:
			break
	#$ 加减符号
	jiajian = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', data)
	#$ 如果没有加减符合，则直接返回结果
	if not jiajian:
		return data
	#$ 匹配到加减符号
	jiajianlist = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', data).group()
	#$ 如果匹配到加号
	if len(jiajianlist.split('+')) > 1:
		#$ n1 等于加号前面的数，n2 等于加号后面的数
		n1,n2 = jiajianlist.split('+')
		#$ 计算两个数的和
		jieguo = float(n1) + float(n2)
	else:
		#$ 如果没有匹配到加号，就是匹配到减号，下面的操作和上面的一样
		n1,n2 = jiajianlist.split('-')
		jieguo = float(n1) - float(n2)
	#$ 取出这个计算结果前后的数字
	qian,hou = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', data, 1)
	#$ 拼接成一个新的表达式
	new_data = "%s%s%s" % (qian,jieguo,hou)
	#$ 新的表达试重新赋值给 data
	data = new_data
	#$ 继续计算
	JiaJian(data)


#$ 乘除的函数，方法是和上面加减一样
def ChengChu(data):
	chengchu = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', data)
	if not chengchu:
		return
	chengchulist = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', data).group()
	if len(jiajianlist.split('*')) > 1:
		n1,n2 = jiajianlist.split('*')
		jieguo = float(n1) * float(n2)
	else:
		n1,n2 = jiajianlist.split('/')
		jieguo = float(n1) / float(n2)
	qian,hou = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', data, 1)
	new_data = "%s%s%s" % (qian,jieguo,hou)
	data = new_data
	ChengChu(data)

#$ 取括号的函数
def KuoHao(data):
	#$ 判断是否有括号
	if not re.search('\(([\+\-\*\/]*\d+\.*\d*){1,}\)', data):
		#$ 没有括号把 data 传给乘除函数操作
		jieguo = ChengChu(data)
		#$ 乘除函数操作完之后，把 data 传给加减函数操作
		jieguo = JiaJian(data)
		return jieguo
	#$ 取出括号内的表达式
	kuohaolist = re.search('\(([\+\-\*\/]*\d+\.*\d*){1,}\)', data).group()
	#$ 把括号内的表达式传给乘除函数操作
	jieguo = ChengChu(kuohaolist)
	#$ 然后再传给加减函数操作
	jieguo = JiaJian(kuohaolist)
	#$ 取出括号前后的表达式
	qian,hou = re.split('\(([\+\-\*\/]*\d+\.*\d*){1,}\)', data, 1)
	#$ 拼接成一个新的表达式
	new_data = "%s%s%s" % (qian,jieguo,hou)
	#$ 把新的表达式赋值给 data
	data = new_data
	#$ 再次调用括号的函数，继续去除括号
	KuoHao(data)
	#$ 最后返回结果
	return jieguo


if __name__ == "__main":
	data = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
	#$ 去除空格
	data = re.sub('\s*','',data)
	n = KuoHao(data)
	print(n)

