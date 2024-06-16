import sqlite3

def init_db():
    conn = sqlite3.connect('db/users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            uid INTEGER PRIMARY KEY,
            name TEXT,
            direction TEXT,
            avito_accounts INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_user(uid, name, direction):
    conn = sqlite3.connect('db/users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (uid, name, direction) VALUES (?, ?, ?)', (uid, name, direction))
    conn.commit()
    conn.close()

def get_user(uid):
    conn = sqlite3.connect('db/users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE uid = ?', (uid,))
    user = c.fetchone()
    conn.close()
    return user

def account_increment(uid):
    uid = int(uid)
    conn = sqlite3.connect('db/users.db')
    c = conn.cursor()
    c.execute('SELECT avito_accounts FROM users WHERE uid = ?', (uid,))
    counter = sum(c.fetchone())
    counter += 1
    c.execute('UPDATE users SET avito_accounts = ? WHERE uid = ?', (counter, uid))

    conn.commit()
    conn.close()
