# Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
# должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО
# клиента, услуга, сумма сделки, комиссионные (доход конторы).

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    # Создать соединение с SQLite базой данных
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Подключено к SQLite версии {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    # Создать таблицу нотариальных услуг
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notary_services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            service TEXT NOT NULL,
            deal_amount REAL NOT NULL,
            commission REAL NOT NULL
        );
        """)
        print("Таблица 'notary_services' создана или уже существует")
    except Error as e:
        print(e)


def insert_initial_data(conn):
    # Вставить начальные данные (10 записей)
    services = [
        ("Иванов Иван Иванович", "Заверение подписи", 1500.0, 300.0),
        ("Петрова Анна Сергеевна", "Удостоверение договора", 5000.0, 1000.0),
        ("Сидоров Михаил Петрович", "Свидетельствование верности копии", 800.0, 160.0),
        ("Кузнецова Елена Владимировна", "Составление заявления", 2000.0, 400.0),
        ("Васильев Дмитрий Алексеевич", "Заверение перевода", 2500.0, 500.0),
        ("Николаева Ольга Игоревна", "Удостоверение доверенности", 3500.0, 700.0),
        ("Абрамов Павел Сергеевич", "Свидетельствование подписи", 1200.0, 240.0),
        ("Федорова Мария Дмитриевна", "Удостоверение завещания", 6000.0, 1200.0),
        ("Григорьев Андрей Викторович", "Заверение копии паспорта", 900.0, 180.0),
        ("Семенова Ирина Борисовна", "Удостоверение согласия", 2800.0, 560.0)
    ]

    try:
        cursor = conn.cursor()
        cursor.executemany("""
        INSERT INTO notary_services (client_name, service, deal_amount, commission)
        VALUES (?, ?, ?, ?)
        """, services)
        conn.commit()
        print("Добавлено 10 начальных записей")
    except Error as e:
        print(e)


def add_service(conn):
    # Добавить новую нотариальную услугу
    print("\nДобавление новой нотариальной услуги:")
    client_name = input("ФИО клиента: ")
    service = input("Услуга: ")
    deal_amount = float(input("Сумма сделки: "))
    commission = float(input("Комиссионные (доход конторы): "))

    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO notary_services (client_name, service, deal_amount, commission)
        VALUES (?, ?, ?, ?)
        """, (client_name, service, deal_amount, commission))
        conn.commit()
        print("Запись успешно добавлена!")
    except Error as e:
        print(e)


def search_services(conn):
    # Поиск нотариальных услуг
    print("\nВарианты поиска:")
    print("1. По ФИО клиента")
    print("2. По виду услуги")
    print("3. По сумме сделки (больше указанной)")

    choice = input("Выберите вариант поиска (1-3): ")

    try:
        cursor = conn.cursor()
        if choice == "1":
            name = input("Введите ФИО или часть ФИО клиента: ")
            cursor.execute("""
            SELECT * FROM notary_services 
            WHERE client_name LIKE ?
            """, (f"%{name}%",))
        elif choice == "2":
            service = input("Введите название услуги или часть названия: ")
            cursor.execute("""
            SELECT * FROM notary_services 
            WHERE service LIKE ?
            """, (f"%{service}%",))
        elif choice == "3":
            amount = float(input("Введите минимальную сумму сделки: "))
            cursor.execute("""
            SELECT * FROM notary_services 
            WHERE deal_amount >= ?
            """, (amount,))
        else:
            print("Неверный выбор")
            return

        rows = cursor.fetchall()
        if not rows:
            print("Записи не найдены")
        else:
            print("\nРезультаты поиска:")
            for row in rows:
                print(f"ID: {row[0]}, Клиент: {row[1]}, Услуга: {row[2]}, Сумма: {row[3]}, Комиссия: {row[4]}")
    except Error as e:
        print(e)


