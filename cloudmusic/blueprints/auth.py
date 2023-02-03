
from flask import Blueprint,render_template
from flask import request

from GetData.sentimentClassify import sentimentClassify

# auth：蓝图名字;url_prefix：前缀
bp = Blueprint("auth",__name__,url_prefix="/")


@bp.route('/index.html')
def index():
    return render_template('index.html')

@bp.route('/')
def home():
    return index()

@bp.route("/wordcloud.html")
def get_buttons():
    return render_template("wordcloud.html")

@bp.route("/cards.html")
def get_cards():
    return render_template("cards.html")

@bp.route("/charts.html")
def get_charts():
    return render_template("charts.html")

@bp.route("/create-account.html")
def get_create_account():
    return render_template("create-account.html")

@bp.route("/forgot-password.html")
def get_forgot_password():
    return render_template("forgot-password.html")


@bp.route("/login.html")
def get_login():
    return render_template("login.html")

@bp.route("/affective_prediction.html",methods=['POST','GET'])
def get_modals():
    if request.method == 'GET':
        return render_template('affective_prediction.html')
    else:
        results = request.form
        comment_text = results['profession']
        sentimentClassify_positive_prob, sentimentClassify_negative_prob = sentimentClassify(comment_text)
        if sentimentClassify_positive_prob > 0.6:
            comment_text = '您输入的内容为：{}'.format(comment_text)
            comment_result = '根据情感分析，该评论的情感倾向有 ' + str(sentimentClassify_positive_prob * 100) + '% 为积极'
            return render_template("affective_prediction.html",comment_text = comment_text,comment_result=comment_result)
        if sentimentClassify_negative_prob > 0.6:
            #(ಥ﹏ಥ)
            comment_text = '您输入的内容为：{}'.format(comment_text)
            comment_result = '根据情感分析，该评论的情感倾向有 '+str(sentimentClassify_negative_prob * 100) + '% 为消极'
            return render_template("affective_prediction.html",comment_text = comment_text,comment_result = comment_result)


