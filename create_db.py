import sqlite3

# 连接到数据库，如果不存在则创建
conn = sqlite3.connect('example.db')

# 创建一个游标对象来执行SQL语句
cursor = conn.cursor()

# 创建一个名为 'users' 的表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    );
''')

# 插入一些示例数据
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25);")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 30);")

# 提交更改并关闭连接
conn.commit()
conn.close()
