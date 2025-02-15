# import cv2
# import face_recognition
# import sqlite3
# import csv
# import numpy as np
# import os

# DB_PATH = "face_login.db" 

# def create_database():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute()
#     conn.commit()
#     conn.close()
    
# def save_user(name, face_encoding):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO USERS (name, face_encoding)", (name, face_encoding.tobyte()))
#     conn.commit()
#     conn.close()
    
# def get_registered_users():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, face_encoding FROM users")
#     users = cursor.fetchall() #method used with database cursors in SQLite
#     conn.close()
    
#     known_faces = {}
#     for name, encoding in users:
#         known_faces[name] = np.frombuffer(encoding, dtype=np.float64)
        
#     return known_faces

# def capture_face():
#     video_capture = cv2.VideoCapture(0)
    
#     while True:
#         ret, frame = video_capture.read()
#         cv2.imshow("Capture Face (Press 'c' to capture)", frame)
        
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord('c'):
#             video_capture.release()
#             cv2.destroyAllWindow()
#             break
        
#     face_encoding = face_recognition.face_encoding(frame)
#     if len(face_encoding) > 0:
#         return face_encoding[0] 
#     else:
#         print("No face detected.")
#         return None
    
# def signup():
#     name = input("Enter your name: ").strip()
    
#     registered_users = get_registered_users()
#     if name in registered_users:
#         print("User already exists!")
#         return
    
#     print("Capturing your face for registration...")
#     face_encoding = capture_face()
    
#     if face_encoding is not None:
#         save_user(name, face_encoding)
#         print("Signup Successful!")
        
# def login():
#     print("Capturing your face for login...")
#     face_encoding = capture_face()
    
#     if face_encoding is None:
#         return
    
#     registered_users = get_registered_users()
    
#     for name, stored_encoding in registered_users.items():
#         match = face_recognition.compare_faces([store_encoding], face_encoding[0])
#         if match:
#             print(f"Login Successfully")
#             return
        
#         print("Login failed")
        
# #main
# if __name__ == "__LOGIN_OR_SIGNUP__":
#     create_database()
    
#     while True:
#         print("\n1. SignUp (Registration)")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Choose an option: ")
        
#         if choice == "1":
#             signup()
#         elif choice == "2":
#             login()
#         elif choice == "3":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice")

import csv
import sqlite3
import mysql.connector

def get_user_input():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    return name, age, email

def save_to_csv(data, filename='data.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("Data saved to CSV successfully!")

def save_to_sqlite(data, db_name='data.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        age INTEGER,
                        email TEXT)''')
    
    # Insert data
    cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", data)
    conn.commit()
    conn.close()
    print("Data saved to SQLite database successfully!")
    
def save_to_mysql(data, host = 'localhost', user = 'root', password = '', database = 'testdb'):
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255),
                        age INT,
                        email VARCHAR(255))''')
    
    cursor.execute("INSERT INTO users (name, age, email) VALUES (%s, %s, %s)", data)
    conn.commit()
    conn.close()
    print("Data saced to MySQL database successfully!")
    
if __name__ == "__main__":
    user_data = get_user_input()
    save_to_csv(user_data)
    save_to_sqlite(user_data)
    save_to_mysql(user_data)
    