def delete_service(conn):
    # Удаление нотариальных услуг
    print("\nВарианты удаления:")
    print("1. По ID записи")
    print("2. По ФИО клиента")
    print("3. Удалить все услуги с комиссией меньше указанной")

    choice = input("Выберите вариант удаления (1-3): ")

    try:
        cursor = conn.cursor()
        if choice == "1":
            service_id = int(input("Введите ID записи для удаления: "))
            cursor.execute("""
            DELETE FROM notary_services 
            WHERE id = ?
            """, (service_id,))
        elif choice == "2":
            name = input("Введите ФИО клиента для удаления: ")
            cursor.execute("""
            DELETE FROM notary_services 
            WHERE client_name = ?
            """, (name,))
        elif choice == "3":
            commission = float(input("Введите максимальную комиссию для удаления: "))
            cursor.execute("""
            DELETE FROM notary_services 
            WHERE commission < ?
            """, (commission,))
        else:
            print("Неверный выбор")
            return

        conn.commit()
        print(f"Удалено записей: {cursor.rowcount}")
    except Error as e:
        print(e)


def update_service(conn):
    # Редактирование нотариальных услуг
    print("\nВарианты редактирования:")
    print("1. Изменить сумму сделки и комиссию по ID")
    print("2. Обновить вид услуги для клиента")
    print("3. Увеличить комиссию на процент для всех услуг с суммой сделки больше указанной")

    choice = input("Выберите вариант редактирования (1-3): ")

    try:
        cursor = conn.cursor()
        if choice == "1":
            service_id = int(input("Введите ID записи для редактирования: "))
            new_amount = float(input("Новая сумма сделки: "))
            new_commission = float(input("Новые комиссионные: "))
            cursor.execute("""
            UPDATE notary_services 
            SET deal_amount = ?, commission = ?
            WHERE id = ?
            """, (new_amount, new_commission, service_id))
        elif choice == "2":
            name = input("Введите ФИО клиента: ")
            new_service = input("Новый вид услуги: ")
            cursor.execute("""
            UPDATE notary_services 
            SET service = ?
            WHERE client_name = ?
            """, (new_service, name))
        elif choice == "3":
            min_amount = float(input("Введите минимальную сумму сделки: "))
            percent = float(input("Введите процент увеличения комиссии: "))
            cursor.execute("""
            UPDATE notary_services 
            SET commission = commission * (1 + ? / 100)
            WHERE deal_amount > ?
            """, (percent, min_amount))
        else:
            print("Неверный выбор")
            return

        conn.commit()
        print(f"Обновлено записей: {cursor.rowcount}")
    except Error as e:
        print(e)


def show_all_services(conn):
    # Показать все нотариальные услуги
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notary_services")
        rows = cursor.fetchall()

        if not rows:
            print("В базе данных нет записей")
        else:
            print("\nВсе нотариальные услуги:")
            for row in rows:
                print(f"ID: {row[0]}, Клиент: {row[1]}, Услуга: {row[2]}, Сумма: {row[3]}, Комиссия: {row[4]}")
    except Error as e:
        print(e)


def main():
    database = "notary_office.db"

    # Создать соединение с базой данных
    conn = create_connection(database)
    if conn is not None:
        # Создать таблицу
        create_table(conn)

        # Проверить, пуста ли таблица, и если да, добавить начальные данные
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM notary_services")
        count = cursor.fetchone()[0]
        if count == 0:
            insert_initial_data(conn)

        while True:
            print("\nМеню нотариальной конторы:")
            print("1. Показать все услуги")
            print("2. Добавить новую услугу")
            print("3. Поиск услуг")
            print("4. Удалить услугу")
            print("5. Редактировать услугу")
            print("0. Выход")

            choice = input("Выберите действие (0-5): ")

            if choice == "1":
                show_all_services(conn)
            elif choice == "2":
                add_service(conn)
            elif choice == "3":
                search_services(conn)
            elif choice == "4":
                delete_service(conn)
            elif choice == "5":
                update_service(conn)
            elif choice == "0":
                print("Выход из программы")
                break
            else:
                print("Неверный выбор, попробуйте снова")

        # Закрыть соединение
        conn.close()
    else:
        print("Ошибка! Не удалось подключиться к базе данных.")


if __name__ == '__main__':
    main()