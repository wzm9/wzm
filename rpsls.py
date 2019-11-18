#coding:gbk
"""
程序目标：通过自定义函数，用户通过键盘输入任意一个选择（石头/剪刀/布/蜥蜴/史波克），计算机自动生成一个随机选择，根据RPSLS规则，产生最终的结果
作者：文正梅
"""

def name_to_number(n):
	"""
	调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
	"""
	if n=="石头":
		return 0
	elif n=="史波克":
		return 1
	elif n=="布":
		return 2
	elif n=="蜥蜴":
		return 3
	elif n=="剪刀":
		return 4
		return(n)
		
import random
comp_number=random.randint(1,4)
def number_to_name(number):
	"""
	 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
	"""
	if number==0:	
		return "石头"
	elif number==1:
		return "史波克"
	elif number==2:
		return "布"
	elif number==3:
		return "蜥蜴"
	elif number==4:
		return "剪刀"
	return(number)

def rpsls(player_choice):
	player_choice_number = name_to_number(player_choice)
	com_choice = number_to_name(comp_number)
	print("             ")
	print("计算机的选择为: %s"%com_choice)
	print("您的选择为: %s"%player_choice)
	if player_choice_number==0 and comp_number==4:
		print("Wow,你真是太棒了！")
	elif player_choice_number==0 and comp_number==3:
		print("Wow,你真是太棒了！")
	elif player_choice_number==0 and comp_number==1:
		print("唉，继续加油吧")
	elif player_choice_number==0 and comp_number==2:
		print("唉，继续加油吧")
	elif player_choice_number==1 and comp_number==4:
		print("Wow,你真是太棒了！")
	elif player_choice_number==1 and comp_number==0:
		print("Wow,你真是太棒了！")
	elif player_choice_number==1 and comp_number==2:
		print("唉，继续加油吧")
	elif player_choice_number==1 and comp_number==3:
		print("唉，继续加油吧")
	elif player_choice_number==2 and comp_number==0:
		print("Wow,你真是太棒了！")
	elif player_choice_number==2 and comp_number==1:
		print("Wow,你真是太棒了！")
	elif player_choice_number==2 and comp_number==3:
		print("唉，继续加油吧")
	elif player_choice_number==2 and comp_number==4:
		print("唉，继续加油吧")
	elif player_choice_number==3 and comp_number==1:
		print("Wow,你真是太棒了！")
	elif player_choice_number==3 and comp_number==2:
		print("Wow,你真是太棒了！")
	elif player_choice_number==3 and comp_number==4:
		print("唉，继续加油吧")
	elif player_choice_number==3 and comp_number==0:
		print("唉，继续加油吧")
	elif player_choice_number==4 and comp_number==2:
		print("Wow,你真是太棒了！")
	elif player_choice_number==4 and comp_number==3:
		print("Wow,你真是太棒了！")
	elif player_choice_number==4 and comp_number==0:
		print("唉，继续加油吧")
	elif player_choice_number==4 and comp_number==1:
		print("唉，继续加油吧")
	elif player_choice_number==comp_number:
		print("平局")
	else:
		print("Error: No Correct Name")

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
player_choice=input()
rpsls(player_choice)
	
	
	
	
