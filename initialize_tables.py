import sqlite3
from pathlib import Path

def create_tables():
    # Path to SQLite database
    db_path = Path('db.sqlite3')
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations_table (
        table_id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_no INTEGER NOT NULL UNIQUE,
        max_capacity INTEGER NOT NULL,
        available BOOLEAN NOT NULL
    )
    ''')
    
    # Insert 100 tables with capacities alternating between 2-6
    for i in range(1, 101):
        capacity = (i % 5) + 2  
        cursor.execute('''
        INSERT OR IGNORE INTO reservations_table (table_no, max_capacity, available)
        VALUES (?, ?, ?)
        ''', (i, capacity, True))
    
    # Commit and close
    conn.commit()
    conn.close()
    print("Successfully created 100 tables in the database")

if __name__ == '__main__':
    create_tables()