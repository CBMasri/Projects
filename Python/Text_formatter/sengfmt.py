# Sengfmt.py
# Author: Carl Masri

import sys

# Variables
width = 75
margin = 0
fmt = 0
linecopy = ""
output = ""

# ---------------------------------------------------------------- #

def main():
	input = []
	
	# opens file from commad line
	try:
		file = open(sys.argv[1], 'r')
	except IndexError:
	# no file given, take input from stdin
		file = sys.stdin
	
	# reads file into string list, each string is a line of text
	with file:
		input = file.readlines()
	
	# goes through list line by line
	for line in input:
		parameters(line)
	
	# prints last line of file
	if output:
		output.rstrip('\n')
		print (output)
		
# ---------------------------------------------------------------- #

# this function takes a line from the input file and checks
# for any commands that it may contain
def parameters(line):
	
	lines = []
	
	global width
	global margin
	global fmt
	global linecopy
	global output
	
	# creates copy of unfomatted line
	linecopy = line
	
	# splits input line into list of words, removing whitespace
	lines = line.split()
	
	# prints empty lines
	if not lines:
		# if output is empty
		if not output:
			# print output
			print (output)
		else:
			# print output and add new line
			print (output + '\n')
		output = ""
	
	# if the line is nonempty
	elif lines:
	
		# if there is a commnd at the beginning of the line
		if (lines[0] == '?width' or lines[0] == '?fmt' or lines[0] == '?mrgn' or lines[0] == '?align'):
			
			# if the command is width
			if lines[0] == '?width':
				# set width and turn on formatting
				width = int(lines[1])
				fmt = 1
			
			# if the command is margin
			if lines[0] == '?mrgn':	
				# add margin
				if lines[1].startswith('+'):
					more = int(lines[1][1:])
					# if the new margin is greater than the width - 20
					if ((margin + more) > (width - 20)):
						# set margin to width - 20
						margin = width - 20
					else:
						margin += more
				# subtract margin
				elif lines[1].startswith('-'):
					less = int(lines[1][1:])
					# if the margin is less than 0
					if (margin - less) < 0:
						# set margin to 0
						margin = 0
					else:
						margin -= less
				# set margin
				else:
					margin = int(lines[1])
			
			# if the command is format
			if lines[0] == '?fmt':
				# turn on formatting
				if lines[1] == 'on':
					fmt = 1
					# removes '?fmt on' from linecopy
					linecopy = linecopy.partition('on ')[2]
				# else turn off formatting
				elif lines[1] == 'off':
					fmt = 0					
					# removes '?fmt off' from linecopy
					linecopy = linecopy.partition('off ')[2]
						
			# sends line (minus command) to be formatted		
			format_lines(lines[2:])
		
		# no command at line beginning, full line is sent for formatting
		else:
			format_lines(lines)
	
# ---------------------------------------------------------------- #

# this function takes a list of words from one line in the input file
# and formats it accordingly
def format_lines(line):
	
	global output
	
	# if formatting is off
	if (fmt == 0):
		if linecopy:
			# print unformatted line and return
			print (linecopy.rstrip('\n'))
		return
	
	# iterate through words in line
	for word in line:
	
		# if the output list is empty, add margin
		if (len(output) == 0):
			output += " " * margin
		
		# if the word will fit on the line
		if (len(output) + len(word) <= width):
			# add the word to the line
			output += word + " "
		
		# the word will not fit, print and start new line
		else:
			print (output.rstrip('\n'))		# prints line
			output = ""				# clear output for next line
			output += " " * margin			# adds margin to new line
			output += word + " "			# adds overflow word to new line

# ---------------------------------------------------------------- #

if __name__ == '__main__':
	main()
