import random
print("\nWelcome to Kaun Banega Crorepati !!\n")
print("\nLets play Kaun Banega Crorepati !!\n\n")

question = ["Who was the first Prime Minister of India?","Which planet is known as the Red Planet?","Who wrote the national anthem of India?","What is the capital of France?","Who is known as the \"Missile Man of India\"?","Which element has the chemical symbol 'O'?","What is the largest organ in the human body?","In which year did India gain independence?","Who is the author of \"Harry Potter\" series?","Which is the longest river in the world?","Who is known as the \"Father of the Nation\" in India?","What is the hardest natural substance on Earth?","In which city is the Statue of Liberty located?","Who is the current President of the United States? (As of June 2024)","Which sport is associated with the term 'LBW'?","What is the main ingredient in the Japanese dish 'Sushi'?","Who was the first man to walk on the moon?","Which Indian state is known as the \"Land of Rising Sun\"?"," What does 'CPU' stand for in computers?","Who won the Nobel Prize for Peace in 2014 from India?"]

option = [["Jawaharlal Nehru"," Mahatma Gandhi"," Indira Gandhi","Sardar Vallabhbhai Patel"],["Mars","Venus","Jupiter"," Saturn"],["Rabindranath Tagore","Bankim Chandra Chatterjee","Sarojini Naidu","Subhas Chandra Bose"],["Paris","Berlin","Madrid","Rome"],["Vikram Sarabhai","Homi J. Bhabha","Satish Dhawan","Dr. A.P.J. Abdul Kalam"],["Gold","Oxygen","Silver","Iron"],["Liver","Skin","Heart","Brain"],["1937","1947","1957","1965"],["J.R.R. Tolkien","George R.R. Martin","J.K. Rowling","Suzanne Collins"],["Mississippi","Yangtze"," Amazon","Nile"],["Jawaharlal Nehru","Mahatma Gandhi","B.R. Ambedkar","Sardar Vallabhbhai Patel"],[" Gold","Iron"," Diamond","Silver"],["New York City","Los Angeles","Chicago","San Francisco"],["Donald Trump"," Joe Biden","Barack Obama","Kamala Harris"],["Cricket","Tennis","Football","Basketball"],["Rice","Noodles","Bread"," Pasta"],["Yuri Gagarin","Neil Armstrong","Buzz Aldrin","Michael Collins"],["Arunachal Pradesh","Assam","West Bengal","Odisha"],["Computer Power Unit","Central Power Unit","Computer Processing Unit","Central Processing Unit"],["Malala Yousafzai","Amartya Sen","Mother Teresa"," Kailash Satyarthi"]]


answer = ["Jawaharlal Nehru","Mars","Rabindranath Tagore","Paris","Dr. A.P.J. Abdul Kalam","Oxygen","Skin","1947","J.K. Rowling","Nile","Mahatma Gandhi","Diamond","Diamond","Joe Biden","Cricket","Rice","Neil Armstrong","Arunachal Pradesh","Central Processing Unit","Kailash Satyarthi"] 

count = 0
amount = 0
flag = 0 
quit =""
while count<20 and quit!= "quit":
    number = int(random.randint(0,19)) 
    print(question[number],"\n")
    question.remove(question[number])
    print("Options are :- \n")
    for i in option[number]:
        print(i)
    print("\nType your answer\n")
    userAnswer = input()
    if(userAnswer == answer[number]):
        count+=1
        print("Correct Answer!!\n")
    else:
        print("Sorry you lose!!\n")
        flag = 1
        break
    match count:
        case 0: pass
        case 1:
            print("Prize Amount Won ₹1,000/-")
            amount = 1000
        case 2:
            print("Prize Amount Won₹2,000/-")
            amount = 2000
        case 3:
            print("Prize Amount Won ₹3,000/-")
            amount = 3000
        case 4:
            print("Prize Amount Won ₹5,000/-")
            amount = 5000
        case 5:
            print("Prize Amount Won ₹10,000/-")
            amount = 10000
        case 6:
            print("Prize Amount Won ₹20,000/-")
            amount = 20000
        case 7:
            print("Prize Amount Won ₹40,000/-")
            amount = 40000
        case 8:
            print("Prize Amount Won ₹80,000/-")
            amount = 80000
        case 9:
            print("Prize Amount Won ₹1,60,000/-")
            amount = 160000
        case 10:
            print("Prize Amount Won ₹3,20,000/-")
            amount = 320000
        case 11:
            print("Prize Amount Won ₹6,40,000/-")
            amount = 640000
        case 12:
            print("Prize Amount Won ₹12,50,000/-")
            amount = 1250000
        case 13:
            print("Prize Amount Won ₹25,00,000/-")
            amount = 2500000
        case 14:
            print("Prize Amount Won ₹50,00,000/-")
            amount = 5000000
        case 15:
            print("Prize Amount Won ₹75,00,000/-")
            amount = 7500000
        case 16:
            print("Prize Amount Won ₹1 Crore/-")
            amount = 10000000
        case 17:
            print("Prize Amount Won ₹3 Crore/-")
            amount = 30000000
        case 18:
            print("Prize Amount Won ₹5 Crore/-")
            amount = 50000000
        case 19:
            print("Prize Amount Won ₹7 Crore/-")
            amount = 70000000
        case _:pass
    print("Do you want to quit. Type quit else type anything\n")
    quit = input()
match count:
        case 0: pass
        case 1:
            amount = 1000
        case 2:
            amount = 2000
        case 3:
            amount = 3000
        case 4:
            amount = 5000
        case 5:
            amount = 10000
        case 6:
            amount = 20000
        case 7:
            amount = 40000
        case 8:
            amount = 80000
        case 9:
            amount = 160000
        case 10:
            amount = 320000
        case 11:
            amount = 640000
        case 12:
            amount = 1250000
        case 13:
            amount = 2500000
        case 14:
            amount = 5000000
        case 15:
            amount = 7500000
        case 16:
            amount = 10000000
        case 17:
            amount = 30000000
        case 18:
            amount = 50000000
        case 19:
            amount = 70000000
        case _:pass
if flag == 1:
    if amount >= 10000 and amount <320000:
        print("Prize Amount Won ₹10,000/-")
    elif amount >=320000 and  amount < 7500000:
        print("Prize Amount Won ₹75,00,000/-")
    else:
        print("OPPs you lose")
        
        
        
        
        

    