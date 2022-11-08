from datetime import datetime

def Save_data_csv(name_list, date_list, content_list, score_list):
    # CSV 파일로 저장
    import csv

    filename = datetime.now().strftime('result/%Y-%m-%d_%H시%M분-%S초.csv')
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'date', 'content', 'score']) # CSV 파일의 첫 줄에 각 컬럼의 이름을 적어줌

        for i in range(len(name_list)): # 각 리뷰의 정보를 CSV 파일에 저장
            writer.writerow([name_list[i], date_list[i], content_list[i], score_list[i]])
