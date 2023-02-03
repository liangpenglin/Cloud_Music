#连接mysql数据库

# coding = utf-8
import pymysql
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'cloudmusic',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

def create_comment(table_name):
    db = pymysql.connect(**config)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql_drop = "drop table if exists `cloudmusic`.`" + table_name + "`;"
    sql_table = "CREATE TABLE `cloudmusic`.`" + table_name + "`(`musicname` TEXT NOT NULL , `id` INT(100) NOT NULL , `name` TEXT NOT NULL , `GetData` TEXT NOT NULL , `likeCound` INT(100) NOT NULL , `timeStr` TEXT NOT NULL, `isvip` TEXT NOT NULL,`vipLevel` INT(20) NOT NULL ,`location` TEXT NOT NULL,`emo_result` TEXT NOT NULL) ENGINE = MyISAM;"
    try:
        # 执行sql语句
        cursor.execute(sql_drop)
        cursor.execute(sql_table)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print('出现错误啦~错误是:', e)
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()

# 将用户(table_name, music_name , user_id, user_name, GetData, likeCound, timeStr, isvip,vipLevel,location,emo_result)添加到user_comment数据中
def insert_commnet(table_name,music_name,id, name, comment,likeCound,timeStr,isvip,vipLevel,location,emo_result):
    # Connect to the database
    db = pymysql.connect(**config)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql_insert = "INSERT INTO `cloudmusic`.`"+table_name+"` (`musicname` ,`id`, `name`, `GetData` ,`likeCound` ,`timeStr`, `isvip`,`vipLevel`,`location`,`emo_result`) VALUES (%s, %s, %s, %s , %s, %s, %s, %s, %s, %s)"
    try:
        # 执行sql语句
        cursor.execute(sql_insert, (music_name,id, name,comment,likeCound,timeStr,isvip,vipLevel,location,emo_result))
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print('出现错误啦~错误是:', e)
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()

def select_commentAndemo(table_name):
    count = 0
    pos_count = 0
    neg_count = 0
    # Connect to the database
    db = pymysql.connect(**config)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    SQL_SELECT_COMMENT = 'select count(`GetData`) from '+table_name
    SQL_SELECT_EMO_POS = "select count(`id`) from {} where `emo_result`='pos';".format(table_name)
    SQL_SELECT_EMO_NEG = "select count(`id`) from {} where `emo_result`='neg';".format(table_name)
    try:
        # 执行sql语句
        cursor.execute(SQL_SELECT_COMMENT)
        counts = cursor.fetchone()
        # 提交到数据库执行
        db.commit()
        for key in counts:
            count = counts[key]
        cursor.execute(SQL_SELECT_EMO_POS)
        counts = cursor.fetchone()
        db.commit()
        for key in counts:
            pos_count = counts[key]
        cursor.execute(SQL_SELECT_EMO_NEG)
        counts = cursor.fetchone()
        db.commit()
        for key in counts:
            neg_count = counts[key]
        return count,pos_count,neg_count
    except Exception as e:
        print('出现错误啦~错误是:', e)
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
    pass
