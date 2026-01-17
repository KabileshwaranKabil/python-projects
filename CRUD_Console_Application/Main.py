import os 
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

def init_connection():
	load_dotenv() # load dotenv
	try:
		conn=mysql.connector.connect(
			host=os.getenv('DB_HOST','localhost'),
			port=os.getenv('DB_PORT',3307),
			user=os.getenv('DB_USER','root'),
			password=os.getenv('DB_PASSWORD'),
			database=os.getenv('DB_NAME','studentsdb')
		)
		if conn.is_connected():
			return conn
	except Error as e:
		print(f'Database Error {e}')

def get_valid_id():
	while True:
		reg_no=input("Enter Your Registration No: ").strip()
		if len(reg_no)>=5:
			return reg_no
		print("Registration Number Format : (e.g. 22/COM/10)")

def get_valid_email():
	import re
	while True:
		email=input("Enter Email: ").strip()
		pattern =r'[a-zA-z0-9._%+-]+@[a-zA-z0-9._]+\.[a-zA-Z]{2,}$'
		if re.match(pattern,email):
			return email
		print(f'Invalid Email format')

# Add a new student
def add_student(conn):
	try:
		cursor=conn.cursor()
		reg_no=get_valid_id()
		name=input("Enter Name: ").strip()
		email=get_valid_email()
		address=input("Enter Address: ")
		sql='insert into students(RegNo,Name,Email,Address) values(%s,%s,%s,%s)'
		values=(reg_no,name,email,address)
		cursor.execute(sql,values)
		conn.commit()
		print(f'\n\tnew student is added to database')
	except Error as e:
		print(f'Database Error {e}')
		conn.rollback()
	finally:
		cursor.close()

# Display student details
def view_students(conn):
	cursor=conn.cursor()
	cursor.execute('select * from students')
	rows=cursor.fetchall()
	for row in rows:
		print(row)
	cursor.close()

# Update student information
def update_student(conn):
	try:
		cursor=conn.cursor()
		reg_no=get_valid_id()
		email=get_valid_email()
		sql='update students set email=%s where RegNo=%s'
		values=(email,reg_no)
		cursor.execute(sql,values)
		conn.commit()
		print(f'\n\tupdated {reg_no} student details')
	except Error as e:
		print(f'Database Failed')
		conn.rollback()
	finally:
		cursor.close()

# Delete a particular student
def delete_student(conn):
	try:
		cursor=conn.cursor()
		name=input("Enter name of the student to delete: ").strip()
		sql='delete from students where name=%s'
		values=(name,)
		cursor.execute(sql,values)
		conn.commit()
		print(f'\n\t {name}\'s details deleted from database')
	except Error as e:
		print(f'Failed to delete')
		conn.rollback()
	finally:
		cursor.close()


def get_menu_choice():
	while True:
		choice=input("\n1. Add a new student\n2. Display student details\n3. Update student information\n4. Delete a particular student\n5. Exit\n:> ").strip()
		if choice in ['1','2','3','4','5']:
			return int(choice)
		print(f'Invalid choice!')

def main():
	conn=init_connection()
	if not conn:
		return

	try:
		while True:
			choice=get_menu_choice()
			if choice==1:
				add_student(conn)
			elif choice ==2:
				view_students(conn)
			elif choice == 3:
				update_student(conn)
			elif choice == 4:
				delete_student(conn)
			else:
				print(f'Thank you!')
				break
	finally:
		conn.close()


if __name__=="__main__":
	main()