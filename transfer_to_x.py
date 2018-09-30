# this piece of code will convert strings like "8D4C2404" into "\x8D\x4C\x24\x04"
# which will then be disassembled by capstone and print the machine code  

import sys
from capstone import *

# print("the hex string is " + sys.argv[1])

the_str = sys.argv[1]
def x_encode(str):
	the_str_len = len(str)
	count = 0
	the_x_str = r"\x"  # \x is not some kind of encodeing. It is an escape character, the fllowing two characters will be interpreted as hex digit
					   # in order not to escape here, we need raw string to stop character escaping
	while 1:
		the_x_str = the_x_str + sys.argv[1][count:count+2] + r"\x"
		count += 2
		if count == the_str_len:
			return(the_x_str[:-2].decode("string_escape"))  # this will convert raw string into normal string

def x_disassem(str):
	CODE = str
	# CODE = "\x89\xe5"
	# print(type(CODE))
	md = Cs(CS_ARCH_X86, CS_MODE_64)
	for i in md.disasm(CODE, 0x1000):
		print "0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str)

x_disassem(x_encode(the_str))

