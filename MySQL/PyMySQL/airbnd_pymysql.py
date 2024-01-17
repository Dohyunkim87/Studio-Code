import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    db = 'airbnb',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:   # with 문 안에서는 connection.cursor()을 cursor이라 부름
    # # 문제1. 새로운 제품 추가
    # sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"   # %s로 데이터를 밖에서 받음
    # cursor.execute(sql, ('Python Book', 10000, 10))  # 앞에 온 데이터를 넣는것
    # connection.commit()

    # # 문제2. 고객 목록 조회
    # cursor.execute("SELECT * FROM Products")
    # for book in cursor.fetchall():
    #     print(book)

    # # 문제3. 제품 재고 업데이트
    # sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    # cursor.execute(sql, (1,1))
    # connection.commit()

    # # 문제4. 고객별 총 주문 금액
    # sql = "SELECT customerID, SUM(totalAmount) As TotalAmount FROM Orders GROUP By customerID"
    # cursor.execute(sql)
    # datas = cursor.fetchall()
    # print(datas)

    # # 문제5. 고객 이메일 업데이트
    # sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
    # cursor.execute(sql, ('oz@oz.com', 1))
    # connection.commit()

    # # 문제6. 주문 취소
    # sql = "DELETE From Orders WHERE orderID=%s"
    # cursor.execute(sql, (15))
    # connection.commit()

    # # 문제7. 특정 제품 검색
    # sql = "SELECT * FROM Products WHERE productName LIKE %s"   # 이경우에는 = 보다는 LIKE를 통해 비슷한 것을 찾을 수 있도록 한다
    # cursor.execute(sql, ('%Book%'))
    # datas = cursor.fetchall()

    # for data in datas:
    #     print(data['productName'])

    # # 문제8. 특정 고객의 주문 데이터 조회
    # sql = "SELECT * FROM Orders WHERE customerID = %s"
    # cursor.execute(sql, (1))
    # datas = cursor.fetchall()

    # for data in datas:
    #     print(data)

    # 문제9. 가장 많이 주문한 고객 찾기
    sql = """
            SELECT customerID, COUNT(*) as orderCount
            FROM Orders GROUP BY customerID
            ORDER BY orderCount DESC LIMIT 1
            """
    cursor.execute(sql)

    data = cursor.fetchone()
    print(data)
    

cursor.close()