# oodp_hackathon2023
OODP Hackathon. Held on 27th and 28th April of 2023. Project is based on mobile phones' specifications comparison based system. Being updated to somewhat industry standard. Participants include:

1.Aankit Satpathy (https://github.com/aankitsatpathy)
2.Alok Chedambath (https://github.com/AlokChedambath64)
3.Divyanshu Kumar (https://github.com/DudeDiv)
4.Sanya Mathur (https://github.com/SanyaMathur0411)
5.Sidhansu Keshri (https://github.com/sidhansukeshri)
Project was made using functionalities or features or concepts of Object Oriented Programming (OOPs) and Designing. We mainly used Python IDLE, mySQL to work on database and backend coding. For the designing part, we used StarUML to create UML diagrams (behavioural and structural).

Explanation for the "admin.py" code:

This code is a Python program for managing phone specifications using MySQL database. The program provides four options to the user:

Add a new phone specification to the database
Delete a phone specification from the database
Modify a phone specification in the database
Exit the program The program first imports the necessary modules - mysql.connector and PrettyTable. It then connects to the MySQL server and selects the database called "phone_specifications".
Next, there are four functions defined:

display_data() function is used to retrieve all phone specifications from the database and display them in a formatted table using the PrettyTable library.

add_data() function is used to add a new phone specification to the database. The user is prompted to enter the values for Model Name, OS, Memory, Battery, Price, Camera and Review. The values entered are then inserted into the "specifications" table in the database.

delete_data() function is used to delete a phone specification from the database. The user is prompted to enter the Model Name of the phone specification to be deleted. The specified record is then deleted from the "specifications" table in the database.

modify_data() function is used to modify a phone specification in the database. The user is prompted to enter the Model Name of the phone specification to be modified, the field name to be modified, and the new value for the specified field. The specified record is then updated in the "specifications" table in the database.

After defining the functions, the program displays all the phone specifications using the display_data() function. Then the program enters a while loop, which provides the user with options to either add a new phone specification, delete a phone specification, modify a phone specification or exit the program. Depending on the user's choice, the corresponding function is called.

Finally, the display_data() function is called again to display all the phone specifications after the modifications are made.
