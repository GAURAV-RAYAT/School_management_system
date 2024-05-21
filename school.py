# Importing Modules Required

from datetime import datetime
import time
import os

try:
    import MySQLdb as connector     #pip install MySQLdb
except:
    print("MySQLdb Not Installed")
    print("Installing MySQLdb")
    os.system("pip3 install MySQLdb")
    import MySQLdb as connector

try:
    from pandas import *            #pip install pandas
except:
    print("pandas not installed\nInstalling Pandas")
    os.system("pip3 install pandas")
    from pandas import *

try:
    import matplotlib.pyplot as plt
except:
    print("Matplotlib not installed")
    os.system("pip3 install matplotlib")
    import matplotlib.pylot as plt

try:
    from rich.console import Console
    from rich.markdown import Markdown
except:
    print("Rich not installed\nInstalling Rich")
    os.system("pip3 install rich")
    from rich.console import Console
    from rich.markdown import Markdown

try:
    from password_strength import PasswordPolicy,PasswordStats    #pip install password_strength
except:
    print("password_strength not installed\nInstalling...")
    os.system("pip3 install password_strength")
    from password_strength import PasswordPolicy,PasswordStats


# Password Policy
policy = PasswordPolicy.from_names(
    strength = 0.35
)

#Rich Styles
style = "cyan"
style1 = "magenta"
console = Console()

inp1 = input("Enter The Name of the host :")
inp2 = input("Enter The Name of the user :")
inp3 = input("Enter The Name of the Database :")
inp4 = input("Enter The Password :")

# Connection in my system
# conn = connector.connect(host='localhost',user='root',passwd='skype123',db='SCHOOL')

# Connecting Databse
conn = connector.connect(host=inp1,user=inp2,passwd=inp4,db=inp3)
cur = conn.cursor()

if conn:
    console.print("\nDatabase successfully connected\n",style="green")
else:
    console.print("Not Connected \nTerminating...\n",style="red")

console.print(Markdown("""# School Management System"""),style='cyan')
console.print("\n1. New user\n2. Registration \n3. Retrieve information\n4. Remove a Student or Staff\n5. Visualisation\n6. Exit",style=style)

try:
    inp1 = int(input("Enter Your Choice :"))
except:
    console.print("INPUT SHOULD BE IN INTERGER!!",style=style1)
    inp1 = int(input("Enter Your Choice :"))

if inp1 == 1:
    while True:
        b = False
        inp0 = int(input("SECRET CODE OF THE SCHOOL :"))
        if inp0 == 25235:
            pass
        else:
            console.print("SCHOOL CODE IS WRONG!!",style="red")
            break
        username = input("Enter a Username :")
        # Checking of the availaiblity of the username
        pd_username = []
        sql = "select * from user"
        cur.execute(sql)
        for row in cur.fetchall():
            pd_username.append(row[0])
        for i in pd_username:
            if username == i:
                print(f"{username} already exist as a username.\nTry with a different username.")
                b = True
        if b:
            break
        
        name = input("Enter The name :")
        age = int(input("Enter The age of the person :"))
        password = input("Enter a Strong Password :")
        stats = PasswordStats(password)
        if policy.test(password) == []:
            confirm_password = input("Confirm Your Password :")
            if password == confirm_password:
                query = f"insert into user values('{username}','{password}','{name}','{age}');"
                cur.execute(query)
                conn.commit()
                console.print("User Created...",style="green")
        else:
            console.print(f"Please Enter a Strong Password...\nYour Password Strength is {stats.strength()}",style=style1)
            console.print("It should be more that 0.35",style=style1)
        break

