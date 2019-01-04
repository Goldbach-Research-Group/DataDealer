DataDealer
========
	合并每日answers的json  
	提取id、url_token、name、headline、gender  
	取url_token并集  

## JSONRunner.py  
* 提取json文件的author信息  
* 输出到自定义目录  
* + 可通过传入不同的json处理函数，实现特征提取或单纯的json文件合并
* + 函数 [featuresToAuthor] 为提取author的指定特征
* + 函数 [featuresAllSave] 为单纯json文件合并

## Combiner.py  
* 合并JSONRunner.py提取的authors  
* 并输出到./AuthorsofAnswers.json  

## Sample.py
* 对[答案]集进行抽样
* 具体抽样方法：
* + 将[答案]均分为四份
* + 根据总抽样数，每份按比例 0.16 0.18 0.32 0.34 抽取
* + 输出保存到[answersCombine](./answersCombine)

## Tools.py
* 一些通用的操作抽象实现

## 数据文件说明  
### authorsCombination
* 问题 **如果高中生能证明哥德巴赫猜想，会被清华北大数学系保送吗？** 的所有去重答主基本信息集  
* 数据结构  
	id  
	url_token  
	name  
	headline  
	gender  
	badge  
* 其他数据文件，没有特别作用，仅为程序运行输出  

### answersCombine
* 存储了当日单次爬虫爬取的所有答案json，及该json的抽样
* [答案]文件名命名规范: [$questionId]\_[$date]\_[order]
+ + $questionID: 为爬取的知乎问题的id号，由知乎编辑生成
+ + $data: 为爬虫爬取时的日期，精确到日
+ + $order: 为[data数据集](../data)中所爬取的数据每日的流水号
* [答案抽样]文件名命名规范: samples\_Num\_[$num]\_[$questionId]\_[$date]\_[order]
+ + $num: 为该文件的抽样数
