# 获取用户数据、评论

# coding = utf-8
import demoji
from Crypto.Cipher import AES
import base64
import requests
import json
import music_mysql
import time
import sentiment
# headers
headers = {
    'Referer': 'http://music.163.com/',
    'Cookie': '_ntes_nuid=e358c035194e85e2f34c89bffe8679d1; appver=1.5.0.75771;MUSIC_U=601bb566023d5e3624646395e8a5172a780b772014e079de0a8ecce48dc9ce0d993166e004087dd3beec47810f46c5d15effa01b242951c545b68ec3c2e42745f96d23638c58e939d4dbf082a8813684;'
}
#获取params
def get_params(first_param, forth_param):
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key.encode(), iv.encode())
    h_encText = AES_encrypt(h_encText.decode(), second_key.encode(), iv.encode())
    return h_encText.decode()


# 获取encSecKey
def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


# 解AES秘
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text.encode())
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


# 获取json数据
def get_json(url, data):
    response = requests.post(url, headers=headers, data=data)
    return response.content


# 传入post数据
def crypt_api(id, offset):
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s/?csrf_token=" % id
    first_param = "{rid:\"\", offset:\"%s\", total:\"true\", limit:\"20\", csrf_token:\"\"}" % offset
    forth_param = "0CoJUm6Qyw8W8jud"
    params = get_params(first_param, forth_param)
    encSecKey = get_encSecKey()
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    return url, data


def get_comment(id,table_name):
    try:
        offset = 0
        music_mysql.create_comment(table_name)
        url, data = crypt_api(id, offset)
        json_text = get_json(url, data)
        json_dict = json.loads(json_text.decode("utf-8"))
        comments_sum = json_dict['total']
        for i in range(0, 3000, 20):
            offset = i
            url, data = crypt_api(id, offset)
            json_text = get_json(url, data)
            json_dict = json.loads(json_text.decode("utf-8"))
            json_comment = json_dict['comments']
            # 以json字典格式存储每个用户的信息
            for json_comment in json_comment:
                music_name = table_name
                user_id = json_comment['user']['userId']  # 获取用户ID
                user_name = json_comment['user']['nickname']  # 获取用户昵称
                user_name = str(user_name)
                comment = json_comment['content']  # 获取评论数据
                comment = demoji.replace_with_desc(comment)  # 将表情符转化为字符
                # print(json_comment)
                isvip = '否'  # 是否属于会员
                vipLevel = 0  # 会员等级
                if json_comment['user']['vipType'] == 11:
                    isvip = '是'
                    vipLevel = json_comment['user']['vipRights']['redVipLevel']
                likeCound = json_comment['likedCount']  # 点赞人数
                timeStr = json_comment['timeStr']  # 评论时间
                location = json_comment['ipLocation']['location']

                if not comment or not user_name or not user_name.isalnum():  # 去除空评论字段
                    continue

                # 利用snownlp进行情感分析
                emo_result = sentiment.snowanalysis(comment)  # 该评论的情感

                # 添加评论的ID，名字以及评论到数据库中
                music_mysql.insert_commnet(table_name, music_name ,user_id, user_name, comment, likeCound, timeStr, isvip, vipLevel,
                                           location, emo_result)
                print("用户ID:", user_id, end=" ")
                print("昵称:", user_name, end=" ")
                print("已经添加到'" + table_name + "'表中啦")
            time.sleep(0.5)
        print("用户评论获取结束！")

    except Exception as e:
        print('出现错误啦~错误是:', e)
        pass