elif inp1 == 2:
    username = input("Enter Your Username :")
    pd_username = []
    sql = "select * from user"
    cur.execute(sql)
    for row in cur.fetchall():
        pd_username.append(row[0])
    if username not in pd_username:
        print("Username Not Registered Kindly Register it.")
        exit()
    password = input("Enter Your Password :")
    query = "select * from user where username='{}' and password='{}'".format(username,password)
    cur.execute(query)
    data = cur.fetchall()
    if any(data):
        print(f"Welcome {username}!!")
        while True:
            print("What Do you like to do?")
            print("1. Register a Student")
            print("2. Register a Staff")
            print("3. Exit")
            try:
                inp2 = int(input("Enter Your Choice :"))
            except:
                print("INPUT SHOULD BE IN INTERGER!!")
                inp2 = int(input("Enter Your Choice :"))

            if inp2 == 1:
                name = input("Name of the Student :")
                age = int(input("Age of the Student :"))
                #admn should not be same of two students since its a primary key in our Table.
                admn = int(input("Enter The admission number :"))
                mother_name = input("Student's Mother Name :")
                father_name = input("Student's Father Name :")
                gender = input("Enter Student's Gender (m or f) :")
                year_of_admission = datetime.now().year
                query = f"insert into student values('{name}','{age}','{admn}','{mother_name}','{father_name}','{gender}','{year_of_admission}');"
                cur.execute(query)
                conn.commit()
                print("Details Inserted!!")
            elif inp2 == 2:
                name = input("Name of the Staff :")
                #id_no should not be same of two Staffs since its a primary key in our Table.
                id_no = int(input("Enter The ID :"))
                age = int(input("Age of the Staff :"))
                role = input("Enter The Role (eg. Teacher) :")
                year_of_joining = datetime.now().year
                query = f"insert into staff values('{name}','{id_no}','{age}','{role}','{year_of_joining}')"
                cur.execute(query)
                conn.commit()
                print("Details Inserted!!")
            elif inp2 == 3:
                print("Terminating")
                exit()
            else:
                print("Wrong Choice")
            print("Do you want to continue?")
            inp10 = input("y or n :")
            if inp10 == ('y' or 'Y'):
                continue
            else:
                break
    else:
        print("Your password or Username is incorrect\nTry Again.")

elif inp1 == 3:
    style2 = "cyan"
    username = input("Enter Your Username :")
    pd_username = []
    sql = "select * from user"
    cur.execute(sql)
    for row in cur.fetchall():
        pd_username.append(row[0])
    if username not in pd_username:
        print("Username Not Registered Kindly Register it.")
        exit()
    password = input("Enter Your Password :")
    query = "select * from user where username='{}' and password='{}'".format(username,password)
    cur.execute(query)
    data = cur.fetchall()
    if any(data):
        while True:
            console.print("1. Details of all Student",style=style2)
            console.print("2. Details of all Staff",style=style2)
            console.print("3. Details of particular Student",style=style2)
            console.print("4. Details of particular Staff",style=style2)
            console.print("5. Total Number Of Students.",style=style2)
            console.print("6. Total Number of Staff",style=style2)
            inp3 = int(input("Enter Your Choice :"))
            if inp3 == 1:
                name = []
                age = []
                admn = []
                mother = []
                father = []
                gender = []
                year = []
                main_dict = {}
                sql = "select * from student;"
                cur.execute(sql)
                for row in cur.fetchall():
                    name.append(row[0])
                    age.append(row[1])
                    admn.append(row[2])
                    mother.append(row[3])
                    father.append(row[4])
                    gender.append(row[5])
                    year.append(row[6])
                main_dict['Name'] = name
                main_dict['Age'] = age
                main_dict['ADMN'] = admn
                main_dict['Mother Name'] = mother
                main_dict['father Name'] = father
                main_dict['Gender'] = gender
                main_dict['Year of Admission'] = year
                df = DataFrame(main_dict)
                df.index = range(1,len(name) + 1)
                print("Do you want to create a csv file? (y or n)?")
                inp6 = input("Enter Your Choice :")
                if inp6 == ('y' or 'Y'):
                    inp100 = input("Enter The Name of the csv file including .csv :")
                    df.to_csv(f'{inp100}',index=False)
                    print(df)
                    print(f"CSV file Created!!\nName = {inp100}")
                else:
                    print()
                    console.print(df,style=style)
                    print()
                                
            elif inp3 == 2:
                name = []
                id_no = []
                age = []
                role = []
                year = []
                main_dict = {}
                sql = "select * from staff;"
                cur.execute(sql)
                for row in cur.fetchall():
                    name.append(row[0])
                    id_no.append(row[1])
                    age.append(row[2])
                    role.append(row[4])
                    year.append(row[5])
                main_dict['Name'] = name
                main_dict['ID Number'] = id_no
                main_dict['Age'] = age
                main_dict['Role'] = role
                main_dict['Year_of_Joining'] = year
                df = DataFrame(main_dict)
                df.index = range(1,len(name) + 1)
                print("Do you want to create a csv file? (y or n)?")
                inp6 = input("Enter Your Choice :")
                if inp6 == ('y' or 'Y'):
                    inp100 = input("Enter The Name of the csv file including .csv :")
                    df.to_csv(f'{inp100}',index=False)
                    print(df)
                    print(f"CSV file Created!!\nName = {inp100}")
                else:
                    print(df)
            elif inp3 == 3:
                inp4 = int(input("Enter The Admission number of the student :"))
                query = f"select * from student where admn = {inp4};"
                cur.execute(query)
                list1 = ['Name','Age','Admn.','Mother','Father','GEN','YOA']
                print()
                for row in cur.fetchall():
                    for i in list1:
                        print(i,row[list1.index(i)],sep=" - ")
                print()
            elif inp3 == 4:
                inp4 = int(input("Enter The ID Number of the Staff :"))
                query = f"select * from staff where ID_no = {inp4};"
                cur.execute(query)
                list1 = ['Name','ID Number','Age','Role','YOJ']
                print()
                for row in cur.fetchall():
                    for i in list1:
                        print(i,row[list1.index(i)],sep=" - ")
                print()
            elif inp3 == 5:
                query = "select * from student;"
                cur.execute(query)
                list1 = []
                for row in cur.fetchall():
                    list1.append(row[0])
                print("Total Number Of Student in our School =",len(list1))
            elif inp3 == 6:
                query = "select * from staff;"
                cur.execute(query)
                list1 = []
                for row in cur.fetchall():
                    list1.append(row[0])
                print("Total Number Of Staff in our School =",len(list1))
            else:
                print("Wrong Choice \nTerminating")
                exit()
            print("Do you want to continue? (y or n)")
            inp5 = input("Enter Your Choice :")
            if inp5 == ('y' or 'Y'):
                continue
            else:
                break
    else:
        print("Your password or Username is incorrect\nTry Again.")

