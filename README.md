DataDealer
========
	合并每日answers的json
	提取id、url_token、name、headline、gender
	取url_token并集

## JSONRunner.py
	*提取json文件的author信息
	*输出到自定义目录

## Combiner.py
	*合并JSONRunner.py提取的authors
	*并输出到./AuthorsofAnswers.json

## 数据文件说明
	*[此文件](306537777_authorsCombination.json)
		*问题**如果高中生能证明哥德巴赫猜想，会被清华北大数学系保送吗？**的所有去重答主基本信息集
		*数据结构
			*id
			*url_token
			*name
			*headline
			*gender
			*badge
	*其他数据文件，没有特别作用，仅为程序运行输出