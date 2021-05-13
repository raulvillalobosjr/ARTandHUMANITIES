import math

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

def is_safe_bridge(s):
	return " " not in s
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

def first_last(name):
  return name[0]+name[-1]

def odd_or_even(word):
	return (len(word))%2==0

def greeting(name):
	if name == "Mubashir":
		return "Hello, my Love!"
	else:
		return "Hello, " + name + "!"

def num_to_dashes(num):
	return "-"*num

def is_plural(word):
	return word[-1]=="s"

def is_last_character_n(word):
	return word[-1] in "nN"

def get_container(product):
	matches = {
	"Bread" : "bag",
	"Milk" : "bottle",
	"Beer" : "bottle",
	"Eggs" : "carton",
	"Cerials" : "box",
	"Candy" : "plastic",
	"Cheese" : None
	}
	return matches[product]

def long_burp(num):
	return "Bu" +("r"*num)+"p"

def remove_numbers(string):
    return "".join(i for i in string if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def new_word(word):
	return word[1:]

def birthday_cake_candles(candles):
	high = sorted(candles)[-1]
	num = []
	for i in candles:
		if i == high:
			num.append(i)
	return len(num)

def has_spaces(txt):
	return " " in txt

def programmers(one, two, three):
	lst = [one, two, three]
	return max(lst) - min(lst)

def first_last(lst):
	return [lst[0], lst[-1]]

def how_many_times(num):
	return "Ed" + (num*"a")+ "bit"

def should_serve_drinks(age, on_break):
	if age >= 18 and on_break==False:
		return True
	else:
		return False

def repeat_string(txt, n):
	if isinstance(txt, str):
		return txt*n
	else:
		return "Not A String !!"

def how_many_walls(n, w, h):
	return math.floor(n/(w*h))

def equal_slices(total, people, each):
	return people*each<=total

def wumbo(words):
	lst=[]
	for i in words:
		if i == "M":
			lst.append("W")
		else:
			lst.append(i)
	return "".join(lst)

def match(s1, s2):
	return s1.lower() == s2.lower()

def potatoes(potato):
	return potato.count("potato")

def get_fillings(sandwich):
	return sandwich[1:-1]

def count_claps(txt):
	return txt.count("C")

def has_same_bread(lst1, lst2):
	return [lst1[0],lst1[-1]] == [lst2[0],lst2[-1]]

def googlify(n):
	if n >= 2:
		return "G"+("o"*n)+"gle"
	else:
		return "invalid"

def count_syllables(txt):
	lst=[]
	for i in txt:
		if i.lower() in "aeiou":
			lst.append(i)
	return len(lst)

def fifty_thirty_twenty(ati):
	needs= ati*0.5
	wants= ati*0.3
	savings= ati*0.2
	return {"Needs": needs, "Wants": wants, "Savings": savings}

def count_d(sentence):
	cap=sentence.count("D")
	low=sentence.count("d")
	return cap+low

def how_many_stickers(n):
	return ((n*n)*6)

def maximumWealth(accounts):
    lst=[]
    for i in accounts:
        lst.append(sum(i))
    return max(lst)

def kidsWithCandies(candies, extraCandies):
    lst=[]
    top=max(candies)
    for i in candies:
        if (i + extraCandies) >= top:
            lst.append(True)
        else:
            lst.append(False)
    return lst

def numJewelsInStones(jewels, stones):
    lst=[]
    for i in stones:
        if i in jewels:
            lst.append(i)
    return len(lst)

def rotate_by_one(lst):
	lsti=[]
	lsti.append(lst[-1])
	for i in lst[:-1]:
		lsti.append(i)
	return lsti

def forbidden_letter(char, lst):
	st=[]
	if lst == []:
		st = True
	else:
		for i in lst:
			if char in i:
				st = False
				break
			else:
				st=True
	return st

def add(char, txt):
	return txt.replace(" ", char)

def smash_factor(bs, cs):
	return round(bs/cs,2)

def distance_home(lst):
    if sum(lst)<0:
	    return -(sum(lst))
    else:
	    return sum(lst)

def yen_to_usd(yen):
	return round(yen/107.5,2)

def check_title(txt):
    lst=[]
    lsti=[]
    for i in txt.split(" "):
        if i[0] == i[0].upper():
            lst.append(i)
        else:
            lsti.append(i)
    return len(lsti)==0

def create_id(firstname, lastname):
    lst=[]
    lst.append(firstname[0].lower())
    lst.append(lastname.capitalize()[:3])
    return "".join(lst)
