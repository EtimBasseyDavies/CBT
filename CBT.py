import time


print("""
            Enigma Qualification Exam 2019
Attempt all questions. Each question carries equal marks.
Once you have answered a question, it cannot be changed!
Make sure your inputs are between (A and D) for the options.
""")
start = ""
score = 0
Started = False 

accepted_options = ["a", "b", "c", "d"]
unaccepted_options = ["e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]




while Started is False:
    start = input('''
    
                Type "S" to start the exam 

                
>''')

    if start.upper() == "S":
        Started = True
        print("""     
                    
                    Exam Started!
                    
                    
                    """)
        break
    else:
        print("""
                    
                    
                    Unrecognized command
                    
                    """)
        
while True:
    option = 1

    print('''
    1. Who is the current president of the 
    United States of America(U.S.A)?
    (a) Abraham Lincoln
    (b) Donald Trump
    (c) Barrack Obama
    (d) Ole Gunar Solskjaer
    ''')
    answer_1 = ""
    answered = False
    while answered is False:
        answer_1 = input('Type in an option: ').lower()
        if answer_1 == accepted_options[1]:
            score += 1
            answered = True
        elif answer_1 == accepted_options[0]:
            answered = True
        elif answer_1 == accepted_options[2]:
            answered = True
        elif answer_1 == accepted_options[3]:
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        
        


    print('''
    2. When did Nigeria become a Federation?
    (a) 1960
    (b) 1912
    (c) 1999
    (d) 1963
    ''')

    answer_2 = ""
    answered = False
    while answered is False:
        answer_2 = input('Type in an option: ').lower()
        if answer_2 == accepted_options[1]:            
            answered = True
        elif answer_2 == accepted_options[0]:
            answered = True
        elif answer_2 == accepted_options[2]:
            answered = True
        elif answer_2 == accepted_options[3]:
            score += 1
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        


    print('''
    3. Who is the current president of Nigeria?
    (a) Mikel Obi
    (b) Donald Trump
    (c) Barrack Obama
    (d) Muhammadu Buhari
    ''')

    answer_3 = ""
    answered = False
    while answered is False:
        answer_3 = input('Type in an option: ').lower()
        if answer_3 == accepted_options[1]:
            answered = True
        elif answer_3 == accepted_options[0]:
            answered = True
        elif answer_3 == accepted_options[2]:
            answered = True
        elif answer_3 == accepted_options[3]:
            score += 1
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        



    print('''
    4. What is the name of the founder
    of enigma international?
    (a) Etim Bassey
    (b) Harry Maguire
    (c) Larry Babs
    (d) Benjamin Todd
    ''')

    answer_4 = ""
    answered = False
    while answered is False:
        answer_4 = input('Type in an option: ').lower()
        if answer_4 == accepted_options[1]:
            answered = True
        elif answer_4 == accepted_options[0]:
            score += 1
            answered = True
        elif answer_4 == accepted_options[2]:
            answered = True
        elif answer_4 == accepted_options[3]:
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        



    print('''
    5. Nigeria practices a bicameral legislatve system.
    Which of the legislative arm is superior?
    (a) Old Trafford
    (b) Federal Government
    (c) House of Senate
    (d) House of Assembly
    ''')
    
    answer_5 = ""
    answered = False
    while answered is False:
        answer_5 = input('Type in an option: ').lower()
        if answer_5 == accepted_options[1]:
            answered = True
        elif answer_5 == accepted_options[0]:
            answered = True
        elif answer_5 == accepted_options[2]:
            score += 1
            answered = True
        elif answer_5 == accepted_options[3]:
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        


    print('''
    6. Who founded Apple Inc?
    (a) Mark Zuckerberg
    (b) Virgil Van Dijk
    (c) Bill Gates
    (d) Steve Jobs
    ''')

    answer_6 = ""
    answered = False
    while answered is False:
        answer_6 = input('Type in an option: ').lower()
        if answer_6 == accepted_options[1]:
            answered = True
        elif answer_6 == accepted_options[0]:
            answered = True
        elif answer_6 == accepted_options[2]:
            answered = True
        elif answer_6 == accepted_options[3]:
            score += 1
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        



    print('''
    7. There are 9 planets in the universe. How many 
    continents are there in earth?
    (a) 10
    (b) 6
    (c) 7
    (d) 5
    ''')

    answer_7 = ""
    answered = False
    while answered is False:
        answer_7 = input('Type in an option: ').lower()
        if answer_7 == accepted_options[1]:
            answered = True
        elif answer_7 == accepted_options[0]:
            answered = True
        elif answer_7 == accepted_options[2]:
            score += 1
            answered = True
        elif answer_7 == accepted_options[3]:
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        


    
    print('''
    8. From 2009 to 2019, Two players, Leonel Messi and 
    Cristiano Ronaldo, dominated the World football 
    by claiming the most prestigous individual award. 
    Which player broke the cycle
    (a) Neymar Jr
    (b) Luka Modric
    (c) Eden Hazard
    (d) Juan Mata
    ''')

    answer_8 = ""
    answered = False
    while answered is False:
        answer_8 = input('Type in an option: ').lower()
        if answer_8 == accepted_options[1]:
            score += 1
            answered = True
        elif answer_8 == accepted_options[0]:
            answered = True
        elif answer_8 == accepted_options[2]:
            answered = True
        elif answer_8 == accepted_options[3]:
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        


    print('''
    9. Who is the first man to land on the moon?
    (a) Adam Smith
    (b) Marcus Rashford
    (c) Nelson Mandela
    (d) Neil Armstrong
    ''')

    answer_9 = ""
    answered = False
    while answered is False:
        answer_9 = input('Type in an option: ').lower()
        if answer_9 == accepted_options[1]:
            answered = True
        elif answer_9 == accepted_options[0]:
            answered = True
        elif answer_9 == accepted_options[2]:
            answered = True
        elif answer_9 == accepted_options[3]:
            score += 1
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        


        
    print('''
    10. The International Court of Justice is 
    located in Africa. What is the name of the
    African Country?
    (a) Ethopia
    (b) Nigeria
    (c) South Africa
    (d) Egypt
    ''')

    answer_10 = ""
    answered = False
    while answered is False:
        answer_10 = input('Type in an option: ').lower()
        if answer_10 == accepted_options[1]:
            answered = True
        elif answer_10 == accepted_options[0]:
            score += 1
            answered = True
        elif answer_10 == accepted_options[2]:
            answered = True
        elif answer_10 == accepted_options[3]:
            answered = True

            break
        else:
            print("You have entered a wrong option. Please select from option A to D")
        

    
    break
print("""

Exam Completed!!!


""")

result = score * 10


ExamCompleted = True

while ExamCompleted:
    check = input('''
    Do you wish to check your result?
                     Y/N

>''')
    if check.upper() == "Y":
        print(f"""
        
                Your total score is {result}%
                
                
                """)
    elif check.upper() == "N":
        break
    
    else:
        print("Sorry, I don't recognize that command!")

print("Thank you for taking this exam.")

print("""




This window closes in 10 seconds !
""")

time.sleep(10)