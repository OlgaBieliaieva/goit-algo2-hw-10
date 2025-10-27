# Клас Teacher описує викладача та предмети, які він може викладати
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()  # буде заповнено після призначення

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"


# ------------------------------
# Функція створення розкладу (жадібний алгоритм)
# ------------------------------
def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)  # Предмети, які ще не покриті
    chosen_teachers = []                # Викладачі, яких обрали

    while uncovered_subjects:
        # Знайти викладача, який покриває найбільше ще не покритих предметів
        best_teacher = None
        best_cover = set()

        for teacher in teachers:
            # Які предмети з непокритих може викладати цей викладач
            cover = teacher.can_teach_subjects & uncovered_subjects

            # Якщо цей викладач покриває більше предметів — він кращий кандидат
            if len(cover) > len(best_cover):
                best_teacher = teacher
                best_cover = cover
            # Якщо кількість однакова — обираємо молодшого за віком
            elif len(cover) == len(best_cover) and len(cover) > 0:
                if best_teacher and teacher.age < best_teacher.age:
                    best_teacher = teacher
                    best_cover = cover

        # Якщо жоден викладач не може покрити більше предметів — зупиняємось
        if not best_teacher or not best_cover:
            return None  # неможливо покрити всі предмети

        # Додаємо викладача до розкладу
        best_teacher.assigned_subjects = best_cover
        chosen_teachers.append(best_teacher)

        # Оновлюємо множину непокритих предметів
        uncovered_subjects -= best_cover

        # Видаляємо викладача зі списку, щоб не вибрати його двічі
        teachers.remove(best_teacher)

    return chosen_teachers


# ------------------------------
# Основна частина програми
# ------------------------------
if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:\n")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")