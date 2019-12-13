from itertools import accumulate # Used for accumulating total_points and total_hours

def gpa():

	user_input = { # User input map for converting numerical values to letter grades.
		1 : "A+",
		2 : "A",
		3 : "A-",
		4 : "B+",
		5 : "B",
		6 : "B-",
		7 : "C+",
		8 : "C",
		9 : "C-",
		10 : "D+",
		11 : "D",
		12 : "D-",
		13 : "F",
	}

	grade_map = { # Grade map for converting letter grades to proper scale values.
		"A+" : 4.0,
		"A" : 4.0,
		"A-" : 3.7,
		"B+" : 3.3,
		"B" : 3.0,
		"B-" : 2.7,
		"C+" : 2.3,
		"C" : 2.0,
		"C-" : 1.7,
		"D+" : 1.3,
		"D" : 1.0,
		"D-" : 0.7,
		"F" : 0,
	}
	
	while True: # While loop allows program to continue running when exception occurs.
		try:
			n = int(input("Enter number of classes taken: ")) # Determines size of array.
			if n == 0: # Can not have an array with 0 objects.
				raise Exception 
			course_size = list(range(n))
			break
		except:
			print("\nError: Improper Value Entered.") 

	# The following arrays are empty but will have a course_size n number of objects. 

	courses = [] # Contains courses which will be listed by the user.
	credit_hours = [] # Contains the number of credit hours each course is worth listed by user.
	grade_inputs = [] # Is an integer ranging from 1-13, will be converted into letter grades by dictionary. 
	scales = [] # Will be created when the program converts the letter grades by scale by dictionary.
	grade_points = [] # Each value will contain the total amount of grade points each course was worth. 

	for x in course_size:
		while True: # While loop allows program to continue running when exception occurs.
			try:
				course = input("\nEnter Course Name: ")

				if course == "": # Will not allow course name to be blank
					raise Exception
				courses.append(course)

				print("\n1: A+, 2: A, 3: A-, 4: B+, 5: B, 6: B-, 7: C+, 8: C, 9: C-, 10: D+, 11: D, 12: D-, 13: F")
				grade_input = int(input("\nEnter Grade for %s: " % (courses[x])))

				if grade_input > 13: # grade_input cannot be out of range from 1-13.
					raise Exception

				elif grade_input < 1:
					raise Exception

				grade_inputs.append(grade_input)
				credit_hour = int(input("\nEnter the number of credit hours earned for %s: " % (courses[x])))

				if credit_hour == 0: # Course can not be worth 0 credit hours.
					raise Exception
				credit_hours.append(credit_hour)
				break
				
			except:
				print("\nError: Improper Value Entered.")
				print("\nAll previous information has been cleared.")

	for x in grade_inputs:
		scales.append(grade_map[user_input[x]]) # Converts letter grade to scale.

	for grade, hour in zip(scales, credit_hours):
		grade_points.append(grade * hour) # Total grade points per class will be listed in the array grade_points.

	total_points = max(list(accumulate(grade_points))) # Must add all of the values in grade_points, max will provide the final accumulated value.
	total_hours = max(list(accumulate(credit_hours))) # See above.

	for course, credit, grade in zip(courses, credit_hours, grade_inputs):
		print("\nIn %s worth %s credit(s), you received a(n) %s." % (course, credit, user_input[grade]))
		
	print("\nYour cumulative GPA is: %s" % round((total_points/total_hours), 2))
gpa()

input("Press ENTER to exit.")
