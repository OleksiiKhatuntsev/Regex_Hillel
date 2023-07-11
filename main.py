first_str = "abc deg 123"
split_str = first_str.split('d')
print(split_str)


new_str = first_str.replace(' ', '1')
print(new_str)


case_str = "    ABC abc cde   "
print(case_str.upper())
case_str = case_str.lower()
print(case_str.count('a'))
print(case_str.strip())
print(case_str.rstrip())
# testmail@gmeil.com
# TestMail@gmail.com


# str = '[bdd] Check the motion'
# видалити [bdd] , всі інші зробити upper, записати в 1 строчку
# https://regex101.com/