import pymysql

try:
    connect = pymysql.connect(host = 'localhost', user = 'root', password = '', db = "Student")
    print("connected")
    db = connect.cursor()

    try:
        db.execute("DROP TABLE IF EXISTS Student")
        db.execute("CREATE TABLE Student(Name VARCHAR(30), Usn VARCHAR(10) primary key)")
        print("Table created")

        while True:
            choice = input("Enter your choice\n1. Insert\n2. Delete\n3. Update name\n4. Update usn\n5.Exit\n")
            if choice == "1":
                try:
                    sql = f"""INSERT INTO Student VALUES ('{input('Enter Name: ')}', '{input('Enter usn: ')}')"""
                    print(sql)
                    db.execute(sql)
                    connect.commit()
                    print("Inserted")
                except:
                    print("Cannot Insert")
            elif choice == "5":
                break
            elif choice == "2":
                sql = f"""DELETE FROM Student WHERE Usn = '{input('Enter usn: ')}'"""
                try:
                    print(sql)
                    db.execute(sql)
                    connect.commit()
                    print("Deleted")
                except:
                    print("Cannot Delete")
            else:
                print("Invalid choice")
    except:
        print("Table could not be created")

except:
    print("Could not connect")
