# import requests
# from selenium import webdriver
# verify_url = 'https://www.douban.com/'
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
#
# }
# response=requests.get(verify_url,headers=headers)
# print(response.status_code)


s=['海洋之星', '鼠之夜', '海鸥墓园', '扑火', '我请求有罪', '扫鼠岭', '讲了100万次的故事·挪威（全两册）',\
 '矮人星上的矮人', '纳闷集', '愤怒', '怜悯恶魔', '万重山', '纵横交错的世界', '万火归一', '熔炉', '比利\
时的哀愁', '长头发的猫咪男孩', '织巢', '祈念守护人']
pk=['海洋之星', '鼠之夜', '海鸥墓园', '扑火', '我请求有罪', '扫鼠岭', '讲了100万次的故事·挪威（全两册）',\
 '矮人星上的矮人', '纳闷集', '愤怒', '怜悯恶魔', '万重山', '纵横交错的世界', '万火归一', '熔炉', '比利\
时的哀愁', '长头发的猫咪男孩', '织巢', '祈念守护人']
lj=['海洋之星', '鼠之夜', '海鸥墓园', '扑火', '我请求有罪', '扫鼠岭', '讲了100万次的故事·挪威（全两册）',\
 '矮人星上的矮人', '纳闷集', '愤怒', '怜悯恶魔', '万重山', '纵横交错的世界', '万火归一', '熔炉', '比利\
时的哀愁', '长头发的猫咪男孩', '织巢', '祈念守护人']
k=['\n                        ［爱尔兰］约瑟夫•奥康纳 / 北京联合出版公司 / 2020-6\n                    ',
 '\n                        [日] 连城三纪彦 / 新星出版社 / 2020-6\n                    ', '\n\
              郑然 / 后浪丨海峡文艺出版社 / 2020-7\n                    ', '\n\
张天翼 / 中信出版集团 / 2020-6\n                    ', '\n                        [日] 早见和真 / 上海\
文艺出版社 / 2020-5\n                    ', '\n                        呼延云 / 新星出版社 / 2020-6\n\
                  ', '\n                        [挪威] 彼·阿斯别约恩生 约·姆厄 编 / 北京联合出版公司\
/ 2020-5-20\n                    ', '\n                        [意] 翁贝托·埃科 / 欧金尼奥·卡尔米 绘\
/ 上海译文出版社 / 2020-5-31\n                    ', '\n                        匡扶 / 雅众文化 | 湖南\
文艺出版社 / 2020-6\n                    ', '\n                        [美] 菲利普·罗斯 / 上海译文出版\
社 / 2020-6\n                    ', '\n                        [日] 西泽保彦 / 新星出版社 / 2020-6\n\
                 ', '\n                        甫跃辉 / 上海人民出版社 / 2020-6\n                    ',\
 '\n                        [英] 阿莉·史密斯 / 浙江文艺出版社 / 2020-5\n                    ', '\n\
                    [阿根廷] 胡里奥·科塔萨尔 / 南海出版公司 / 2020-5-1\n                    ', '\n\
                    [韩]孔枝泳 / 北京联合出版公司 / 2020-6\n                    ', '\n\
       【比利时】雨果·克劳斯 / 译林出版社 / 2020-6\n                    ', '\n\
[以色列]埃特加·凯雷特 / [以色列]阿维尔·巴希尔 / 湖南美术出版社 / 2020-5\n                    ', '\n\
                      西西 / 四川文艺出版社 / 2020-5\n                    ', '\n\
 [日] 东野圭吾 / 南海出版公司 / 2020-6\n                    ']
for i,j,p,l in zip(s,k,pk,lj):
    print(i,p,l,j.strip())