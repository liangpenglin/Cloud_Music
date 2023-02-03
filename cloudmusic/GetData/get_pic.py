#获取各种图的图片

"""
导入各种包
"""
# 分词
import jieba
# 数据处理
import pandas as pd

# 用来关闭警告
import warnings

from sklearn.feature_extraction.text import TfidfVectorizer

import matplotlib as plt
# 基于matplotlib更便捷的画图
import seaborn as sns
# 为了图片可以使用中文
from pylab import *
# 来画云词图
from wordcloud import WordCloud
import os


#不显示警告
warnings.filterwarnings("ignore")

# 设置字体
sns.set(font_scale=1.2)
# 设置线条
sns.set(rc={"lines.linewidth":1})
# 设置风格
sns.set_style("whitegrid")
# 设置中文
mpl.rcParams['font.sans-serif'] = u'SimHei'
plt.rcParams['axes.unicode_minus'] = False


def get_arguements():
    path1 = 'D:/Desktop/cloudmusic/评论'
    # 获得顺序的excel名
    path1_list = os.listdir(path1)
    # 读取并合并数据
    df = pd.DataFrame(
        columns=['musicname', 'id', 'name', 'GetData', 'likeCound', 'timeStr', 'isvip', 'vipLevel', 'location',
                 'emo_result'])
    return path1_list,df

# 获取excel数据
def get_df_data():
    path1_list,df = get_arguements()
    for path in path1_list:
        data = pd.read_excel('D:/Desktop/cloudmusic/评论/' + path)[
            ['musicname', 'id', 'name', 'GetData', 'likeCound', 'timeStr', 'isvip', 'vipLevel', 'location',
             'emo_result']]
        df = pd.concat([df, data], ignore_index=True)  # ignore_index:否则index也会合并
    return df

def create_path():
    pic_path = 'D:/Desktop/cloudmusic/picture'
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    pic_every_music_emo_circle = pic_path+'/every_music_emo_circle'
    if not os.path.exists(pic_every_music_emo_circle):
        os.mkdir(pic_every_music_emo_circle)
    pic_every_music_vip_circle = pic_path+'/every_music_vip_circle'
    if not os.path.exists(pic_every_music_vip_circle):
        os.mkdir(pic_every_music_vip_circle)
    return pic_path

#分词函数
def fenci(text):
    # 保留中文、英文（jieba不会把英文单词分开）、*
#     cut_word = [i for i in list(jieba.cut(text)) if '\u4e00' <= i <= '\u9fff']
    # 只会比词的第一个（注意这里“\u0039”必须4个数，不够用0补）
    cut_word = [i for i in list(jieba.cut(text)) if '\u4e00' <= i <= '\u9fff' or '\u0030' <= i <= '\u0039' or '\u0061' <= i <= '\u007a' or '\u0041' <= i <= '\u005a' or i == '\u002A']
    text = ' '.join(cut_word)
    return text

def fenci_df():
    df = get_df_data()
    df = df.reset_index(drop=True)
    df['分词后'] = ''
    for i in range(len(df)):
        df['分词后'].iloc[i] = fenci(df['GetData'].iloc[i])
    return df

def get_vip_distribution_all_circle():
    df = get_df_data()
    pic_path = create_path()
    df_evaluate = df['vipLevel'].reset_index()
    df_evaluate.columns = ['Count', 'vipLevel']
    df_evaluate = df_evaluate.groupby("vipLevel").aggregate('count').reset_index()
    df_evaluate.sort_values(by='Count', inplace=True, ascending=True)

    plt.figure(figsize=(8, 6))
    plt.pie(df_evaluate['Count'], labels=df_evaluate['vipLevel'], autopct='%1.1f%%', shadow=False, radius=1.2)
    plt.savefig(pic_path+'/get_vip_distribution_all_circle.jpg')
    plt.show()

#总体的情感分布

def get_emo_distribution_all_circle():

    df = get_df_data()
    pic_path = create_path()
    df_evaluate = df['emo_result'].reset_index()
    df_evaluate.columns = ['Count', 'emo_result']
    df_evaluate = df_evaluate.groupby("emo_result").aggregate('count').reset_index()
    df_evaluate.sort_values(by='Count', inplace=True, ascending=True)

    plt.figure(figsize=(3, 6))
    plt.pie(df_evaluate['Count'], labels=df_evaluate['emo_result'], autopct='%1.1f%%', shadow=False, radius=1.2)
    plt.savefig(pic_path+'/get_emo_distribution_all_circle.jpg')
    plt.show()

