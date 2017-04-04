#Jordan Hueber
#3/30/2017
#Dictionary





terms = {"Tuples": "they are like lists, but cannot be changed once entered.",
         "Print": " a command used to display basic messages to the user.",
         "Input": " a command used to make the program interact with the user.",
         "Loop": "a loop occurs when a sequence repeats itself over and over.",
         "Variable": "it's used for key components of a program that will be reused."}

choice = None
while choice !="0":

    print(
    """
    Python Translator

    0 - Quit
    1 - Look up Python term
    2 - Add a Python term
    3 - Redefine a Python term
    4 - Delete a Python term from program

    The current terms in this program are Tuples, Print, Input, Loop, and Variable.
    """
    )

    choice = input("Choice: ")
    print()

#Exit

    if choice == "0":
        print("\nHave a good day.")

#Definition

    elif choice == "1":
        term = input("What term would you like to have defined?: ")
        if term in terms:
            definition = terms[term]
            print("\n",term, "means",definition)
        else:
            print("Sorry, I don't know",term)



    elif choice == "2":
        term = input("What term would you like to have defined?: ")
        if term in terms:
            definition = terms[term]
            print("\n",term, "means",definition)
        else:
            print("Sorry, I don't know",term)



    elif choice == "3":
        term = input("What term would you like to have defined?: ")
        if term in terms:
            definition = terms[term]
            print("\n",term, "means",definition)
        else:
            print("Sorry, I don't know",term)



    elif choice == "4":
        term = input("What term would you like to have defined?: ")
        if term in terms:
            definition = terms[term]
            print("\n",term, "means",definition)
        else:
            print("Sorry, I don't know",term)
            
