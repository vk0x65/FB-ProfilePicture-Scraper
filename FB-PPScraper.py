#Script by Mostafa Mohamed (VK ALFY)
#https://www.facebook.com/VKALFY

import sys
a_file = open("ID.txt", "r")
list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line
  list_of_lists.append(line_list)
a_file.close()
LIST = list(list_of_lists)
sys.stdout = open("URL.txt", "w")
for i in range (len (LIST)):
	print("https://graph.facebook.com/{}/picture?width=1200".format(LIST[i]))
sys.stdout.close()

print("URL Fetching Done , Check URL.txt File ♥")