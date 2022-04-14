from Py_Quiz.question import Question

question_prompt = [
    "What color is my T-shirt ? (a) Blue (b)Red (c) Yellow \n",
    "What color is your hat ? (a) Blue (b)Red (c) Yellow \n",
    "What color is a banana ? (a) Blue (b)Red (c) Yellow \n",
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c")

]

def run_test(questions):
    score = 0
    for question in questions:
        awnser = input(question.prompt)
        if awnser == question.awnser:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)
