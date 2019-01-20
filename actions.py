# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Marwah"
my_age = 23
my_bio = "I'm Awesome"
myself = Person(my_name, my_bio, my_age)


def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    print("-----------------")
    print('Would you like to:')
    print("1) Create a new club \n 2) Browse and join clubs \n 3) View existing clubs \n 4) Display members of a club \n -1) Close application" )
    option = ''
    option = input()
    if(option == "Create a new club" or option == "1"):
    	create_club()
    elif(option == "Browse and join clubs" or option == "2"):
    	view_clubs()
    elif(option == "View existing clubs" or option == "3"):
    	view_club_members()
    elif(option == "Display members of a club" or option == "4"):
    	join_clubs()
    elif(option == "Close application" or option == "-1"):
    	print("app is close")			
    	

    

def create_club():
    # your code goes here!
    name = input("Pick a name for your awesome new club: " )
    description = input("What is your club about: ")

    new_club = Club(name, description)
    new_club.assign_president(myself)
    
    print("Enter the number of people you would like to recruit to your new club (-1 to stop")
    user_input = ''
    index = 1
    # example = range(len(population))
    # print("Here is the example:")
    # print(example)
    for person in population:
        print("[%s] %s" % (index, person))
        index += 1
        # print("[%s] %s" % (person, population[person]))
    while(user_input != "-1"):
    	user_input = input()
    	if(user_input !="-1"):
    		for person in population:
    			
    			target_index = str(population.index(person)+1)
    			
    			if (user_input == target_index):
    				new_club.recruit_member(person)
    				
    			# if user_input == str(member_number):
    			# 	new_club.recruit_member(member)
    				print(str(person) + " is added to the Club " + name)

    		

    print("Here's your club:")
    print("Club Name: " + new_club.name)
    print("Club Description: " + new_club.description)
    print("Members: ")
    print(new_club.president)
    new_club.print_member_list()
    # print(" %s ( %s years old, President ) -  %s" % (, str(my_age),my_bio))
    # print(new_club.recruit_member())

    
    

    

def view_clubs():
    # your code goes here!
    # print(clubName)
    # print(clubDescription)   
    for club in clubs:
    	print()
    	print(club)
    user_input = input("Enter the name of the club you would like to join: ")
    for club in clubs:
    	if user_input.lower() == club.name.lower() :
    		print(my_name + " just joined: " + user_input)
    		club.members.append(myself)
    		print(club)


def view_club_members():
    # your code goes here!
    for club in clubs:
    	print()
    	print(club)
    

def join_clubs():
    # your code goes here!
    # for club in clubs:
    # 	print(club)
    view_club_members()
    user_input = input("Enter the name of the club whose members you would like to see: ")
    for club in clubs:
    	if (user_input.lower() == club.name.lower()):
            print("Members of the %s Are:" %(user_input) )
            club.print_member_list()
            print(club.president)
  
    		
    		
            

    	
    

def application():
    introduction()
    # your code goes here!
    options()
