# ip -> 121.222.212.4
# (0 - 255)
# only digit
# 1-3 chars per sequence
# 4 sets of numbers structure
# No importing

# Write a function which check validity of ip
# use split()

# def ip_check(x: str) -> bool:
#     y = x.split('.')
#     b = True
#
#     # check if IP contains 4 sets of number structures
#     if len(y) == 4:
#         print("The IP contains 4 sets")
#     else:
#         print("This IP is not valid, length")
#         b = False
#
#     # check if IP is only digits
#     g = bool
#     for i in y:
#         if i.isdigit():
#             g = True
#         else:
#             g = False
#             b = False
#             break
#     if g:
#         print("The IP is only digits")
#     else:
#         print("The IP contains chars")
#
#     # check if each structure is <= 255
#     t = bool
#     for i in y:
#         if i.isdigit():
#             if (int(i) <= 255) and (int(i) >= 0):
#                 t = True
#         else:
#             t = False
#             b = False
#             break
#     if t:
#         print("Each structure is >= 0 and <= 255")
#     else:
#         print("The IP is invalid, structure is <0 or > 255")
#
#     # checks for overall success
#     if b:
#         print("Overall success")
#     else:
#         print("Failure")
#     return b
#
#
# class IpChecker:
#
#     ip = None
#     ip_arr = []
#
#     def __init__(self):
#         pass
#
#     def __set_ip(self, ip):
#         self.__split(ip)
#
#     def __split(self):
#         try:
#             self.ip_arr = self.ip.split('.')
#         except:
#             print("Unable to parse ip string")
#
#     def __check_four_parts(self):
#         try:
#             if len(self.ip_arr) == 4:
#                 return True
#             else:
#                 print("Incorrect number of segments")
#                 raise ValueError
#         except Exception as e:
#             return False
#
#     def __check_ip_range(self):
#         try:
#             return all([(0 <= int(i) <= 255) for i in self.ip_arr])
#         except Exception as e:
#             print("Invalid IP range:", e)
#             return False
#
#     def is_valid(self, ip):
#         self.ip = ip
#         self.__split()
#         return all([
#             self.__check_four_parts(),
#             self.__check_ip_range()
#         ])
#
#
# ip_check = IpChecker()
#
# ip_list = [
#     "121.2.222.4",
#     "1.0.1",
#     "1.0.12g.1",
#     "1.0.-23.11"
# ]
# for ip in ip_list:
#     print(f'checking ip: {ip}')
#     print(f'{ip_check.is_valid(ip)}\n')


# ip = Ip("1.1.1.1")
# print(ip.expand())



# 2
# Break the following string into a array and strings
# Cannot use split function

# s = "lets go to the mall today and buy some icecream"
# lst = []
# string = ''
# for idx, i in enumerate(s):
#     if i != " ":
#         string += i
#     if i == " " or (idx == len(s) - 1):
#         lst.append(string)
#         string = ''
#
# # if string:
# #     lst.append(string)
#
# print(lst)


# 3
# Create a dictionary where key: word and value: count of word
s = ("lets go to the mall today and buy some icecream yah but some days the mall is closed i heard its because of the "
     "demon janitor... tsk tsk tsk")


def counts(string):
    words_dict = {}
    # words = string.split()
    words = []
    string = ''
    for idx, i in enumerate(s):
        if i != " ":
            string += i
        if i == " " or (idx == len(s) - 1):
            words.append(string)
            string = ''

    for word in words:
        clean = word.strip(",.?!")

        if clean in words_dict:
            words_dict[clean] += 1
        else:
            words_dict[clean] = 1
    return sorted(words_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)


print(counts(s))


# example
# dict = {
#     'tsk': 3,
#     'lets': 1
# }

# how to insert into dictionary
# dict[key] = 1
