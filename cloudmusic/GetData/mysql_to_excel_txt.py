# 将Mysql数据库中数据存储为excel或txt，便于可视化设计
# 导入相关模块
import os.path

import eel
import pymysql
import xlwt
import songs_data

def drop_txt(command):
    filepath = 'D://Desktop//cloudmusic//comment_txt//'+command
    if os.path.exists(filepath):
        os.remove(filepath)
        print('成功删除 '+command+' 文档。')

def create_doc():
    filepath = '..//static//document'
    if not os.path.exists(filepath):
        os.mkdir(filepath)
        print('成功创建'+filepath+'文件夹')
    return filepath

def Connect_mysql():
    # 连接数据库
    db = pymysql.connect(host="localhost", user="root",
                         password="root", db="cloudmusic", port=3306)
    # 创建游标
    cursor = db.cursor()

    return cursor

def mysql_to_excel(table_name):
    if not os.path.exists('D:\Desktop\cloudmusic\评论'):
        os.makedirs('D:\Desktop\cloudmusic\评论')
    cursor = Connect_mysql()
    # 执行sql语句
    sql = "select * from `"+table_name+'`;'
    cursor.execute(sql)
    # 获取所有记录
    results = cursor.fetchall()
    # 创建excel
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    # 写入excel
    data = ['musicname','id','name','GetData','likeCound','timeStr','isvip','vipLevel','location','emo_result']
    for i in range(len(data)):
        sheet.write(0,i,data[i])
    for row in range(1, len(results)):
        for col in range(0, len(results[row])):
            sheet.write(row, col, results[row][col])
    # 保存excel
    table_name = "“"+table_name+"”"
    table_name = table_name.replace('?','')
    filepath ='D://Desktop//cloudmusic//评论//'+table_name +'.xls'
    wbk.save(filepath)
    print(table_name+'成功存至excel')


def mysql_command_to_txt(table_name,command):
    filepath = create_doc()
    filepath = '../tool'
    # 创建游标
    cursor = Connect_mysql()
    # 执行sql语句
    sql = "select "+command+" from `" + table_name + '`;'
    cursor.execute(sql)
    # 获取所有记录
    results = cursor.fetchall()
    with open(filepath+'//'+command+'.txt', 'a+', encoding='utf-8') as fp:
        for data in results:
            fp.write(data[0])
            fp.write('\n')
    print(table_name + '文档评论已存储入'+command+'.txt中')

def get_Comment_txt():
    songs = songs_data.get_songs()
    for song_name in songs.keys():
        mysql_command_to_txt(song_name,'GetData')

def get_CommentCount(tablename):

    cursor = Connect_mysql()
    # 执行sql语句
    sql = "select `musicname`,count(`GetData`) from `{}`".format(tablename)
    cursor.execute(sql)
    # 获取所有记录
    results = cursor.fetchall()
    dict = {
        results[0][0]:results[0][1],
    }
    return dict


def get_emo_count(tablename):
    # 创建游标
    cursor = Connect_mysql()
    # 执行sql语句
    sql_pos = "select `musicname`,count(`GetData`) from `{}` where emo_result='pos'".format(tablename)
    cursor.execute(sql_pos)
    # 获取所有记录
    results_pos = cursor.fetchall()
    sql_neu = "select `musicname`,count(`GetData`) from `{}` where emo_result='neu'".format(tablename)
    cursor.execute(sql_neu)
    results_neu = cursor.fetchall()
    sql_neg = "select `musicname`,count(`GetData`) from `{}` where emo_result='neg'".format(tablename)
    cursor.execute(sql_neg)
    results_neg = cursor.fetchall()
    dict_pos = {
        results_pos[0][0]: results_pos[0][1],
    }
    dict_neu = {
        results_neu[0][0]: results_neu[0][1],
    }
    dict_neg = {
        results_neg[0][0]: results_neg[0][1],
    }
    return dict_pos,dict_neu,dict_neg



def get_vipCount(tablename):
    # 创建游标
    cursor = Connect_mysql()
    # 执行sql语句
    sql_isvip = "select `musicname`,count(`isvip`) from `{}` where isvip = '是'".format(tablename)
    cursor.execute(sql_isvip)
    # 获取所有记录
    results = cursor.fetchall()
    dict = {
        results[0][0]: results[0][1],
    }
    return dict


def EmoCount_List():
    filepath = create_doc()
    list_pos = []
    list_neu = []
    list_neg = []
    name_list = songs_data.get_songs()
    for tablename in name_list.keys():
        dict_pos,dict_neu,dict_neg = get_emo_count(tablename)
        list_pos.append(dict_pos)
        list_neu.append(dict_neu)
        list_neg.append(dict_neg)
    with open(filepath+'//EmoCount.txt','w') as fp:
        fp.write(str(list_pos)+'\n'+str(list_neu)+'\n'+str(list_neg))
    return list_pos,list_neu,list_neg



def ComCount_List():
    count = 0
    commentCount = []
    filepath = create_doc()
    list = []
    name_list = songs_data.get_songs()
    for tablename in name_list.keys():
        dict = get_CommentCount(tablename)
        list.append(dict)
    with open(filepath+'//CommentCount.txt','w') as fp:
        fp.write(str(list))
    return commentCount

def vipCount_List():
    count = 0
    filepath = create_doc()
    list = []
    musicname = []
    vipCount = []
    name_list = songs_data.get_songs()
    for tablename in name_list.keys():
        dict = get_vipCount(tablename)
        list.append(dict)
    with open(filepath+'//vipCount.txt','w') as fp:
        fp.write(str(list))
    for dic in list:
        for key,values in dic.items():
            musicname.append(key)
            vipCount.append(values)
            count += values
    print(vipCount)
    return list

def get_emo():
    list_emo_pos = []
    list_emo_neu = []
    list_emo_neg = []
    pos_emo_count = 0
    list_pos,list_neu,list_neg = EmoCount_List()
    for dic in list_pos:
        for emo in dic.values():
            pos_emo_count += emo
            list_emo_pos.append(emo)
    for dic in list_neu:
        for emo in dic.values():
            list_emo_neu.append(emo)
    for dic in list_neg:
        for emo in dic.values():
            list_emo_neg.append(emo)
    print(pos_emo_count)