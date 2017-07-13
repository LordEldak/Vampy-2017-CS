grade = input("What grade is your child in?:")
lastName = input("What is your last name?:")
if grade in [0,1,2] and "A"<= lastName and lastName < "G":
	print("Your child's picture will be taken between 7:00 and 7:50 AM on Monday.")
elif grade in [0,1,2] and "G"<= lastName and lastName < "N":
	print("Your child's picture will be taken between 7:50 and 8:40 AM on Monday.")
elif grade in [0,1,2] and "N"<= lastName and lastName < "R":
	print("Your child's picture will be taken between 8:40 and 9:30 AM on Monday.")
elif grade in [0,1,2] and "R"<= lastName and lastName < "U":
	print("Your child's picture will be taken between 9:30 and 10:20 AM on Monday.")
elif grade in [0,1,2] and "U"<= lastName and lastName <= "Z":
	print("Your child's picture will be taken between 10:20 and 11:10 AM on Monday.")

elif grade in [3,4,5] and "A"<= lastName and lastName < "G":
	print("Your child's picture will be taken between 11:10 AM and 12:00 PM on Monday.")
elif grade in [3,4,5] and "G"<= lastName and lastName < "N":
	print("Your child's picture will be taken between 12:00 and 12:50 PM on Monday.")
elif grade in [3,4,5] and "N"<= lastName and lastName < "R":
	print("Your child's picture will be taken between 12:50 and 1:40 PM on Monday.")
elif grade in [3,4,5] and "R"<= lastName and lastName < "U":
	print("Your child's picture will be taken between 1:40 and 2:30 PM on Monday.")
elif grade in [3,4,5] and "U"<= lastName and lastName <= "Z":
	print("Your child's picture will be taken between 2:30 and 3:20 PM on Monday.")

elif grade in [6,7,8] and "A"<= lastName and lastName < "G":
	print("Your child's picture will be taken between 7:00 and 7:50 AM on Tuesday.")
elif grade in [6,7,8] and "G"<= lastName and lastName < "N":
	print("Your child's picture will be taken between 7:50 and 8:40 AM on Tuesday.")
elif grade in [6,7,8] and "N"<= lastName and lastName < "R":
	print("Your child's picture will be taken between 8:40 and 9:30 AM on Tuesday.")
elif grade in [6,7,8] and "R"<= lastName and lastName < "U":
	print("Your child's picture will be taken between 9:30 and 10:20 AM on Tuesday.")
elif grade in [6,7,8] and "U"<= lastName and lastName <= "Z":
	print("Your child's picture will be taken between 10:20 and 11:10 AM on Tuesday.")

elif grade in [9,10,11,12] and "A"<= lastName and lastName < "G":
	print("Your child's picture will be taken between 11:10 AM and 12:00 PM on Tuesday.")
elif grade in [9,10,11,12] and "G"<= lastName and lastName < "N":
	print("Your child's picture will be taken between 12:00 and 12:50 PM on Tuesday.")
elif grade in [9,10,11,12] and "N"<= lastName and lastName < "R":
	print("Your child's picture will be taken between 12:50 and 1:40 PM on Tuesday.")
elif grade in [9,10,11,12] and "R"<= lastName and lastName < "U":
	print("Your child's picture will be taken between 1:40 and 2:30 PM on Tuesday.")
elif grade in [9,10,11,12] and "U"<= lastName and lastName <= "Z":
	print("Your child's picture will be taken between 2:30 and 3:20 PM on Tuesday.")

