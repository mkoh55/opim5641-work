# def sum(k):
# 	if k>0:
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

def brute_force_recursively(position=0, base=10, decimal_places=3, target=100)
print(brute_force_recursively(0, 26, 1, 23))