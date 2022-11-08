import pymysql

def Save_data_mysql(name_list, date_list, content_list, score_list):
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='review_data', charset='utf8mb4') #SQL 연동
    cursor = db.cursor()    #SQL 연동
    cursor.execute("USE review_data")   # review_data DB 사용

    # 데이터베이스에 저장
    for i in range(len(name_list)): # 각 리뷰의 정보를 데이터베이스에 저장
        print('==================='+str(i+1)+'================')

        # SQL 쿼리문
        sql = "INSERT INTO review VALUES("+ str(i+1) +",'" + name_list[i] + "', " + date_list[i] + ", '" + content_list[i] + "', " + str(score_list[i]) +");" 
        cursor.execute(sql) # SQL 쿼리문 실행
        
    db.commit() # SQL 쿼리문 실행
    db.close()  # 데이터베이스 연결 종료