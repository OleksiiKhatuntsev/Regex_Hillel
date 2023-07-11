import re

string_1 = "My name is Alex. I'm from Kharkiv."
# # pattern_ex = r"[a-z]{2}"
# pattern = re.compile(r"[a-z]{2}")
# matches = pattern.findall(string_1)
#
# print(matches)
#
# print(r"abc\ncde\n")

# pattern = re.compile(r"[\w'\s]*\.")
# matches = pattern.findall(string_1)
# print(matches)


# phones = "+380671234567, 380930987654, 0631234567"
# pattern = re.compile(r'\+{0,1}\d{10,}')
# matches = pattern.finditer(phones)
#
# for match in matches:
#     print(match)

emails = "testmail@gmail.com, test_mail@outlook.com, test-123-mail@icloud.com"

pattern = re.compile('[\w-]{1,}@gmail.com|[\w-]{1,}@outlook.com|[\w-]{1,}@icloud.com')
pattern2 = re.compile(r"([\w-]*)@(gmail|outlook|icloud)(.com)")
matches = pattern2.finditer(emails)
sub = pattern2.sub(r"\1" ,emails)

for match in matches:
    print(match)


str_2 = '''
abc
basd
gfjklsd;
ads
'''
str_3 = """
abc
basd
gfjklsd;
ads
"""
