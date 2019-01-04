import Tools as tools
import random


def deal(JSON,per):
    res = []

    length = len(JSON)
    # 均分四份
    perLen = int(length/4)

    i = 0
    for j in range(0,4):
        for k in range(0,int(per[j])):
            # 区间内随机抽样
            num = int(random.random()*perLen)
            res.append(JSON[i + num])
        i += perLen
    return res

def main():
    
    # 均分四份
    # 每份提取比例
    # 1.2 1.3 2.5 2.6 sigema=7.6
    # 0.16 0.18 0.32 0.34
    # 8 9 16 17

    # 需要提取的总数
    total = 20
    print("输入抽样数：")
    total = int(input())
    # 玄学因子，有需要请自行炼丹
    # 设置区间内抽样数
    per = [total*0.16,total*0.20,total*0.30,total*0.34]
    for i in range(0,len(per)):
        # 为四舍五入做预处理，以确保输出的结果数为total
        per[i] += 0.5

    # 读取json文件
    link = ".\\answersCombine"
    targetLink = ".\\answersCombine"
    encoding = "utf-8"

    files = [
        "306537777_20181230_001",
        "306537777_20181230_002",
        "306537777_20181231_001",
        "306537777_20181231_002",
        "306537777_20190101_001",
        "306537777_20190101_002",
        "306537777_20190101_003",
        "307595822_20190102_001",
    ]
    for filename in files:
        print("正在处理：" + filename)
        JSON = tools.readFile_JSON(link,filename,encoding)
        res = deal(JSON,per)
        targetFilename = "samples_Num_" + str(total) + "_" + filename
        tools.writeJSONList(res,targetLink,targetFilename,encoding)
        print("完成处理，输出到：" + targetFilename)

if __name__ == "__main__":
    main()