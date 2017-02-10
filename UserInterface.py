n = raw_input('What do you want to do? Select a for add or b for view:')
if n == "a":
	k = raw_input('Do You want to add a new skill or add a studied skill?Select a to add new or b to add studied skill:')
	if k == "a":
		new_skill = raw_input('Add your new skill')
			
	elif k == "b":
		studied_skill = raw_input("Add a studied skill")
	
	else:
		print "Invalid Selection"
elif n == "b":
	l = raw_input('Select a to view all skills, b to view studied skills, c to view unstudied skills or d to view progress')
	if l == "a":
		print "View All Skills"
		
	elif l == "b":
		print "View Studied Skills"
		
	elif l == "c":
		print "View Unstudied Skills"
		
	elif l == "d":
		print "View Progress"
	
	else:
		print "Invalid Selection"
else:
    print "Invalid Selection"