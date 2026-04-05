import pymysql

print("trying...")

try:
    connection = pymysql.connect(
        host     = 'localhost',
        user     = 'asteroid_user',
        password = 'asteroid123',
        database = 'asteroid_db'
    )
    print("connected!")
    connection.close()

except Exception as e:
    print(f"Error: {e}")