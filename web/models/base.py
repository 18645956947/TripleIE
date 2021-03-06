import json

import pymysql


class Base():
    def __init__(self):
        pass

    def exec_sql(self, sql):
        result = ''
        # 打开数据库连接
        db = pymysql.connect(host='47.96.109.137',
                             port=3306,
                             user='root',
                             passwd='12345678',
                             db='kbqa',
                             charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)

        rs = cursor.fetchall()
        if rs:
            desc = cursor.description
            result = [dict(zip([col[0] for col in desc], row)) for row in rs]

        db.commit()
        # 关闭数据库连接
        db.close()

        return result


if __name__ == '__main__':
    sqlModel = Base()
    question = '2018年上海的城镇人口'
    norm_questions = json.dumps({'normalize_question': []})
    triples = json.dumps({'triples': []})

    insert_sql = ("INSERT INTO kb_questions (question,normalize_question,triples,create_time) "
                  "VALUES ('%s','%s','%s',NOW())" %
                  (question, norm_questions, triples))

    sqlModel.exec_sql(insert_sql)
    # rs = sqlModel.exec_sql("SELECT * FROM kb_questions WHERE id = 5")
    # print(rs[0]['triples'])
