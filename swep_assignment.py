# Tajudeen Abdulsalam Olalekan
# 2022010284

quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. O2", "B. H2O", "C. CO2", "D. H2"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. Jane Austen", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium"],
        "answer": "C"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Sapphire"],
        "answer": "C"
    },
    {
        "question": "Which element has the chemical symbol 'Fe'?",
        "options": ["A. Fluorine", "B. Iron", "C. Francium", "D. Gold"],
        "answer": "B"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
        "answer": "B"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["A. Tomato", "B. Avocado", "C. Pepper", "D. Onion"],
        "answer": "B"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["A. 1910", "B. 1912", "C. 1914", "D. 1916"],
        "answer": "B"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["A. Yen", "B. Dollar", "C. Euro", "D. Peso"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"],
        "answer": "B"
    },
    {
        "question": "How many bones are there in the adult human body?",
        "options": ["A. 206", "B. 205", "C. 207", "D. 208"],
        "answer": "A"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which is the largest desert in the world?",
        "options": ["A. Sahara", "B. Arabian", "C. Gobi", "D. Antarctic"],
        "answer": "D"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["A. Venice", "B. Florence", "C. Rome", "D. Milan"],
        "answer": "C"
    },
]

points = 0
total_points = len(quiz) * 10

# Attempting the quiz
print("Welcome to the 200 Level SWEP Quiz.\nEach question carries 10 points.\nChoose correctly from options A,B,C,D")

for index, data in enumerate(quiz):
    print(f"({index + 1}). {data['question']}")
    for option in data['options']:
        print(option)

    answer = input("Enter your choice: ").upper()

    # Answer
    if answer == data['answer']:
        print("Correct!\n")
        points += 10
    else:
        print(f"Wrong! The correct answer is {data['answer']}.\n")

print(f"Your final score is {points} / {total_points}")

if points >= 180:
    grade = "A"
elif points >= 140:
    grade = "B"
elif points >= 100:
    grade = "C"
elif points >= 70:
    grade = "D"
elif points >= 50:
    grade = "E"
else:
    grade = "F"

print(f"You have an {grade}")
