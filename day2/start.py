#!/usr/bin/env python3
#商品列表
ShangPinList = [('MacBook',9280),('iPhone6',4488),('55寸平板电视',3999),('洗衣机',1999),('冲锋衣裤',999),('登山鞋',599),('咖啡机',399),('速溶咖啡',199),('面包机',59),('彩票',2)]
#定义一个购物车内的列表
GouWuList = []
#输入一个金额，转换为int型，为了后面的价格计算
num = int(input('请输入您的资金：'))
print('欢迎来到瓜子购物')

#输出商品列表，并把索引值加1
for i in range(len(ShangPinList)):
	print(i + 1,ShangPinList[i])#开始循环，购物开始
while True:
	BianHao = input('请输入你所要购买商品的编号，输入q结束购物')
	#判断如果输入q，表示结束购物。打印出购物车里面的内容，和余额。退出程序
	if BianHao == 'q':
		print('您购买的商品有 %s，\n余额为 %s,'%(GouWuList,num))
		print('欢迎下次再来')
		break
	#判断输入的编号减1是否小于等于，商品的个数
	elif (int(BianHao) - 1) <= len(ShangPinList):
		#赋值商品的名称和价格
		ShangPin,JiaGe = ShangPinList[int(BianHao) - 1]
		#判断价格是否小于余额
		if JiaGe <= num:
			#如果小于余额，余额减去商品的价格，生成新的余额。
			num -= JiaGe
			#新的商品添加到购物车里面
			GouWuList.append(ShangPin)
			print('您购买的商品有 %s，\n余额为 %s,'%(GouWuList,num))
			continue
		else:
			#如果商品的价格大于余额，就显示余额不足。
			print('余额不足')
			print('余额为 %s,'%(num))
			continue
	else:
		continue

