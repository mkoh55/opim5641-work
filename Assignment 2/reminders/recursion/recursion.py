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
	s = str(target)
	char = s[decimal_places - 1 - position]
	digit = ord(char)-ord('a') if char.isalpha() else int(char)
	return digit * base**position + brute_force_recursively(target, position + 1, base, decimal_places)


# print(brute_force_recursively(12, 0, 10, 2))
print(brute_force_recursively('000', 0, 26, 3))
print(brute_force_recursively('00a', 0, 26, 3))
print(brute_force_recursively('aaa', 0, 26, 3))
print(brute_force_recursively('a1a', 0, 26, 3))
print(brute_force_recursively('a1b', 0, 26, 3))
print(brute_force_recursively('a11', 0, 26, 3))
print(brute_force_recursively('abc', 0, 26, 3))
print(brute_force_recursively('apple', 0, 26, 5))


# a a a b a = 0 0 0 1 0 
# ((26^0)*0)+
# ((26^1)*1)+
# ((26^2)*0)+
# ((26^3)*0)+
# ((26^4)*0)+1
# = 27 tries
print(brute_force_recursively(10, 0, 26, 2))

# a a b c a = 0 0 1 2 0 = 
# ((26^0)*0)+
# ((26^1)*2)+
# ((26^2)*1)+
# ((26^3)*0)+
# ((26^4)*0)+1
# = 729 tries
print(brute_force_recursively('00120', 0, 26, 5))
print(brute_force_recursively('aabca', 0, 26, 5))

# a p p l e = 0 15 15 11 4
# ((26^0)*4)+
# ((26^1)*11)+
# ((26^2)*15)+
# ((26^3)*15)+
# ((26^4)*0)+1
# = 274071 tries
print(brute_force_recursively('apple', 0, 26, 5))

