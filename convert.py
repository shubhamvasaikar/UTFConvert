#!/usr/bin/python3

utf16hex = eval(input("Enter the UTF-16 Hex code: (Format: 0xXXXX): "));

print("Original UTF-16 hex code: " + hex(utf16hex))

if(utf16hex >= 0x00) and (utf16hex <=0x007f):
	utf8hex = utf16hex
	print("\nBit representation of converted code: ");
	print("Byte1 : " + bin(utf8hex));	
	
elif(utf16hex >= 0x0080) and (utf16hex <=0x07ff):	# Example input 0xA2: 000 10100010
	utf8byte1 = utf16hex >> 6			# 00000010
	utf8byte1 = utf8byte1 + 0xc0			# 00000010 + 11000000 = 11000010 = 0xC2
	
	utf8byte2 = utf16hex & 0x3f			# 000 10100010 & 000 00111111 = 00100010
	utf8byte2 = utf8byte2 + 0x80			# 00100010 + 10000000 = 10100010 = 0xA2
	
	utf8byte1 = utf8byte1 << 8
	utf8hex = utf8byte1 + utf8byte2			# 11000010 10100010 = C2 A2
	utf8byte1 = utf8byte1 >> 8
		
	print("\nBit representation of converted code: ");
	print("Byte1 : " + bin(utf8byte1));
	print("Byte2 : " + bin(utf8byte2));	
	
print("\nHex code of UTF-16 converted to UTF-8: " + hex(utf8hex))