elif inp1 == 4:
    username = input("Enter Your Username :")
    pd_username = []
    sql = "select * from user"
    cur.execute(sql)
    for row in cur.fetchall():
        pd_username.append(row[0])
    if username not in pd_username:
        print("Username Not Registered Kindly Register it.")
        exit()
    password = input("Enter Your Password :")
    query = "select * from user where username='{}' and password='{}'".format(username,password)
    cur.execute(query)
    data = cur.fetchall()
    if any(data):
        console.print("1. Remove a Student\n2. Remove a Staff\n3. EXIT",style=style)
        inp2 = int(input("Enter You Choice :"))

        if inp2 == 1:
            inp3 = int(input("Enter The Admission Number :"))
            query = f"delete from student where admn = {inp3};"
            cur.execute(query)
            console.print("Record Deleted",style=style)
        elif inp2 == 2:
            inp3 = int(input("Enter The ID Number of the staff :"))
            query = f"delete from staff where ID_no = {inp3};"
            cur.execute(query)
            console.print("Record Deleted",style=style)
        else:
            console.print("TERMINATING",style='red')
            time.sleep(1)
            exit()

elif inp1 == 5:
    name = []
    age = []
    admn = []
    mother = []
    father = []
    main_dict = {}
    sql = "select * from student;"
    cur.execute(sql)
    for row in cur.fetchall():
        name.append(row[0])
        age.append(row[1])
        admn.append(row[2])
        mother.append(row[3])
        father.append(row[4])
    main_dict['Name'] = name
    main_dict['Age'] = age
    main_dict['ADMN'] = admn
    main_dict['Mother Name'] = mother
    main_dict['father Name'] = father
    df = DataFrame(main_dict)

    print("1. LINE GRAPH\n2. BAR GRAPH")
    inp2 = int(input("Enter Your Choice :"))

    if inp2 == 1:
        df.plot(kind="line")
    elif inp2 == 2:
        df.plot(kind="bar")
    plt.show()
    
elif inp1 == 6:
    print("Terminating")
    time.sleep(1)
    exit()

else:
    print("wrong choice...\nTerminating")
    time.sleep(1)
    exit()