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
