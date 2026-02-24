#step 1 : Get's the users name
while True:
    name = input ("Please enter your name \n or type 'quit' to exit: ")
    
    if name.lower()=="quit":
        print ("Good bye have a nice day.")
        break
    #step 2 : Gets the users birth year 
    birth_year = int (input("Please enter your birth year: ")) # convert input in to an integer 
    #step 3 : calculate age
    current_year = 2026
    age = current_year - birth_year
    #step 4 : print the message
    print ("So you are " + name + " you  present  age  is " + str(age))
    if age < 18:
        print("So you are still a kid.")
    elif age == 18:
        print("So you turned in to an adult now.") 
    elif age > 18:
        print("How it feels being an adult.")    
  