###IDEAS FOR OTHER CTF'seek
"""
Add a lockout timer for those who enter the wrong password, giving the other team a chance for a come-behind-win
This would also add the chance of the opposing team to try to find out the other team's id and lock them out purposefully

someone could hack the pi to hide the other team's .py file in a different folder.




"""







#Python file to handle the checking of the "password" that people find in the CTF game.

team = input("What team are you on?\n\n1. Red Team\n2. Blue Team")
attemptHASH = input("Enter the hash: ")


if (attemptHASH == "abcdefghijklmnop"):
	if (team = 1):
		#turn on Red Team Light
		
	elif (team == 2):
		#turn on Blue Team Light
	
	else:
		print ("You entered the wrong team number.")
		
	
#