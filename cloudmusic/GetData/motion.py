#用于将全部评论进行情感分析（分析精确度没sentimentClassify高，但一次可分析多条数据）
import json
import requests

def get_token():

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=R8Ds4MPnWdACyP8fPZgHQ1k3&client_secret=KDHbFiOMN90wjVjLSrpavBz18obcuRdj'
    response = requests.get(host)

    my_token = response.json()['access_token']
    return my_token

def get_header():
    # 函数传参，固定值
    header = {
        "Content-Type": "application/json"
    }
    return header

def get_myurl():
    # 根据官网获取api接口地址，并凭借对应参数
    my_token = get_token()
    url1 = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify'
    myurl = url1 + '?charset=UTF-8&access_token=' + my_token
    return myurl

def get_emotion(mystr):

    header = get_header()
    myurl = get_myurl()
    #函数输入文本的 json 格式，用于接收文本，并转为json
    content_txt = json.dumps({
        "text": mystr
    })

    #发起请求，并提取关键信息，共2处，文本的情感正向数值
    results = requests.post(url=myurl, headers=header, data=content_txt).json()
    print(results)
    print(results['items'])
    content_emotion_positive_prob= results['items'][0]['positive_prob']
    if content_emotion_positive_prob >0.7:
        return 'pos'        #积极
    elif content_emotion_positive_prob>0.4:
        return 'neu'        #中立
    else:
        return 'neg'