#获取每首歌曲vip听众饼图
def get_vip_distribution_circle():
    pic_path = create_path()
    df = get_df_data()
    path1_list, df = get_arguements()
    for path in path1_list:
        music_name = path.split('.')[0]
        data = pd.read_excel('D:/Desktop/cloudmusic/评论/' + path)[
            ['musicname', 'id', 'name', 'GetData', 'likeCound', 'timeStr', 'isvip', 'vipLevel', 'location',
             'emo_result']]
        df = pd.concat([df, data], ignore_index=True)  # ignore_index:否则index也会合并
        data = pd.read_excel('D:/Desktop/cloudmusic/评论/' + path)[
            ['musicname', 'id', 'name', 'GetData', 'likeCound', 'timeStr', 'isvip', 'vipLevel', 'location',
             'emo_result']]
        df = pd.concat([df, data], ignore_index=True)  # ignore_index:否则index也会合并
        df = pd.concat([df, data], ignore_index=True)  # ignore_index:否则index也会合并
        df_evaluate = df['vipLevel'].reset_index()
        df_evaluate.columns = ['Count', 'vipLevel']
        df_evaluate = df_evaluate.groupby("vipLevel").aggregate('count').reset_index()
        df_evaluate.sort_values(by='Count', inplace=True, ascending=True)

        plt.figure(figsize=(8, 6))
        plt.pie(df_evaluate['Count'], labels=df_evaluate['vipLevel'], autopct='%1.1f%%', shadow=False, radius=1.2)
        plt.savefig(pic_path+'/every_music_vip_circle/'+music_name+'.jpg')

#获取每首歌曲情感倾向可视化图
def get_emo_distribution():
    pic_path = create_path()
    path1_list, df = get_arguements()
    for path in path1_list:
        data = pd.read_excel('D:/Desktop/cloudmusic/评论/' + path)[
            ['musicname', 'id', 'name', 'GetData', 'likeCound', 'timeStr', 'isvip', 'vipLevel', 'location',
             'emo_result']]
        music_name = path.split('.')[0]
        df = pd.concat([df, data], ignore_index=True)  # ignore_index:否则index也会合并
        df_evaluate = df['emo_result'].reset_index()
        df_evaluate.columns = ['Count', 'emo_result']
        df_evaluate = df_evaluate.groupby("emo_result").aggregate('count').reset_index()
        df_evaluate.sort_values(by='Count', inplace=True, ascending=True)
        title_word = '歌曲' + music_name.split('.')[0] + '评论情感分析图'
        plt.figure(figsize=(3, 6))
        plt.pie(df_evaluate['Count'], labels=df_evaluate['emo_result'], autopct='%1.1f%%', shadow=False, radius=1.2)
        plt.title(title_word)
        plt.savefig(pic_path+'/every_music_emo_circle/'+music_name+'_emo_distribution_circle.jpg')



#获取每首歌曲vip听众柱形图
def get_vip_distribution_column():
    pic_path = create_path()
    df = get_df_data()
    plt.figure(figsize=(20, 6))
    sns.histplot(data=df, x="musicname", hue="isvip", multiple="dodge", shrink=.8)
    # 旋转标签90度
    plt.xticks(rotation=90)
    plt.savefig(pic_path+'/vip_distribution_column.jpg')

#获取每首歌曲情感分析结果柱形图
def emo_result_distribution():
    pic_path = create_path()
    df = get_df_data()
    plt.figure(figsize=(20, 6))
    sns.histplot(data=df, x="musicname", hue="emo_result", multiple="dodge", shrink=.8)
    # 旋转标签90度
    plt.xticks(rotation=90)
    plt.savefig(pic_path+'/emo_result_distribution.jpg')

# 词云
def get_word_cloud():
    pic_path = create_path()
    df = fenci_df()
    # TfidfVectorizer = CountVectorizer + TfidfTransformer()
    pos = df[df['emo_result'] == 'pos']
    tv_pos_transfer = TfidfVectorizer()
    tv_pos_data = tv_pos_transfer.fit_transform(list(pos['分词后']))
    # 获得横坐标
    sorted_pos = sorted(tv_pos_transfer.vocabulary_.items(), key=lambda x: x[1])  # .items()可以遍历将{,,,,}变为[(,),(,)]
    # 变成dataframe
    sorted_pos = [i[0] for i in sorted_pos]
    df_pos = pd.DataFrame(tv_pos_data.toarray(), columns=sorted_pos)
    """
    根据权重排名，取出权重比较大的特征（）
    """
    pos_res = df_pos.mean().sort_values(ascending=False)
    plt.figure(figsize=(20, 9))
    wordcloud = WordCloud(font_path="../tool/msyh.ttf", background_color='white', width=2800, height=1200, max_words=300,
                          max_font_size=180).generate_from_frequencies(pos_res)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig(pic_path+'/word_cloud.jpg')




if __name__ == '__main__':
    # get_emo_distribution_all_circle()
    # get_vip_distribution_all_circle()
    # get_vip_distribution_circle()
    # get_emo_distribution()
    # get_vip_distribution_column()
    # emo_result_distribution()
    # get_word_cloud()
    pass