#获取词云

import os

from get_pic import create_path,fenci_df,TfidfVectorizer,WordCloud,plt,pd
from matplotlib.image import imread
def get_word_cloud():
    mk = imread('D:\Desktop\毕业设计\cloudmusic\comment\wukong.png', str(1))
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
    wordcloud = WordCloud(font_path="../tool/msyh.ttf", mask=mk, background_color='white', width=2800, height=1200, max_words=300,
                          max_font_size=180).generate_from_frequencies(pos_res)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    # wordcloud.to_file('ciyun.jpg')
    plt.savefig('ciyun.jpg')
    # plt.savefig(pic_path+'/word_cloud.jpg')
get_word_cloud()