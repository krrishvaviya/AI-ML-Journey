from quis import question

questions_prompt=[
    "The colour of watermelon \n (a)yellow \n(b)green\n(c)purple\n\n ",
    "The colour ofbanana \n(a)yellow\n(b)green\n(C)blue\n\n",
    "The colour of tomato\n(a)yellow\n(b)red\n\n"
                  ]

questions =[ 
   question(questions_prompt[0],"b"),
    question(questions_prompt[1],"a"),
    question(questions_prompt[2],"b")
]

def run (questions):
    score=0
    for Question in questions:  #after for loop Question = questions list defined above
        answer=input(Question.question)
        if answer == Question.answer:
            score+=1
    print(f"your score is {score}")
run(questions)