#-*-coding : utf-8 -*-
from functools import reduce
import jieba
import jieba.analyse
import math
import sys


def resemble_cal(all_key, article1_dic, article2_dic):
    str1_vector = []
    str2_vector = []
    # 计算词频向量
    for i in all_key:
        # 返回字典article1_dic中i元素对应的值,若无，则进行初始化
        # 若不存在article1_dic，则字典article1_dic中生成i元素，并使其对应的数字为0
        str1_count = article1_dic.get(i, 0)
        # append函数会在数组后加上相应的元素
        str1_vector.append(str1_count)
        str2_count = article2_dic.get(i, 0)
        str2_vector.append(str2_count)
    # 计算各自平方和
    # map() 会根据提供的函数对指定序列做映射
    str1_map = map(lambda x: x * x, str1_vector)
    str2_map = map(lambda x: x * x, str2_vector)
    # reduce() 函数会对参数序列中元素进行累积
    str1_mod = reduce(lambda x, y: x + y, str1_map)
    str2_mod = reduce(lambda x, y: x + y, str2_map)
    # 计算平方根
    str1_mod = math.sqrt(str1_mod)
    str2_mod = math.sqrt(str2_mod)
    # 计算向量积
    vector_multi = reduce(lambda x, y: x + y,
                          map(lambda x, y: x * y, str1_vector, str2_vector))
    # 计算余弦值
    cos = float(vector_multi) / (str1_mod * str2_mod)
    return cos
    return return_dic


'''
文章关键词提取
'''


def analyse_word(content):
    # 新建两个数组
    zidian = {}
    return_dic = {}
    # 内容分词
    # jieba.cut_for_search 方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。
    # 该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
    fenci = jieba.cut_for_search(content)
    for fc in fenci:
        # 如果fc在fenci中
        if fc in zidian:
            zidian[fc] += 1
        else:
            zidian[fc] = 1
    # jieba.analyse.extract_tags(sentence, topK=5, withWeight=True, allowPOS=())
    # content 需要提取的字符串，必须是str类型，不能是list
    # topK 提取前多少个关键字
    # withWeight 是否返回每个关键词的权重
    # allowPOS是允许的提取的词性，默认为allowPOS=‘ns’, ‘n’, ‘vn’, ‘v’，提取地名、名词、动名词、动词

    # 关键字的个数
    topK = 100
    tfidf = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
    artice = open(
        'C:/Users/Administrator.USER-20190905VU/Desktop/3118005403/requirements/stop_word.txt',
        'r',
        encoding='utf-8').read()
    # 要转换成字符串
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    # 移除停用库里面的词
    stopkeyword = [content.strip(str(artice))]
    # 在tfidf中的字符中2
    for word_weight in tfidf:
        # 如果这个在停用词中
        if word_weight in stopkeyword:
            # continue 语句跳出本次循环，而break跳出整个循环。
            # continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分
            continue
        frequence = zidian.get(word_weight[0], 'not found')
        return_dic[word_weight[0]] = frequence
    return return_dic

# 保留两位小数
def result(num):
    num_str = str(num).split('.')
    num = float(num_str[0] + '.' + num_str[1][0:2])
    return num

def main():
    # set是把重复的去掉
    all_key = set()
    # 打开文件
    f = open(
        sys.argv[1],
        'r',
        encoding='utf-8')
    lines = f.readlines()
    # join()是一个字符串方法，它返回被子字符串连接的字符串。
    lines = "".join(lines)
    # print(lines)
    # 得到关键字典
    article1_dic = analyse_word(lines)
    print('第一篇文章的关键字和词频', article1_dic)
    # 如果kv在字典中则添加到all_key中
    # for循环中k和v都是变量，分别遍历了key，value
    for k, v in article1_dic.items():
        all_key.add(k)
    g = open(
        sys.argv[2],
        'r',
        encoding='utf-8')
    lines1 = g.readlines()
    lines1 = "".join(lines1)
    # print(lines1)
    article2_dic = analyse_word(lines1)
    print('第二篇文章的关键字和词频', article2_dic)
    for k, v in article2_dic.items():
        all_key.add(k)
        # 进行计算
    cos = resemble_cal(all_key, article1_dic, article2_dic)
    cosfinal = result(cos)
    # output = input('请输入答案文件的地址：')
    with open(sys.argv[3], 'w') as file:
        file.write(str(cosfinal))
    file.close()
    print('两篇文章的相似度:', cosfinal)
    
    


if __name__ == "__main__":
    main()