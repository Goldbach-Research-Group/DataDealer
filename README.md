DataDealer
========
	合并每日answers的json  
	提取id、url_token、name、headline、gender  
	取url_token并集  

## JSONRunner.py  
* 提取json文件的author信息  
* 输出到自定义目录  

## Combiner.py  
* 合并JSONRunner.py提取的authors  
* 并输出到./AuthorsofAnswers.json  

## 数据文件说明  
* [此文件](./output/306537777_authorsCombination.json)  
* 问题 **如果高中生能证明哥德巴赫猜想，会被清华北大数学系保送吗？** 的所有去重答主基本信息集  
* 数据结构  
	id  
	url_token  
	name  
	headline  
	gender  
	badge  
* 其他数据文件，没有特别作用，仅为程序运行输出  

## answersCombine
* 存储了当日单次爬虫爬取的所有答案json，及该json的抽样
* [答案]文件名命名规范: [$questionId]\_[$date]\_[order]
+ + $questionID: 为爬取的知乎问题的id号，由知乎编辑生成
+ + $data: 为爬虫爬取时的日期，精确到日
+ + $order: 为[data数据集](..\data)中所爬取的数据每日的流水号
* [答案抽样]文件名命名规范: samples\_Num\_[$num]\_[$questionId]\_[$date]\_[order]
+ + $num: 为该文件的抽样数
