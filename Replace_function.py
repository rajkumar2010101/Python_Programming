# problem2
letter = '''Dear <|NAME|>
you are selected !

Date <|DATE|>'''
print(letter)
 name = input("Enter your Name\n")
 name = str(name)
 date = input("Enter Date\n")
 letter = latter.replace("<|NAME|>",name)
 letter = latter.replace("<|DATE|>",date)
 print(latter)