import pymssql

connect = pymssql.connect('DS918:49153', 'sa', '4817@Foic_', 'TsetDB', autocommit=True)
if connect:
    print('链接成功！')
cursor = connect.cursor()

with open('3.txt', 'a+', encoding='utf-8') as sqlfs:
    sqlfs.seek(0)
    models = sqlfs.read().split('\n')
    for model in models:
        url = model.split('?n=')[0]
        title = model.split('?n=')[1]
        print(url, title)
        # sql = 'insert into T_Models (Title,Url) values(' + title + ',' + url + ')'
        # cursor.execute(sql)
    # connect.commit()
    cursor.close()
    connect.close()
