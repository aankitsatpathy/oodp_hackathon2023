









#main code for phone_specs
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

def display_data():
    mycursor.execute("SELECT * FROM specifications")
    rows = mycursor.fetchall()
    if rows:
        x = PrettyTable()
        x.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
        for row in rows:
            x.add_row(row)
        print(x)
    else:
        print("No data available.")


import prettytable
def display():
    mycursor.execute("SELECT `Model_Name` FROM `specifications`")
    rows = mycursor.fetchall()
    if rows:
        table = prettytable.PrettyTable(['Model Name'])
        for row in rows:
            table.add_row([row[0]])
        print(table)
    else:
        print("No data available.")



class PhoneSpecifications:
  
        
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="classic",
      database="phone_specifications"
    )
    self.mycursor = self.mydb.cursor()

  def search(self):
    column = input("Enter the column to search\n1.OS\n2.Memory\n3.Battery\n4.Price\n5.Camera\n6.Review\n")
    
    if(column == "1"):
        a=input("Enter number of phone to compare : ")
        if a== "1":
            value = input("Enter the model name: ")

            sql = f"SELECT os FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)
            results = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "OS"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "OS"]
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "OS"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
 
            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "OS"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()

            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
        
            value5 = input("Enter the fifth model name: ")
            sql5 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)
            results5 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "OS"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            for row in results5:
                table.add_row([value5, row[0]])
            print(table)
    if(column == "2"):
        a=input("Enter number of phone to compare : ")
        if a== "1":
            value = input("Enter the model name: ")

            sql = f"SELECT memory FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)
            results = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Memory"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Memory"]
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Memory"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
 
            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Memory"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()

            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
        
            value5 = input("Enter the fifth model name: ")
            sql5 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)
            results5 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Memory"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            for row in results5:
                table.add_row([value5, row[0]])
            print(table)

    
    if(column == "3"):
        a=input("Enter number of phone to compare : ")
        if a== "1":
            value = input("Enter the model name: ")

            sql = f"SELECT battery FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)
            results = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Battery"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Battery"]
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Battery"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
 
            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Battery"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()

            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
        
            value5 = input("Enter the fifth model name: ")
            sql5 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)
            results5 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Battery"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            for row in results5:
                table.add_row([value5, row[0]])
            print(table)

    
    if(column == "4"):
        a=input("Enter number of phone to compare : ")
        if a== "1":
            value = input("Enter the model name: ")

            sql = f"SELECT Price FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)
            results = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Price"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Price"]
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Price"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
 
            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Price"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()

            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
        
            value5 = input("Enter the fifth model name: ")
            sql5 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)
            results5 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Price"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            for row in results5:
                table.add_row([value5, row[0]])
            print(table)
   
 


    if(column == "5"):
        a=input("Enter number of phone to compare : ")
        if a== "1":
            value = input("Enter the model name: ")

            sql = f"SELECT Camera FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)
            results = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Camera"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Camera"]
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Camera"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
 
            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Camera"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()

            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
        
            value5 = input("Enter the fifth model name: ")
            sql5 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)
            results5 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Camera"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            for row in results5:
                table.add_row([value5, row[0]])
            print(table)


    
    if(column == "6"):
        a=input("Enter number of phone to compare : ")
        if a== "1":
            value = input("Enter the model name: ")

            sql = f"SELECT Review FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)
            results = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Review"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Review"]
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Review"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()
 
            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Review"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)
            results1 = self.mycursor.fetchall()
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)
            results2 = self.mycursor.fetchall()

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)
            results3 = self.mycursor.fetchall()

            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)
            results4 = self.mycursor.fetchall()
        
            value5 = input("Enter the fifth model name: ")
            sql5 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)
            results5 = self.mycursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Review"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            for row in results5:
                table.add_row([value5, row[0]])
            print(table)
  def review(self):
    value = input("Enter the model name: ")
    sql = "SELECT review FROM specifications WHERE Model_Name=%s"
    val = (value,)
    self.mycursor.execute(sql, val)
    current_review = self.mycursor.fetchone()[0] # fetch the current review
    new_review = input("Enter your review: ")
    new_review_avg = (float(current_review) + float(new_review)) / 2 # calculate new average
    sql2 = "UPDATE specifications SET Review=%s WHERE Model_Name=%s"
    val2 = (new_review_avg, value)
    self.mycursor.execute(sql2, val2)
    self.mydb.commit()
    print(self.mycursor.rowcount, "record(s) updated.")


 
    """   mycursor.execute("SELECT * FROM specifications")
    rows = mycursor.fetchall()
    if rows:
        x = PrettyTable()
        x.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
        for row in rows:
            x.add_row(row)
        print(x)
    else:
        print("No data available.")"""


  def compare(self):
    a=input("Enter number of phone to compare : ")
    if a== "1":
        value = input("Enter the model name: ")
        sql = f"SELECT * FROM specifications WHERE Model_name=%s"
        val = (value,)
        self.mycursor.execute(sql, val)
        results = self.mycursor.fetchall()
        if results:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")
    elif a == "2":
        value1 = input("Enter the first model name: ")
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)
        results1 = self.mycursor.fetchall()
    
        value2 = input("Enter the second model name: ")
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)
        results2 = self.mycursor.fetchall()
    
        if results1 and results2:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results1:
                table.add_row(result)
            for result in results2:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")
            
    elif a == "3":
        value1 = input("Enter the first model name: ")
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)
        results1 = self.mycursor.fetchall()
    
        value2 = input("Enter the second model name: ")
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)
        results2 = self.mycursor.fetchall()

        value3 = input("Enter the third model name: ")
        sql3 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val3 = (value3,)
        self.mycursor.execute(sql3, val3)
        results3 = self.mycursor.fetchall()
    
        if results1 and results2 and results3:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results1:
                table.add_row(result)
            for result in results2:
                table.add_row(result)
            for result in results3:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")
        

    elif a == "4":
        value1 = input("Enter the first model name: ")
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)
        results1 = self.mycursor.fetchall()
    
        value2 = input("Enter the second model name: ")
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)
        results2 = self.mycursor.fetchall()

        value3 = input("Enter the third model name: ")
        sql3 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val3 = (value3,)
        self.mycursor.execute(sql3, val3)
        results3 = self.mycursor.fetchall()

        value4 = input("Enter the fourth model name: ")
        sql4 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val4 = (value4,)
        self.mycursor.execute(sql4, val4)
        results4 = self.mycursor.fetchall()
        
        if results1 and results2 and results3 and results4:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results1:
                table.add_row(result)
            for result in results2:
                table.add_row(result)
            for result in results3:
                table.add_row(result)
            for result in results4:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")

    elif a == "5":
        value1 = input("Enter the first model name: ")
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)
        results1 = self.mycursor.fetchall()
    
        value2 = input("Enter the second model name: ")
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)
        results2 = self.mycursor.fetchall()

        value3 = input("Enter the third model name: ")
        sql3 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val3 = (value3,)
        self.mycursor.execute(sql3, val3)
        results3 = self.mycursor.fetchall()

        value4 = input("Enter the fourth model name: ")
        sql4 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val4 = (value4,)
        self.mycursor.execute(sql4, val4)
        results4 = self.mycursor.fetchall()
        
        value5 = input("Enter the fifth model name: ")
        sql5 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val5 = (value5,)
        self.mycursor.execute(sql5, val5)
        results5 = self.mycursor.fetchall()
        
        if results1 and results2 and results3 and results4 and results5:
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            for result in results1:
                table.add_row(result)
            for result in results2:
                table.add_row(result)
            for result in results3:
                table.add_row(result)
            for result in results4:
                table.add_row(result)
            for result in results5:
                table.add_row(result)
            print(table)
        else:
            print("No results found.")
            

phone_specs = PhoneSpecifications()
display()
while True:
  print("1. COMPARE PHONES")
  print("2. SEARCH PHONE SPECIFICATIONS")
  print("3. REVIEW A PHONE")
  print("4. DISPLAY")
  print("5. EXIT")

  choice = input("Enter your choice (1-5): ")
  if choice == "1":
    phone_specs.compare()

  elif choice == "2":
    phone_specs.search()

  elif choice == "3":
    phone_specs.review()

  elif choice == "4":
    display_data()
    
  elif choice == "5":
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 3.")



print("Program terminated. Run again.")

