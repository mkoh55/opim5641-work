# def sum(k):
	# last solution first
# 	if k>0:
	# otherwise do:
# 		return sum(k-1)+k
# 	return 0

# print(sum(5))


# ((base^decimal_place)*letter_position_minus_one)
# pattern for 5 decimal places:

# ((26^0)*)+
# ((26^1)*)+
# ((26^2)*)+
# ((26^3)*)+
# ((26^4)*)+1
# =  tries

def brute_force_recursively(target=100, position=0, base=10, decimal_places=0):
	if position == decimal_places:
		return 1

# print(brute_force_recursively(23, 0, 26, 1))