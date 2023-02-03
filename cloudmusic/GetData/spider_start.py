# 主程序

#coding: utf-8
import music_mysql
import comment
import mysql_to_excel_txt
import songs_data



def spider_start():
    songs_name_data=songs_data.get_songs()
    print(len(songs_name_data))
    # mysql_to_excel_txt.drop_txt('GetData')
    # mysql_to_excel_txt.drop_txt('location')
    # 遍历想要爬取的歌曲，并将其评论用户的（id,name,GetData）添加到user_comment数据中
    # for table_name,id in songs_name_data.items():
        #GetData.get_comment(id,table_name)
        # mysql_to_excel_txt.mysql_to_excel(table_name)
        # mysql_to_excel_txt.mysql_command_to_txt(table_name,'GetData')
        # mysql_to_excel_txt.mysql_command_to_txt(table_name,'location')
        # pass
if __name__ == '__main__':
    spider_start()