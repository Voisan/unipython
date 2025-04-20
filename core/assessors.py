from abc import ABC, abstractmethod
from typing import Dict


class ProgressAssessor(ABC):
    """
    Абстрактный класс для оценки прогресса студентов.

    Методы:
        - assess_progress: оценивает прогресс на основе словаря оценок студентов.
        - get_scores: извлекает оценки студентов.
        - apply_assessment: применяет шкалу оценок.
        - students_scores: выводит оценки каждого студента.
    """

    def assess_progress(self, stud_scores: Dict[str, float]) -> str:
        """
        Оценивает прогресс студентов, выводит средний балл и индивидуальные оценки.

        :param stud_scores: словарь {имя_студента: оценка}
        """
        scores = self.get_scores(stud_scores)
        average = sum(scores) / len(scores) if scores else 0
        print(f"Средний балл: {average}")
        self.students_scores(stud_scores)
        for name, score in stud_scores.items():
            print(f"Оценка студента {name}: {self.apply_assessment(score)}")

    @abstractmethod
    def get_scores(self, student_scores: Dict[str, float]):
        """Извлекает список оценок студентов."""
        pass

    @abstractmethod
    def apply_assessment(self, average_score: float) -> str:
        """Возвращает вербальную оценку по числовому значению."""
        pass

    @abstractmethod
    def students_scores(self, students):
        """Выводит оценки всех студентов."""
        pass


class ProgrammingProgressAssessor(ProgressAssessor):
    """
    Оценка прогресса для курсов программирования.
    """

    def students_scores(self, students):
        print("Оценки студентов:")
        for name, score in students.items():
            print(f"{name}: {score}")
        return list(students.values())

    def get_scores(self, students):
        return list(students.values())

    def apply_assessment(self, average_score):
        if average_score >= 86:
            return "Отлично"
        elif average_score >= 72:
            return "Хорошо"
        elif average_score >= 56:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"


class DesignProgressAssessor(ProgressAssessor):
    """
    Оценка прогресса для курсов дизайна.
    """

    def students_scores(self, students):
        print("Оценки студентов по дизайну:")
        for name, score in students.items():
            print(f"{name}: {score}")
        return list(students.values())

    def get_scores(self, students):
        return list(students.values())

    def apply_assessment(self, average_score):
        if average_score >= 90:
            return "Превосходно"
        elif average_score >= 75:
            return "Хорошо"
        elif average_score >= 60:
            return "Приемлемо"
        else:
            return "Нужно доработать"


class ScienceProgressAssessor(ProgressAssessor):
    """
    Оценка прогресса для курсов по науке.
    """

    def students_scores(self, students):
        print("Оценки студентов по науке:")
        for name, score in students.items():
            print(f"{name}: {score}")
        return list(students.values())

    def get_scores(self, students):
        return list(students.values())

    def apply_assessment(self, average_score):
        if average_score >= 85:
            return "Отлично"
        elif average_score >= 70:
            return "Хорошо"
        elif average_score >= 55:
            return "Удовлетворительно"
        else:
            return "Плохо"
