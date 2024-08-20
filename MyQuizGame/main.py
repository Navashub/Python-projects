import random

questions = [
    {
        "question": "Which is the largest animal in the world?",
        "answers": [
            {"text": "Shark", "correct": False},
            {"text": "Blue whale", "correct": True},
            {"text": "Elephant", "correct": False},
            {"text": "Giraffe", "correct": False}
        ]
    },
    {
        "question": "Which is the smallest country in the world?",
        "answers": [
            {"text": "Vatican City", "correct": True},
            {"text": "Bhutan", "correct": False},
            {"text": "Nepal", "correct": False},
            {"text": "Sri Lanka", "correct": False}
        ]
    },
    {
        "question": "Which is the largest desert in the world?",
        "answers": [
            {"text": "Kalahari", "correct": False},
            {"text": "Gobi", "correct": False},
            {"text": "Sahara", "correct": False},
            {"text": "Antarctica", "correct": True}
        ]
    },
    {
        "question": "Which is the smallest continent in the world?",
        "answers": [
            {"text": "Asia", "correct": False},
            {"text": "Australia", "correct": True},
            {"text": "Arctic", "correct": False},
            {"text": "Africa", "correct": False}
        ]
    }
]

def display_question(question_data):
    print(question_data["question"])
    for idx, answer in enumerate(question_data["answers"], start=1):
        print(f"{idx}. {answer['text']}")

def get_user_answer():
    try:
        choice = int(input("Enter the number of your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_answer()

def run_quiz():
    score = 0
    random.shuffle(questions)  

    for question in questions:
        display_question(question)
        choice = get_user_answer()
        if 1 <= choice <= len(question["answers"]):
            if question["answers"][choice - 1]["correct"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        else:
            print("Invalid choice.")
        
        print()  
    
    print(f"Quiz completed. Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
