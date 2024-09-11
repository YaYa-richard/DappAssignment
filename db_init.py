import sqlite3

def init_db():
    # 连接到数据库文件（如果不存在会自动创建）
    with sqlite3.connect('dapp.db') as conn:
        c = conn.cursor()
        # 创建表，如果表已存在则不会重复创建
        c.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()  # 提交事务

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")
