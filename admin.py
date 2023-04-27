# main codes for admin 
import mysql.connector


from prettytable import PrettyTable

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="classic"
)

mycursor = mydb.cursor()
mycursor.execute("USE phone_specifications")





# Function to display all data
def display_data():
    mycursor.execute("SELECT * FROM specifications")
    rows = mycursor.fetchall()
    if rows:
        #creating table configration
        x = PrettyTable()
        x.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
        for row in rows:
            # add results to the table
            x.add_row(row)
        print(x)
    else:
        print("No data available.")

# Function to add data
def add_data():
    model_name = input("Enter model name: ")#user input taken
    os = input("Enter OS: ")#user input taken
    memory = input("Enter memory: ")#user input taken
    battery = input("Enter battery: ")#user input taken
    price = input("Enter price: ")#user input taken
    camera = input("Enter camera: ")#user input taken
    review = input("Enter review: ")#user input taken
    sql = "INSERT INTO specifications (Model_Name, OS, Memory, Battery, Price, Camera, Review) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (model_name, os, memory, battery, price, camera, review)
    mycursor.execute(sql, val)#execute mysql code
    mydb.commit()#code pushed
    print(mycursor.rowcount, "record inserted.")

# Function to delete data
def delete_data():
    model_name = input("Enter model name: ")#user input taken
    sql = "DELETE FROM specifications WHERE Model_Name = %s"
    val = (model_name,)
    mycursor.execute(sql, val)#execute mysql code
    mydb.commit()#code pushed
    print(mycursor.rowcount, "record(s) deleted.")

def modify_data():
  model_name = input("Enter model name to modify: ")#user input taken
  field_name = input("Enter field name to modify (OS, Memory, Battery, Price, Camera, Review): ")#user input taken
  new_value = input("Enter new value: ")#user input taken
  sql = f"UPDATE specifications SET {field_name} = %s WHERE Model_Name = %s"
  val = (new_value, model_name)
  mycursor.execute(sql, val)#execute mysql code
  mydb.commit()#code pushed
  print("Data modified successfully.")


display_data()
while True:
  print("1. ADD PHONE")
  print("2. DELETE PHONE")
  print("3. MODIFY PHONE SPECIFICATIONS")
  print("4. EXIT")

  choice = input("Enter your choice (1-4): ")#user input taken
  if choice == "1":
      add_data()#add_data function called
      break
  elif choice == "2":
      delete_data()#delete_data function called
      break
  elif choice == "3":
      modify_data()#modify_data function called
      break
  elif choice == "4":
      break#loop exitted
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")

display_data()#delete_data function called
