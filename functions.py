def greetings(names):
    if(isinstance(names, list) == False):
        print("Please provide a list of names")
        return
    
    for name in names:
        print(f"Hello {name}!")
        

greetings(5)