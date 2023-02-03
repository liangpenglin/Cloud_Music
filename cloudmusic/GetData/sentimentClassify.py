#此模块可以用于后面在网页中输入评论，及时得出情感倾向，精确度高，但是一次仅能分析几条数据
#用于在网页中进行实时评论情感分析


import aip


def get_AipNlp():

    client_aip="29659839"
    client_ak="R8Ds4MPnWdACyP8fPZgHQ1k3"
    client_sk="KDHbFiOMN90wjVjLSrpavBz18obcuRdj"

    return client_aip,client_ak,client_sk


def sentimentClassify(my_txt):
    client_aip,client_ak,client_sk = get_AipNlp()

    my_nlp = aip.nlp.AipNlp(client_aip,client_ak,client_sk)
    sentimentClassify_positive_prob = my_nlp.sentimentClassify(my_txt)['items'][0]['positive_prob']
    sentimentClassify_negative_prob = my_nlp.sentimentClassify(my_txt)['items'][0]['negative_prob']
    return sentimentClassify_positive_prob,sentimentClassify_negative_prob

# strs = "这首歌不好听"
# sentimentClassify_positive_prob,sentimentClassify_negative_prob = sentimentClassify(strs)
# if sentimentClassify_positive_prob > 0.6:
#     print('根据情感分析，该评论的情感倾向有 ' + str(sentimentClassify_positive_prob * 100) + '% 为积极\n(๑•̀ㅂ•́)و✧')
# if sentimentClassify_negative_prob > 0.6:
#     print('根据情感分析，该评论的情感倾向有 ' + str(sentimentClassify_negative_prob * 100) + '% 为消极\n(ಥ﹏ಥ)')