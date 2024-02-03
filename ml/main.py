import os

def get_categories():
    file_names = [file for file in os.listdir("questions") if file.endswith("_questions.csv")]

    categories = [file.replace("_questions.csv", "") for file in file_names]

    return categories

def get_questions(category):
    file_name = os.path.join("questions", f"{category}_questions.csv")
    with open(file_name, "r", encoding="utf-8") as file:
        questions = file.readlines()
    return [question.strip() for question in questions]

def create_answer_file(category):
    folder_path = "answers"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_name = os.path.join(folder_path, f"{category}_answers.csv")
    with open(file_name, "w", encoding="utf-8") as file:
        pass  # Opret en tom fil


def save_answers(category, answer):
    file_name = os.path.join("answers", f"{category}_answers.csv")
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(','.join(map(str, answer)) + '\n')

def read_answer(category):
    file_name = os.path.join("answers", f"{category}_answers.csv")
    with open(file_name, "r", encoding="utf-8") as file:
        answer_lines = file.readlines()
    answer = [list(map(int, line.strip().split(','))) for line in answer_lines]
    return answer

def validate_category_choice(choice, num_categories):
    try:
        choice = int(choice)
        if 1 <= choice <= num_categories:
            return True, choice
        else:
            print("Ugyldigt nummer. Prøv igen.")
            return False, None
    except ValueError:
        print("Indtast venligst et heltal.")
        return False, None
    
def validate_answers(answer, num_questions):
    try:
        validated_answer = [int(val) for val in answer]
        if all(1 <= val <= 5 for val in validated_answer) and len(validated_answer) == num_questions:
            return True, validated_answer
        else:
            print("Ugyldige svar. Svar skal være heltal mellem 1 og 5 for hvert spørgsmål.")
            return False, None
    except ValueError:
        print("Alle svar skal være heltal mellem 1 og 5.")
        return False, None

def main():
    print("Velkommen til testen!")

    # Get available categories
    categories = get_categories()

    if not categories:
        print("Ingen tilgængelig kategorier")
        return
    
    # Present the available categories
    print("Vælg en kategori:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}.{category}")

    if not categories:
        print("Ingen tilgængelige kategorier")
        return
    
    # Present the available categories
    print("Vælg en kategori:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}.{category}")

    # User chooses the category with input validation
    while True:
        choice = input("Indtast nummeret på den ønskede kategori: ")
        is_valid, chosen_index = validate_category_choice(choice, len(categories))
        
        if is_valid:
            break

    chosen_category = categories[chosen_index - 1]

    print(f"Du valgte kategorien: {chosen_category}")


     # Tjek om svarfilen eksisterer, og opret den, hvis den ikke gør
    file_path = os.path.join("answers", f"{chosen_category}_answers.csv")
    if not os.path.exists(file_path):
        create_answer_file(chosen_category)

    questions = get_questions(chosen_category)

    # Ask and save answers
    answers = []
    for i, question_text in enumerate(questions, start=1):
        while True:
            answer = input(f"{i}.{question_text} (Svar fra 1-5): ")
            is_valid, validated_answer = validate_answers([answer], 1)
            
            if is_valid:
                answers.append(validated_answer[0])
                break
            else:
                print("Ugyldigt svar. Prøv igen.")

    # save the answers
    save_answers(chosen_category, answers)

if __name__ == "__main__":
    main()
