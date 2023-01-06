import view
import model
import time

is_end = 0

model = model.DbModel()

while is_end == 0:
    view.hello()

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            mas = model.get_table_names()
            view.show(mas)
            time.sleep(2)
        case "2":
            table = input("Enter a name for the table: ")
            mas = model.get_column_types(table)
            view.show(mas)
            time.sleep(2)
        case "3":
            table = input("Enter a name for the table: ")
            mas = model.get_column_names(table)
            view.show(mas)
            time.sleep(2)
        case "4":
            table = input("Enter the table name: ")
            count = input("Enter count: ")
            model.generate_data(table, count)
            mas = model.get_table_data(table)
            view.show(mas)
            time.sleep(2)
        case "5":
            table = input("Enter the table name: ")
            columns = input("Enter the colum name: ").split(' ')
            val = input("Enter the values: ").split(' ')
            values = {key: value for (key, value) in zip(columns, val)}
            model.insert_data(table, values)
            print("result:\n")
            mas = model.get_table_data(table)
            view.show(mas)
            time.sleep(2)
        case "6":
            table = input("Enter the table name: ")
            columns = input("Enter the colum name: ").split(' ')
            val = input("Enter the values: ").split(' ')
            values = {key: value for (key, value) in zip(columns, val)}
            model.change_data(table, values)
            mas = model.get_table_data(table)
            view.show(mas)
            time.sleep(2)
        case "7":
            table = input("Enter the table name: ")
            column = input("Enter the colum name: ")
            param = input("Параметр: ")
            model.delete_data(table, column, param)
            mas = model.get_table_data(table)
            view.show(mas)
            time.sleep(2)
        case "8":
            table = input("Enter the table name: ")
            mas = model.get_table_data(table)
            view.show(mas)
            time.sleep(2)
        case _:
            is_end = 1
            print("End")
