#!/usr/bin/env python

UserName = input('请输入用户名：')
#判断输入的用户名是否为空
if len(UserName) != 0:
	#判断用户名是否被锁定，锁定提示锁定，没有锁定提示输入密码
	f = open('lock_user.txt','r+')
	if UserName not in f.readline():
		f.close()
		#循环3次，密码输入正确退出程序
		for i in range(3):
			Password = input('请输入密码：')
			if len(Password) != 0:
				#用户名和密码拼凑为一个数组
				UserPass = UserName + ':' + Password + '\n'
				f2 = open('user.txt','r+')
				f3 = f2.readlines()
				f2.close()
				#判断这个数组，是否存在这个文件。用来验证用户名和密码。
				if UserPass not in f3:
					print('密码错误:')
					continue
				else:
					print('登陆成功')
				break
		else:
			#密码输入次数过多，把用户写入锁定文件
			LockList = open('lock_user.txt','a+')
			LockList.write( UserName +  '\n')
			LockList.flush()
			LockList.close()
			print('帐号密码输入次数过多，锁定')
	else:
		f.close()
		print('用户已经被锁定：')
else:
	print('用户名不能为空\n请重新运行程序')



