def menu_select(num):
	if(num == 1):
		binary = input("Enter binary number: ")
		decimal = binary_to_decimal(binary)
		return(decimal)
		
	elif(num == 2):
		decimal = input("Enter decimal number: ")
		binary = decimal_to_binary(decimal)
		return(binary)
		

def binary_to_decimal(num):
	b = list(num)
	n = len(list(num))
	decimal = 0
	hold = 0
	i = 0
	exp = n-1
	while (i < n):
		x = int(b[i])
		quot= 2**exp
		hold = x*quot
		i += 1
		exp -= 1
		decimal = decimal + hold
	return(decimal)

def decimal_to_binary(num):
	quot = int(num)
	base = 0
	counter = 0
	binary=[]
	while (quot > 0):
		rem = quot%2
		binary.append(str(rem))
		quot = quot//2
		counter +=1

	binary.reverse()
	return(int(''.join(binary)))

# assert binary_to_decimal(0) == 0, "0 to decimal should return 0"
# assert binary_to_decimal(1011) == 11, "1011 to decimal should return 11"
# assert binary_to_decimal(101011) == 43, "101011 to decimal should return 43"
# assert binary_to_decimal(101011101) == 349, "101011101 to decimal should return 349"
#
# assert decimal_to_binary(0) == 0, "0 to binary should return 0"
# assert decimal_to_binary(5) == 101, "5 to binary should return 101"
# assert decimal_to_binary(10) == 1010, "10 to binary should return 1010"
# assert decimal_to_binary(113) == 1110001, "113 to binary should return 1110001"


print("Binary-Decimal Converter\n")
print("What type do you want to convert? : \n")
print("1- Binary\n")
print("2- Decimal\n")

choice = input("Select: ")
s = menu_select(int(choice))
print("Result : ", s)
