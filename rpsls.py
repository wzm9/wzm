#coding:gbk
"""
����Ŀ�꣺ͨ���Զ��庯�����û�ͨ��������������һ��ѡ��ʯͷ/����/��/����/ʷ���ˣ���������Զ�����һ�����ѡ�񣬸���RPSLS���򣬲������յĽ��
���ߣ�����÷
"""

def name_to_number(n):
	"""
	����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
	"""
	if n=="ʯͷ":
		return 0
	elif n=="ʷ����":
		return 1
	elif n=="��":
		return 2
	elif n=="����":
		return 3
	elif n=="����":
		return 4
		return(n)
		
import random
comp_number=random.randint(1,4)
def number_to_name(number):
	"""
	 ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
	"""
	if number==0:	
		return "ʯͷ"
	elif number==1:
		return "ʷ����"
	elif number==2:
		return "��"
	elif number==3:
		return "����"
	elif number==4:
		return "����"
	return(number)

def rpsls(player_choice):
	player_choice_number = name_to_number(player_choice)
	com_choice = number_to_name(comp_number)
	print("             ")
	print("�������ѡ��Ϊ: %s"%com_choice)
	print("����ѡ��Ϊ: %s"%player_choice)
	if player_choice_number==0 and comp_number==4:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==0 and comp_number==3:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==0 and comp_number==1:
		print("�����������Ͱ�")
	elif player_choice_number==0 and comp_number==2:
		print("�����������Ͱ�")
	elif player_choice_number==1 and comp_number==4:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==1 and comp_number==0:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==1 and comp_number==2:
		print("�����������Ͱ�")
	elif player_choice_number==1 and comp_number==3:
		print("�����������Ͱ�")
	elif player_choice_number==2 and comp_number==0:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==2 and comp_number==1:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==2 and comp_number==3:
		print("�����������Ͱ�")
	elif player_choice_number==2 and comp_number==4:
		print("�����������Ͱ�")
	elif player_choice_number==3 and comp_number==1:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==3 and comp_number==2:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==3 and comp_number==4:
		print("�����������Ͱ�")
	elif player_choice_number==3 and comp_number==0:
		print("�����������Ͱ�")
	elif player_choice_number==4 and comp_number==2:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==4 and comp_number==3:
		print("Wow,������̫���ˣ�")
	elif player_choice_number==4 and comp_number==0:
		print("�����������Ͱ�")
	elif player_choice_number==4 and comp_number==1:
		print("�����������Ͱ�")
	elif player_choice_number==comp_number:
		print("ƽ��")
	else:
		print("Error: No Correct Name")

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()
rpsls(player_choice)
	
	
	
	
