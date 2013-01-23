#!/usr/bin/python

import binascii
import os
import sys


def main(argv):
	try:

		if len(argv) != 3:
			raise ValueError

		#TODO: validate color format
		#TODO: accept for #aaaaaa, #aaa, aaaaaa, aaa
		#TODO: add color mode flag for hsb/cmwk/lab

		color = argv[1].lstrip("#") 
		name = "#" + color

		R = color[:2]
		G = color[2:4]
		B = color[4:6]

		aco = open(argv[2], "wb")

		# spec according to http://www.nomodes.com/aco.html
		# version 1 in ico is not relevant to latest version of PS

		#      version| #colors| c_space |R| G| B| ---- 
		x =  " 0001     0001     0000     %x %x %x 0000" % (int(R,16)*256, int(G,16)*256, int(B,16)*256)
		x += " 0002     0001     0000     %x %x %x 0000" % (int(R,16)*256, int(G,16)*256, int(B,16)*256)

		#      ---- | len(name)+1 | name | ----
		x += " 00 00  %04x          %s     00 00" % (len(name)+1, "".join([binascii.hexlify(letter).zfill(4) for letter in name]))

		x = "".join(x.split(" "))

		aco.write(binascii.a2b_hex(x))
		aco.close()

		print "Successfully created %s" % (argv[2]) 

	except ValueError:
		print "usage: %s <#RGBHEX> <outputfile.aco>" % (argv[0])
		sys.exit(2)


if __name__ == "__main__":
	main(sys.argv)

