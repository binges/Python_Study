#!/usr/bin/env python3
import json

#$ 定义查看的函数
def See(data):
	#$ 定义文件的开头
	input_list = 'backend %s' % data
	#$ 定义配置列表
	conf_list = []
	#$ 开始读取文件
	with open('ha.txt') as f:
		flag = False
		for key in f:
			key = key.strip()
			#$ 如果文件和定义的开头一样,则跳出本次循环
			if key == input_list:
				flag = True
				continue
			#$ 下次循环从定义的开头开始
			if flag and key.startswith('backend'):
				flag = False
				break
			if flag and key:
				conf_list.append(key)
	return conf_list


def Add(data):
	data_l = data.get('backend')
	l = See(data_l)
	add_list = "server %s %s weight %d maxconn %d" % (data['record']['server'], data['record']['server'], data['record']['weight'], data['record']['maxconn'])
	with open('ha.txt','a+') as f:
		for i in f:
			i = i.strip()
			if i == l:
				f.write('%s%s\n'%(8*' ' ,add_list))
				f.flush()
	return l


print('1、获取；2、添加；3、删除')
num = input('请输入序号：')
data = input('请输入内容：')
if num == '1':
	print(See(data))
else:
	data = json.loads(data)
	if num == '2':
		print(Add(data))







