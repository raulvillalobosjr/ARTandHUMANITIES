def get_first_value(number_list):
	return number_list[0]

def football_points(wins, draws, losses):
	return (wins*3)+draws

def animals(chickens, cows, pigs):
	return (chickens*2)+((cows+pigs)*4)

def name_string(name):
	  b = "Github"
	  result = name + b
	  return result

def bool_to_string(flag):
	return str(flag)

def give_me_something(a):
	return "something " + a

def points(twopointers, threepointers):
	return (twopointers*2)+(threepointers*3)

def get_last_item(lst):
	return lst[-1]

def hello_name(name):
	return "Hello " + name +"!"

def is_equal(obj_one, obj_two):
	return obj_one==obj_two

def profitable_gamble(prob, prize, pay):
	return((prob*prize)-pay)>0

def comp(txt1, txt2):
	return len(txt1)==len(txt2)

def is_empty(s):
	return len(s)==0

def repetition(txt, n):
	return txt*n

def front3(txt):
	if len(txt)<=3:
		return txt*3
	else:
		return txt[0:3]*3

def concat_name(first_name, last_name):
	return last_name + ", " + first_name

def total_amount_adjectives(dct):
	return len(dct)
