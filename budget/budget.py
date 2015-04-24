
'''

A csv file is a very simple file that is used quite often. Usually a csv file will look something like this

A simple expenses csv file

---
name,amount,monthly
food,1000.00,y
rent,2000.00,y
braces,2000.00,n
---

A csv usually starts with a header line that lists the names of the fields so someone reading or importing it into a spreadsheet app knows what each column is for.

The task is to write a simple budget app. This application will have a simple interface that shows the list of commands to the user, and allows to enter a command and keep doing it until they say
quit. 

It will store the data it gets from the user in a csv file. 

The program will have the following commands

1. Open a file - should then ask the user for the file name to open
2. Save file
3. Show items in the budget - calculates the total amount of expenses
4. Add an item to the budget - should ask the user for each field name, amount, monthly
5. Remove an item from the budget

On open the program needs to read in the file data, and on save write out the changes. You can only use the tools shown, no extra modules.

To test you should be able to open the file in a spreadsheet application after closing.

'''

# glboal variables
import os

# store header as separate variable
# when you assign rows at open, create hash with information for each column
# saving goes from hash back to array (string)

# REFACTOR 

# setup as an ordered dictionary
# build csv file with keys from dictionary as header
# build csv file with values from dictioanry as csvs
# total function to change after ordered dictionary setup
# hashes and functions in UI loop
# separate functinos for array to csv and csv to array
# add commenting
# add exceptions



# open file (o)
def open_file():
	filename = raw_input("Filename: ")
	return filename


def run_file(filename):
	# check to see if file exists, if it does, open it and assign its contents to the rows array
	if os.path.exists(filename):
		with open(filename, "r") as f:
			return f.readlines()
			 
	# if file doesn't exist assign header to rows array
	else:
		return ['NAME,AMOUNT,MONTHLY\n']


# save file (which involves printing all items array to open file)
def save_file(filename, rows):
 	with open(filename, "w") as f:
 		for i in rows:
			f.write(i)


# calculate budget total
def total(rows):
	total = 0.00
	values = []
	# get amount value from each line
	for i, v in enumerate(rows):
		row = v.strip('').strip("\n").split(",")
		value = row[1]
		values.append(value)
	# delete "AMOUNT" from list
	del values[0]
	# sum values 
	for i in values:
		total += float(i)
	print "Total Budget: $" + str(total) #MAKE THIS A RETURN


# list items in the budget by iterating through the budget file
def print_file(rows):
	print "\n"
	for i, v in enumerate(rows):
		row = v.strip('').strip("\n").split(",")
		print str(i) + ") " + row[0] + " " + row[1] + " " + row[2]
	total(rows) #MAKE THIS PRINT TOTAL(ROWS)


# add and item to the budget
def add_item():
	print "\nEnter Item Details:"
	name = raw_input("Name: ")
	amount = raw_input("Amount: $")
	monthly = raw_input("Monthly (Y/N): ").lower()

	new_item = name + "," + amount + "," + monthly + "\n"

	#NEED TO APPEND TO ROWS
	#RETURN NEW ROWS ARRAY
	return new_item


# remove item
def remove_item(filename, rows):
	print_file(rows)
	remove_number = int(raw_input("\nDelete: #"))
	del rows[remove_number]
	return rows


#master function
def run_budget(): 

	print ("\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
		   "$$$$ $$$$$$$$$ $$$$$$$$$ $$$$$$$$$ $$$$$\n"
		   "$$     $$$$$     $$$$$     $$$$$     $$$\n"
		   "$$ $$$$$$$$$ $$$$$$$$$ $$$$$$$$$ $$$$$$$\n"
		   "$$     $$$$$     $$$$$     $$$$$     $$$\n"
		   "$$$$$$ $$$$$$$$$ $$$$$$$$$ $$$$$$$$$ $$$\n"
		   "$$     $$$$$     $$$$$     $$$$$     $$$\n"
		   "$$$$ $$$$$$$$$ $$$$$$$$$ $$$$$$$$$ $$$$$\n"
		   "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

	print "Let's build a budget.\n"

	# initiate with filename request
	# remove this step
	filename = open_file()
	rows = run_file(filename)

	# main menu loop
	while(True):

		print "\no)pen a different file\na)dd a new item\nd)elete an item\np)rint budget items\ns)ave\nq)uit\n"
		command = raw_input("Enter a command: ").lower() #obtains command from 
	
		if command == 'o': #open
			filename = open_file()
			rows = run_file(filename)
		elif command == 'a': #add an item
			new_row = add_item()
			rows.append(new_row)
		elif command == 'd': #delete 
			row = remove_item(filename, rows)
		elif command == 'p': #print 
			print_file(rows)
		elif command == 's': #save 
			save_file(filename, rows)
		elif command == 'q': #quit
			print "Adios"
			break


# run master
run_budget()













