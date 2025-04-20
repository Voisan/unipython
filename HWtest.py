import random
import datetime
import os


class TestSystem:
    def __init__(self, questions_file='questions.txt', results_file='results.txt'):
        self.questions_file = questions_file
        self.results_file = results_file
        self.questions = []
        self.load_questions()
        self.shuffle_questions()
        self.results = {
            'start_time': None,
            'end_time': None,
            'total_questions': 0,
            'correct_answers': 0
        }

    def load_questions(self):
        try:
            with open(self.questions_file, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 7:
                        question = {
                            'text': parts[0],
                            'options': parts[1:6],
                            'correct': parts[6]
                        }
                        self.questions.append(question)
        except FileNotFoundError:
            print(f"Ошибка: Файл с вопросами '{self.questions_file}' не найден.")
            exit()
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            exit()

    def shuffle_questions(self):
        random.shuffle(self.questions)
        for question in self.questions:
            options = question['options']
            random.shuffle(options)


    def run_test(self):
        self.results['start_time'] = datetime.datetime.now()
        self.results['total_questions'] = len(self.questions)

        for i, question in enumerate(self.questions, 1):
            print(f"Вопрос {i}/{len(self.questions)}: {question['text']}")
            for j, option in enumerate(question['options'], 1):
                print(f"{j}. {option}")

            while True:
                try:
                    answer = int(input("\nВаш ответ (1-5): "))
                    if 1 <= answer <= 5:
                        selected = question['options'][answer - 1]
                        if selected == question['correct']:
                            print("\nПравильно!")
                            self.results['correct_answers'] += 1
                        else:
                            print(f"\nНеправильно. Правильный ответ: {question['correct']}")
                        break
                    else:
                        print("Пожалуйста, введите число от 1 до 5.")
                except ValueError:
                    print("Ошибка: введите номер варианта (1-5).")

            print("\n" + "=" * 50 + "\n")

        self.results['end_time'] = datetime.datetime.now()
        self.show_results()
        self.save_results()
    def show_results(self):
        print("Тестирование завершено! \n")
        print(f"Общее количество вопросов: {self.results['total_questions']}")
        print(f"Количество правильных ответов: {self.results['correct_answers']}")
        percentage = (self.results['correct_answers'] / self.results['total_questions']) * 100
        print(f"Процент правильных ответов: {percentage:.2f}%")

    def save_results(self):
        with open(self.results_file, 'a', encoding='utf-8') as file:
            file.write("\n" + "=" * 50 + "\n")
            print("Тестирование завершено!\n")
            file.write(f"Время начала теста: {self.results['start_time']}\n")
            file.write(f"Время окончания теста: {self.results['end_time']}\n")
            file.write(f"Общее количество вопросов: {self.results['total_questions']}\n")
            file.write(f"Количество правильных ответов: {self.results['correct_answers']}\n")
            percentage = (self.results['correct_answers'] / self.results['total_questions']) * 100
            file.write(f"Процент правильных ответов: {percentage:.2f}%\n")
            file.write("=" * 50 + "\n")

        print(f"\nРезультаты сохранены в файл '{self.results_file}'")




if __name__ == "__main__":
    test = TestSystem()
    test.run_test()