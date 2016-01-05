#!/usr/bin/env python
#地区字典，摘取了一部分
dir = {'北京市':{'北京直辖市':['东城区','西城区','崇文区','宣武区','朝阳区','丰台区','石景山区','海淀区','门头沟区','房山区','通州区','顺义区','昌平区','大兴区','怀柔区','平谷区','密云县','延庆县']},
	   '河南省':
		   {'郑州市':['中原区','二七区''金水区','上街区','新密市','新郑市','登封市'],
	   		'驻马店市':['驿城区','西平县','上蔡县','平舆县','正阳县','确山县','泌阳县','汝南县','遂平县','新蔡县'] }
	}
#生成一个省的列表
ShengList = []
for i in dir.keys():
    ShengList.append(i)
#程序开始
while True:
	#打印省列表
	for i in range(len(ShengList)):
		print(i + 1 ,ShengList[i])
	Sheng = input('请输入省或直辖市(输入b返回上一级，输入q退出程序）：')
	#如果输入的省在省列表里面，就生成一个市的字典和市的列表
	if Sheng in ShengList:
		ShiDir = {}
		ShiDir = dir.get(Sheng)
		ShiList = []
		for i in ShiDir.keys():
			ShiList.append(i)
		#市的程序开始
		while True:
			for i in range(len(ShiList)):
				print(i + 1 ,ShiList[i])
			Shi = input('请输入市或区(输入b返回上一级，输入q退出程序）：')
			#如果输入的市在市列表里面，就生成一个区的列表
			if Shi in ShiList:
				QuList = []
				QuList = ShiDir.get(Shi)
				#区的列表开始
				while True:
					for i in range(len(QuList)):
						print(i + 1 ,QuList[i])
					Qu = input('请输入区或县(输入b返回上一级，输入q退出程序）：')
					#如果输入的区在区的列表中，就打印信息，程序退出
					if Qu in QuList:
						print('你来自%s,%s,%s'%(Sheng,Shi,Qu))
						exit()
					elif Qu == 'b':
						break
					elif Qu == 'q':
						exit()
					else:
						continue
			elif Shi == 'b':
				break
			elif Shi == 'q':
				exit()
			else:
				continue
	elif Sheng == 'b':
		break
	elif Sheng == 'q':
		exit()
	else:
		continue
