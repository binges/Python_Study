#!/usr/bin/env python

#打开user，生成一个用户列表UserList
UserList = []
f = open('user.txt','r+')
for i in f:
	u = i.split(':')
	UserList.append(u[0])
f.close()
NewUser = input('请输入用户名：')
#判断输入的用户名是否为空
if len(NewUser) != 0:
#判断用户是否存在，不存在提示输入密码，存在提示用户已经存在
	if NewUser not in UserList:
		Password1 = input('请输入密码：')
		if len(Password1) != 0:
			Password2 = input('确认密码：')
			#判断两次输入的密码是否一致,密码一致写入user
			if Password1 == Password2:
				f2 = open('user.txt','a+')
				f2.write( NewUser + ':' + Password1 + '\n')
				f2.flush()
				f2.close()
				print('注册成功\n请执行登陆程序')
			else:
				print('密码不一致')
		else:
			print('密码不能为空')
	else:
		print('用户已经存在\n请执行登陆程序')
else:
	print('用户名不能为空\n请重新运行程序')


