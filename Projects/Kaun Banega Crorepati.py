import random

price_money= 0

questions= [{
    "question": "What is the full form of CPU ?",
    "option": ["1. Central Processing Unit", "2. Control Processing Unit", "3. Current Producing Unit"],
    "answer": 1
},{
    "question": "Who is the CEO of Google ?",
    "option": ["1. Mukesh Ambani", "2. Bill Gates", "3. Sundar Pichai"],
    "answer": 3
},{
    "question": "Who is the owner of the Microsoft Company ?",
    "option": ["1. Ratan Tata", "2. Bill Gates", "3. Steve Jobs"],
    "answer": 2
}]
random.shuffle(questions)

for question in questions:
    print(question["question"])
    for option in question["option"]:
        print(option)
    
    user_ans= int(input("Enter your answer: "))
    if user_ans == question["answer"]:
        print("Correct answer!")
        price_money += 1000
        
    else:
        print("Wrong Answer!")
        break

print("\nPrice money: ",price_money)