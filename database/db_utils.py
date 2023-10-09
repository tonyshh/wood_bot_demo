import sqlite3

def create_connection():
    conn = sqlite3.connect('your_database_name.db')
    return conn

def add_ad(user_id, description, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ads (user_id, description, price) VALUES (?, ?, ?)", (user_id, description, price))
    conn.commit()
    conn.close()

# Позже доюавлю другие функции

def get_all_ads():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, description, price FROM ads")
    all_ads = cursor.fetchall()
    conn.close()
    return all_ads

