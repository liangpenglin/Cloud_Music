#

# coding = utf-8
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np

import pymysql
comment = []

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'cloudmusic',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

def mysql(table_name):
    db = pymysql.connect(**config)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = 'select * from '+table_name
    data = cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print(data)

def snowanalysis(comment):
    s = SnowNLP(comment)
    content_emotion_positive_prob = s.sentiments
    if content_emotion_positive_prob > 0.5:
        return 'pos'  # 积极
    elif content_emotion_positive_prob > 0.2:
        return 'neu'  # 中立
    else:
        return 'neg'

def snowanalyse(self):
    sentimentslist = []
    for li in self:
        print(li)
        s = SnowNLP(li)
        print(s.sentiments)
        sentimentslist.append(s.sentiments)
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01))
    plt.xlabel("The comments distribution")
    plt.show()
    print(sentimentslist)

    for i in range(len(sentimentslist)):
        if (sentimentslist[i] > 0.5):
            sentimentslist[i] = 1
        else:
            sentimentslist[i] = -1
    print(sentimentslist)
    info = []
    a = 0
    b = 0
    for x in range(0, len(sentimentslist)):
        if (sentimentslist[x] == 1):
            a = a + 1
        else:
            b = b + 1
    info.append(b)
    info.append(a)
    info2 = ['negative', 'positive']
    plt.bar(info2, info, tick_label=info2, color='#2FC25B')
    plt.xlabel("comments analyst")
    plt.show()

mysql('antihero')