students_db = {}
student_id = 1
print(students_db)
def start():
      while True:
              print("""1. add students
              2.delete students
              3. update students record
              4. get a student
              5. display all the students
              6. search student by name
              7. count students
              8. filter age
              >>>""")
              user_choice = int(input(""))
              if user_choice == 1:
                      add_student()
              elif user_choice == 2:
                      delete_student()
              elif user_choice == 3:
                      update_student()
              elif user_choice == 4:
                      get_student()
              elif user_choice == 5:
                      display_student()
              elif user_choice == 6:
                     search_student_by_name()
              elif user_choice == 7:
                     count_students()
              elif user_choice == 8:
                     filter_by_age()
              else:
                      print("invalid option")
def add_student():
    name = input("student name: ")
    age = int(input("student age: "))
    department = input("department: ")
    students_db[1] = {"name": name, "age": age, "department": department}
    key =  len(students_db) + 1
    students_db[key] = {"name": name, "age": age, "department": department}

def delete_student():
    student_id = int(input("student id to delete"))
    if student_id in students_db:
            del students_db[student_id]
            print("deleted successfully")
    else:
            print("id not found")

def update_student():
    student_id = int(input("enter id to update: "))
    if student_id in students_db:
        print("""
want to update??
1. name
2. age
3. department
""")
        choice = input("enter choice: ")
        if choice == "1":
          name = input("new name:")
          students_db[student_id]["name"] = name
        elif choice == "2":
          age = input("new age: ")
          students_db[student_id]["age"] = age
        elif choice == "3":
          department = input("new dept: ")
          students_db[student_id]["department"] = department
        else:
          print("invalid choice")
          return
        print("successfully updated")
    else:
          print("student not found")
    
def get_student():
    student = int(input("enter stdent id: "))
    for student_id in students_db:
        name = students_db[student]['name']
        if student == name:
            print(f"id: {student_id}, name: {students_db[student_id]['name']}, age: {students_db[student_id]['age']}, department: {students_db[student_id]['department']}")
        
def display_student():
    if not students_db:
        print("no students yet")
    else:
        for student_id, info in students_db.items():
            print(f"id: {student_id}")
            print(f"name: {students_db[student_id]['name']}")
            print(f"age: {students_db[student_id]['age']}")
            print(f"department: {students_db[student_id]['department']}")
            print("------------------")
def search_student_by_name():
    student_name = input("search name: ").strip().lower()
    for student_id in students_db:
        name = students_db[student_id]['name']
        if name == name:
            print("student found")
            print(f"id: {student_id}")
            print(f"name: {students_db[student_id]['name']}")
            print(f"age: {students_db[student_id]['age']}")
            print(f"department: {students_db[student_id]['department']}")
def count_students():
    total = len(students_db)
    print(f"total number of students: {total}")
def filter_by_age():
    age = int(input("enter age to filter: "))
    found = False 
    for student_id, info in students_db.items():
        if info['age'] == age:
            print(f"id: {student_id}, name: {info['name']}, age: {info['age']}, department: {info['department']}")
            found = True
    if not found:
        print("no student with that age found")
start()
 


