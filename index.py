s = "(2,1)(3,3)"
point1 = tuple(map(int, s[1:4].split(",")))
point2 = tuple(map(int, s[6:9].split(",")))
w = max(point1[0], point2[0]) - min(point1[0], point2[0]) + 1
h = max(point1[1], point2[1]) - min(point1[1], point2[1]) + 1

print(w,h)



# import keyword
# import random

# # Get all Python keywords as a list
# keywords = "False None range len for return >= True and as if break class len [i] continue range def del elif else except for > from if in len is lambda if return nonlocal () not or > pass for raise return <= for try while for len with return False None range len for return >= True and as if break class len [i] continue range def del elif else except for > from if in len is lambda if return nonlocal () not or > pass for raise return <= for try while for len with return False None range len for return >= True and as if break class len [i] continue range def del elif else except for > from if in len is lambda if return nonlocal () not or > pass for raise return <= for try while for len with return False None range len for return >= True and as if break class len [i] continue range def del elif else except for > from if in len is lambda if return nonlocal () not or > pass for raise return <= for try while for len with return False None range len for return >= True and as if break class len [i] continue range def del elif else except for > from if in len is lambda if return nonlocal () not or > pass for raise return <= for try while for len with return False None range len for return >= True and as if break class len [i] continue range def del elif else except for > from if in len is lambda if return nonlocal () not or > pass for raise return <= for try while for len with return ".split(" ")

# # Randomize the order of keywords
# random.shuffle(keywords)

# # Join the randomized keywords list into a single string separated by a space
# keywords_string = ' '.join(keywords)

# print(keywords_string)
