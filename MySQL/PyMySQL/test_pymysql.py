import pymysql
 
# 1. db connection
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'password',
    db = 'classicmodels',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor,  # type: ignore # DictCursor을 통해서 cursor을 dictionary 화 시키다
)

# 2.1 CRUD
def get_customers():
    cursor = connection.cursor()

    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()   # sql 쿼리를 날려서, cursor을 실행하면, fetchall(전부) 가져온다.

    # print("customers : ", customers)
    # print("customers : ", customers['customerNumber'])
    # print("customers : ", customers['customerName'])
    # print("customers : ", customers['country'])
    cursor.close()

# 2.2 SELECT * FROM
# def add_customer():
#     cursor = connection.cursor()

#     name = 'dohyun'
#     family_name = 'kim'
#     sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES({1004}, '{name}', '{family_name}')"
#     cursor.execute(sql)
#     connection.commit() # 쿼리를 실행한 결과를 데이터베이스에 반영
#     cursor.close()

# add_customer()

# 2.3 UPDATE_INTO
# def update_customer():
#     cursor = connection.cursor()
#     update_name = 'update_Dohyun'
#     contactLastName = 'update_Kim'

#     sql = f"UPDATE customers SET customerName ='{update_name}', contactLastName='{contactLastName}' WHERE customerNumber=1000"
#     cursor.execute(sql)
#     connection.commit()
#     cursor.close()

# update_customer()

# 2.4 DELETE FROM]
def delete_customer():
    cursor = connection.cursor()

    sql = "DELETE FROM customers WHERE customerNumber=1004"

    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()