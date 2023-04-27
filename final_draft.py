









#main code for phone_specs
import mysql.connector
from prettytable import PrettyTable

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="classic"
)
#make cursor
mycursor = mydb.cursor()
mycursor.execute("USE phone_specifications")

# import the prettytable module
import prettytable

# define a function to display all the data from the 'specifications' table
def display_data():
    # execute a SQL query to select all the columns from the 'specifications' table
    mycursor.execute("SELECT * FROM specifications")
    
    # fetch all the rows returned by the SQL query
    rows = mycursor.fetchall()
    
    # check if there are any rows
    if rows:
        # create a prettytable object with columns named "Model Name", "OS", "Memory", "Battery", "Price", "Camera", and "Review"
        x = PrettyTable()
        x.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
        
        # loop through each row and add it to the prettytable object
        for row in rows:
            x.add_row(row)
        
        # print the prettytable object
        print(x)
    else:
        # print a message if there are no rows
        print("No data available.")

# define a function to display only the model names from the 'specifications' table
def display():
    # execute a SQL query to select only the 'Model_Name' column from the 'specifications' table
    mycursor.execute("SELECT `Model_Name` FROM `specifications`")
    
    # fetch all the rows returned by the SQL query
    rows = mycursor.fetchall()
    
    # check if there are any rows
    if rows:
        # create a prettytable object with a single column named 'Model Name'
        table = prettytable.PrettyTable(['Model Name'])
        
        # loop through each row and add the model name to the prettytable object
        for row in rows:
            table.add_row([row[0]])
        
        # print the prettytable object
        print(table)
    else:
        # print a message if there are no rows
        print("No data available.")


#class declaration

