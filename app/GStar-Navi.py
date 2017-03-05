# GStar Navigation -- What happened to OnStar, people ask... GStar -- Like no Other
# This elegant algorithm provides you with global heading directions for all snakes
# Gerrit van Rensburg A.K.A. Hadreezy
# BattleSnake 20-17



# How does it work you may?
# Three Simple Steps:
#	(Step 1): Get snake coordinates (coords) and compare them row-wise to find a 				difference (no difference no bends). This currently a 2-bend detector (more layers, more possible bends).
#			  
#	(Step 2): 




#"coords": 
coords = [[3,4], [2,4], [2,3], [2,2], [3,2], [4,2], [5,2], [2,4]]


# Initializing count variable for X column
xC = 0

# Initializing count variable for Y column
# yC = 0

head = coords[1]
print head


# For loop working through a snakes array of values to find the 'kinks'
# Where snakeBody is the body of the snake (coords), excluding the head (hence body). 


# for l1, l2 in snakeBody(coords, coords[1:]):
for l1, l2 in zip(coords, coords[1:]):
	if l1[:] == l2[:]:
		print l1[:], l2[:]
		# print 'l1[0]:',l1[0], 'l1[1]:', l1[1],'l2[0]:', l2[0], 'l2[1]:', l2[1]
		print "There's a dupe!"
	if l1[:] != l2[:]:
		print 'Mismatch:', l1[:], l2[:]



# (Step 0): Get head of snake


head = (coords[0])
print 'head:', head


# (Step 1): Determining Bends in the Snakes chain 
print "Comparing X Values"
for l1, l2 in zip(coords, coords[1:]):   
	s1 = cmp(l1[:1],l2[:1])   # Comparing X values
	if (s1 != 0): 			  # Finding First Bend
		p1 = l2[:]			  # First Bend - p1
		print 'p1:', p1       
		
		# Keeping track of Bends
		xC += 1
# 		print 'xC:', xC 
		     
	if (xC == 1):               # Searching for Second Bend
		p2 = l2[:]			       # Second Bend - p2
		print 'p2', p2	
	
	# Collect the end point (tail) 
	# if (xC = 0) The If statement is for the need to collect the end point for a straight chain
	endP = l1
	print 'endP', l1[:]
		
	# print l1[:1], l2[:1]
	# print s1

print 'p1:', p1, 'p2:', p2, 'endP:', endP


# (Step 2): Determining the vectors from the bends in the snake
print 'head:', head

v1 = [head - p1 for head, p1 in zip(head, p1)]
print 'v1:', v1

head = (coords[0])
print 'head:', head

v2 = [head - p2 for head, p2 in zip(head, p2)]
print 'v2:', v2

head = (coords[0])


	
# Comparing Y values 
# print "Comparing Y Values"
# for l1, l2 in zip(coords, coords[1:]):
# 	m = cmp(l1[1:],l2[1:])
# 	print l1[1:], l2[1:]
# 	print m
	
	
	
# Looking in the X column (1st column '[X, y]') 		
# print "X Column Search Results:"
# for x1, x2 in zip(coords[1:], coords[1:]):
# 	if x1[1:] == x2[1:]:
# 		print x1[:], x2[:]
# 		# print 'l1[0]:',l1[0], 'l1[1]:', l1[1],'l2[0]:', l2[0], 'l2[1]:', l2[1]
# 		print "There's a 'X' match!"
# 	
# 	if x1[:] != x2[:]:
# 		print 'Mismatch:', x1[:], x2[:]
# 		xC = xC + 1
# 		
# 		
# # Increment X column counter to find which X column index has a kink
# 	# xC = xC + 1
# print xC
	
# Looking in the Y column (1st column '[X, y]') 		
# print "Y Column Search Results:"
# for y1, y2 in zip(coords[:1], coords[:1]):
# 	if y1[:] == y2[:]:
# 		print y1[:], y2[:]
# 		# print 'l1[0]:',l1[0], 'l1[1]:', l1[1],'l2[0]:', l2[0], 'l2[1]:', l2[1]
# 		print "There's a 'Y' dupe!"
# 	
# 	if y1[:] != y2[:]:
# 		print 'Mismatch:', y1[:], y2[:]
# 		yC = yC + 1
# 		
# 
# # Increment Y column counter to find which Y column index has a kink
# 	# yC = yC + 1
# print yC
	
	
# If Statement checks if there are 'kinks' in the the snake
# Variable my_list represents a snakes array 
# if len(set(my_list)) < len(my_list):
    
    
    
    
    	
    
    
    