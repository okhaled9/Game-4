#creating a grid
g=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def grid():
	print(g[0]," /",g[1]," /",g[2]," /",g[3])
	print(g[4]," /",g[5]," /",g[6]," /",g[7])
	print(g[8]," /",g[9]," /",g[10],"/",g[11])
	print(g[12],"/",g[13],"/",g[14],"/",g[15])
grid()
x=0
while(x<=16):
	#player 1 will play his turn
	print("player 1's turn")
	a=int(input("enter 1st position to fill :"))
	b=int(input("enter 2nd position to fill :"))
	#check if number is on the grid
	while(a<0 or a>15 or b<0 or b>15):
		grid()
		print("number is not on grid")
		a=int(input("enter 1st position to fill :"))
		b=int(input("enter 2nd position to fill :"))
	#check if numbers are in the same square
	while(not(a==g[a] and (b==g[a+1] or b==g[a+4] or b==g[a-1] or b==g[a-4]))):
		grid()
		print("numbers have to be from the same square or number has already been chosen")
		a=int(input("enter 1st position to fill :"))
		b=int(input("enter 2nd position to fill :"))
	#replacing chosen numbers with x 
	g[a]="x"
	g[b]="x"
	print(" ")
	grid()
	print(" ")
	#check if there is any valid movements,if there is not the the player wins
	for i in range(12):
		if(g[i]=="x"):
			pass
		elif(g[i]==i and (g[i+1]==i+1 or g[i+4]==i+4 or g.count("x")<=12)):
			pass
		else:
			print("player 1 wins")
			x=1
			break
	if(x==1):
		break
	#checking for valid movements for the last row.(here checking under each element gives index out of range)
	for i in range(12,15):
		if(g[i]=="x"):
			pass
		elif(g[i]==i and g[i+1]==i+1 or g.count("x")<=12):
			pass
		else:
			print("player 1 wins")
			x=1
			break
	if(x==1):
		break

	#player 2 will play his turn
	print("player 2's turn")
	a=int(input("enter 1st position to fill :"))
	b=int(input("enter 2nd position to fill :"))
	#check if number is on the grid
	while(a<0 or a>15 or b<0 or b>15):
		grid()
		print("number is not on grid")
		a=int(input("enter 1st position to fill :"))
		b=int(input("enter 2nd position to fill :"))
	#check if numbers are in the same square
	while(not(a==g[a] and (b==g[a+1] or b==g[a+4] or b==g[a-1] or b==g[a-4]))):
		grid()
		print("numbers have to be from the same square or number has already been chosen")
		a=int(input("enter 1st position to fill :"))
		b=int(input("enter 2nd position to fill :"))
	g[a]="x"
	g[b]="x"
	print(" ")
	grid()
	print(" ")
	#check if there is any valid movements,if there is not the the player wins
	for i in range(12):
		if(g[i]=="x"):
			pass
		elif(g[i]==i and (g[i+1]==i+1 or g[i+4]==i+4 or g.count("x")<=12)):
			pass
		else:
			print("player 2 wins")
			x=1
			break
	if(x==1):
		break
	#checking for valid movements for the last row.(here checking under each element gives index out of range)	
	for i in range(12,15):
		if(g[i]=="x"):
			pass
		elif((g[i]==i and g[i+1]==i+1) or g.count("x")<=12):
			pass
		else:
			print("player 1 wins")
			x=1
			break
	if(x==1):
		break
	if(g.count("x")==16):
		print("it's a tie")
		break