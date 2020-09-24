from functools import reduce
import jieba
import jieba.analyse
import math


def resemble_cal(all_key,article1_dic,article2_dic):
    str1_vector=[]
    str2_vector=[]
    # 计算词频向量
    for i in all_key:
        str1_count = article1_dic.get(i,0)
        str1_vector.append(str1_count)
        str2_count = article2_dic.get(i,0)
        str2_vector.append(str2_count)
    # 计算各自平方和
    str1_map = map(lambda x: x*x,str1_vector)
    str2_map = map(lambda x: x*x,str2_vector)
    str1_mod =  reduce(lambda x, y: x+y, str1_map)
    str2_mod = reduce(lambda x, y: x+y, str2_map)
    # 计算平方根
    str1_mod = math.sqrt(str1_mod)
    str2_mod = math.sqrt(str2_mod)
    # 计算向量积
    vector_multi = reduce(lambda x, y: x + y, map(lambda x, y: x * y, str1_vector, str2_vector))
    # 计算余弦值
    cos = float(vector_multi)/(str1_mod*str2_mod)
    return cos
    return return_dic


'''
文章关键词提取
'''
def analyse_word(content):
    # 新建两个数组
    zidian={}
    return_dic={}
    # 内容分词
    fenci = jieba.cut_for_search(content)
    for fc in fenci:
        if fc in zidian:
            zidian[fc] += 1
        else:
            zidian[fc] = 1
    # 关键字的个数
    topK=100
    # 关键词  比率
    tfidf = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
    artice = open('C:/Users/Administrator.USER-20190905VU/Desktop/test/stop_word.txt', 'r', encoding='utf-8').read()
    # 要转换成字符串
    stopkeyword = [content.strip(str(artice))]
    for word_weight in tfidf:
        if word_weight in stopkeyword:
            continue
        frequence = zidian.get(word_weight[0], 'not found')
        return_dic[word_weight[0]]=frequence
    return return_dic



# set是把重复的去掉
all_key=set()
f = open('C:/Users/Administrator.USER-20190905VU/Desktop/test/orig.txt', 'r', encoding='utf-8')
lines = f.readlines()
lines = "".join(lines)
# print(lines)
article1_dic = analyse_word(lines)
print(article1_dic)
for k,v in article1_dic.items():
        all_key.add(k)
g = open('C:/Users/Administrator.USER-20190905VU/Desktop/test/orig_ 0.8_ del_10.txt', 'r', encoding='utf-8')
lines1 = g.readlines()
lines1 = "".join(lines1)
# print(lines1)
article2_dic = analyse_word(lines1)
print(article2_dic)
for k,v in article2_dic.items():
        all_key.add(k)
cos = resemble_cal(all_key,article1_dic,article2_dic)
print(cos)