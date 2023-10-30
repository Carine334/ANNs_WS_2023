class Cat:
    def __init__ (cat1, name): 
        cat1.name= name

    def naming(cat1):
        print ("Please name your cat: ")
        name=input()
        return name

    def greetings (cat1):
         print("Hello my name is " + cat1.naming() + "! nice to meet you" )
        