class PhoneSpecifications:
  
  #constructor to connect mysql    
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="classic",
      database="phone_specifications"
    )
    self.mycursor = self.mydb.cursor()
    #to compare specific specs
  def search(self):
    column = input("Enter the column to search\n1.OS\n2.Memory\n3.Battery\n4.Price\n5.Camera\n6.Review\n")#user input taken
    #first case being checked
    if(column == "1"):
        #processing user request
        
        a=input("Enter number of phone to compare : ")#user input taken
        if a== "1":
            value = input("Enter the model name: ")#user input taken

            sql = f"SELECT os FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)#execute mysql code
            results = self.mycursor.fetchall()#fetch current data
            #creating table configration
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "OS"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            #creating table configration
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "OS"]
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "OS"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            # add results3 to the table
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
 
            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "OS"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            # add results3 to the table
            for row in results3:
                table.add_row([value3, row[0]])
            # add results4 to the table
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data

            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
        
            value5 = input("Enter the fifth model name: ")#user input taken
            sql5 = f"SELECT os FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)#execute mysql code
            results5 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "OS"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            # add results3 to the table
            for row in results3:
                table.add_row([value3, row[0]])
            # add results4 to the table
            for row in results4:
                table.add_row([value4, row[0]])
            # add results5 to the table
            for row in results5:
                table.add_row([value5, row[0]])
            print(table)
    if(column == "2"):
        a=input("Enter number of phone to compare : ")#user input taken
        if a== "1":
            value = input("Enter the model name: ")#user input taken

            sql = f"SELECT memory FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)#execute mysql code
            results = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Memory"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Memory"]
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Memory"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            # add results3 to the table
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
 
            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Memory"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            # add results3 to the table
            for row in results3:
                table.add_row([value3, row[0]])
            # add results4 to the table
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data

            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
        
            value5 = input("Enter the fifth model name: ")#user input taken
            sql5 = f"SELECT memory FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)#execute mysql code
            results5 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Memory"]
            # add results1 to the table
            for row in results1:
                table.add_row([value1, row[0]])
            # add results2 to the table
            for row in results2:
                table.add_row([value2, row[0]])
            # add results3 to the table
            for row in results3:
                table.add_row([value3, row[0]])
            # add results4 to the table
            for row in results4:
                table.add_row([value4, row[0]])
            # add results5 to the table
            for row in results5:
                table.add_row([value5, row[0]])
            print(table)

    
    if(column == "3"):
        a=input("Enter number of phone to compare : ")#user input taken
        if a== "1":
            value = input("Enter the model name: ")#user input taken

            sql = f"SELECT battery FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)#execute mysql code
            results = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()
            table.field_names = ["Model Name", "Battery"]
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Battery"]
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Battery"]
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
 
            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Battery"]
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data

            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
        
            value5 = input("Enter the fifth model name: ")#user input taken
            sql5 = f"SELECT battery FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)#execute mysql code
            results5 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Battery"]
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
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
        a=input("Enter number of phone to compare : ")#user input taken
        if a== "1":
            value = input("Enter the model name: ")#user input taken

            sql = f"SELECT Price FROM specifications WHERE Model_name=%s"

            val = (value,)
            self.mycursor.execute(sql, val)#execute mysql code
            results = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Price"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Price"]
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data
    
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Price"]
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
 
            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Price"]
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data

            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
        
            value5 = input("Enter the fifth model name: ")#user input taken
            sql5 = f"SELECT Price FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)#execute mysql code
            results5 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Price"]
            for row in results1:
                table.add_row([value1, row[0]])
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
            self.mycursor.execute(sql, val)#execute mysql code
            results = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
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
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Camera"]
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
 
            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Camera"]
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
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
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data

            value4 = input("Enter the fourth model name: ")
            sql4 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
        
            value5 = input("Enter the fifth model name: ")#user input taken
            sql5 = f"SELECT Camera FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)#execute mysql code
            results5 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Camera"]
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
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
            self.mycursor.execute(sql, val)#execute mysql code
            results = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Review"]
            # add results to the table
            for row in results:
                table.add_row([value, row[0]])
            print(table)
            
        elif a == "2":
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Review"]
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            print(table)
           

      
        elif a == "3":
            value1 = input("Enter the first model name: ")
            sql1 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")
            sql2 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")
            sql3 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Review"]
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            print(table)

        

        elif a == "4":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data
 
            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Review"]
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
            for row in results2:
                table.add_row([value2, row[0]])
            for row in results3:
                table.add_row([value3, row[0]])
            for row in results4:
                table.add_row([value4, row[0]])
            print(table)
        

        elif a == "5":
            value1 = input("Enter the first model name: ")#user input taken
            sql1 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val1 = (value1,)
            self.mycursor.execute(sql1, val1)#execute mysql code
            results1 = self.mycursor.fetchall()#fetch current data
    
            value2 = input("Enter the second model name: ")#user input taken
            sql2 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val2 = (value2,)
            self.mycursor.execute(sql2, val2)#execute mysql code
            results2 = self.mycursor.fetchall()#fetch current data

            value3 = input("Enter the third model name: ")#user input taken
            sql3 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val3 = (value3,)
            self.mycursor.execute(sql3, val3)#execute mysql code
            results3 = self.mycursor.fetchall()#fetch current data

            value4 = input("Enter the fourth model name: ")#user input taken
            sql4 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val4 = (value4,)
            self.mycursor.execute(sql4, val4)#execute mysql code
            results4 = self.mycursor.fetchall()#fetch current data
        
            value5 = input("Enter the fifth model name: ")#user input taken
            sql5 = f"SELECT Review FROM specifications WHERE Model_name=%s"
            val5 = (value5,)
            self.mycursor.execute(sql5, val5)#execute mysql code
            results5 = self.mycursor.fetchall()#fetch current data
            table = prettytable.PrettyTable()#creating table configration
            table.field_names = ["Model Name", "Review"]
            # add results to the table
            for row in results1:
                table.add_row([value1, row[0]])
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
    #taking model name
    value = input("Enter the model name: ")
    sql = "SELECT review FROM specifications WHERE Model_Name=%s"
    val = (value,)
    self.mycursor.execute(sql, val)#execute mysql code
    current_review = self.mycursor.fetchone()[0] # fetch the current review
    new_review = input("Enter your review: ")#taking user review
    new_review_avg = (float(current_review) + float(new_review)) / 2 # calculate new average
    sql2 = "UPDATE specifications SET Review=%s WHERE Model_Name=%s"#update review
    val2 = (new_review_avg, value)
    self.mycursor.execute(sql2, val2)
    self.mydb.commit()


  def compare(self):
    a=input("Enter number of phone to compare : ")#user input taken'
    if a== "1":
        value = input("Enter the model name: ")#user input taken
        sql = f"SELECT * FROM specifications WHERE Model_name=%s"
        val = (value,)
        self.mycursor.execute(sql, val)#execute mysql code
        results = self.mycursor.fetchall()#fetch current data
        if results:
            #setting table configration
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            #adding data to table
            for result in results:
                table.add_row(result)
            print(table)#print the table
        else:
            print("No results found.")
    elif a == "2":
        value1 = input("Enter the first model name: ")#user input taken 
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)#execute mysql code
        results1 = self.mycursor.fetchall()#fetch current data
    
        value2 = input("Enter the second model name: ")#user input taken 
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)#execute mysql code
        results2 = self.mycursor.fetchall()#fetch current data
    
        if results1 and results2:
            #setting table configration
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            #adding data to table
            for result in results1:
                table.add_row(result)
            for result in results2:
                table.add_row(result)
            print(table)#print table
        else:
            print("No results found.")
            
    elif a == "3":
        value1 = input("Enter the first model name: ")#user input taken
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)#execute mysql code
        results1 = self.mycursor.fetchall()#fetch current data
    
        value2 = input("Enter the second model name: ")#user input taken
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)#execute mysql taken
        results2 = self.mycursor.fetchall()#fetch current data

        value3 = input("Enter the third model name: ")#user input taken
        sql3 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val3 = (value3,)
        self.mycursor.execute(sql3, val3)#execute mysql data
        results3 = self.mycursor.fetchall()#fetch current data
    
        if results1 and results2 and results3:
            #setting table configration
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            #adding data to table
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
        value1 = input("Enter the first model name: ")#user input taken
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)#execute mysql code
        results1 = self.mycursor.fetchall()#fetch current data
    
        value2 = input("Enter the second model name: ")#user input taken
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)#execute mysql code
        results2 = self.mycursor.fetchall()#fetch current data

        value3 = input("Enter the third model name: ")#user input data
        sql3 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val3 = (value3,)
        self.mycursor.execute(sql3, val3)#execute mysql code
        results3 = self.mycursor.fetchall()#fetch current data

        value4 = input("Enter the fourth model name: ")#user input taken
        sql4 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val4 = (value4,)
        self.mycursor.execute(sql4, val4)#execute mysql code
        results4 = self.mycursor.fetchall()#fetch current data
        
        if results1 and results2 and results3 and results4:
            #creating table configration
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            #adding data to table
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
        value1 = input("Enter the first model name: ")#user input taken
        sql1 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val1 = (value1,)
        self.mycursor.execute(sql1, val1)#execute mysql code
        results1 = self.mycursor.fetchall()#fetch current data
    
        value2 = input("Enter the second model name: ")#user input taken
        sql2 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val2 = (value2,)
        self.mycursor.execute(sql2, val2)#execute mysql code
        results2 = self.mycursor.fetchall()#fetch current data

        value3 = input("Enter the third model name: ")#user input taken
        sql3 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val3 = (value3,)
        self.mycursor.execute(sql3, val3)#execute mysql code
        results3 = self.mycursor.fetchall()#fetch current data

        value4 = input("Enter the fourth model name: ")#user input taken
        sql4 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val4 = (value4,)
        self.mycursor.execute(sql4, val4)#execute mysql code
        results4 = self.mycursor.fetchall()#fetch current data
        
        value5 = input("Enter the fifth model name: ")#user input taken
        sql5 = f"SELECT * FROM specifications WHERE Model_name=%s"
        val5 = (value5,)
        self.mycursor.execute(sql5, val5)#execute mysql code
        results5 = self.mycursor.fetchall()#fetch current data
        
        if results1 and results2 and results3 and results4 and results5:
            #creating table configration
            table = PrettyTable()
            table.field_names = ["Model Name", "OS", "Memory", "Battery", "Price", "Camera", "Review"]
            #adding data to table
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
            
#object for class phonespecification made
phone_specs = PhoneSpecifications()
display()#display function called
while True:
  print("1. COMPARE PHONES")
  print("2. SEARCH PHONE SPECIFICATIONS")
  print("3. REVIEW A PHONE")
  print("4. DISPLAY")
  print("5. EXIT")

  choice = input("Enter your choice (1-5): ")
  if choice == "1":
    phone_specs.compare()#compare function called

  elif choice == "2":
    phone_specs.search()#search function called

  elif choice == "3":
    phone_specs.review()#review function called

  elif choice == "4":
    display_data()#display_data function called
    
  elif choice == "5":
      break#loop exitted
  else:
      print("Invalid choice. Please enter a number between 1 and 3.")



print("Program terminated. Run again.")

