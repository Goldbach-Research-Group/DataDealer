import json
# 全局authors jsonList
authors = {}

def readFile_JSON(link,filename,encoding):
	# 假设内存足够大，不考虑内存泄漏
	# link 文件路径
	# filename 无后缀文件名
	# 直接抛出io异常，不作任何处理

	# 读取出异常，多半是路径格式不对，注意转义
	# 强制文件后缀过滤，注意文件保存格式，我有洁癖
	src = link + "\\" + filename + ".json"
	# print(src)
	file = open(src,"r",encoding=encoding)
	fileData = file.read()
	JSON = json.loads(fileData)

	# 迭代器
	for x in JSON:
		if x != "":
			authors[x] = JSON[x]
			# print(str(authors))
			# 断点设置
			# raise ValueError('assert')
			# 监测正常

def writeJSONList(jsonList,targetLink,targetFilename,encoding):
	# 重复代码标记，不能忍，但懒得抽象了，这次就忍自己一次 by tenma
	# 将author信息写入文件
	src = targetLink + "\\" + targetFilename + ".json"
	# print(src)
	file = open(src,"w",encoding=encoding)
	file.write(json.dumps(jsonList))
	file.close()

def main():
	# 天气好冷，没暖气，不想封装了，，
	encoding = "utf-8"
	filesList = [
		"authorsofAnswers_12_30_001",
		"authorsofAnswers_12_30_002",
		"authorsofAnswers_12_31_001",
		"authorsofAnswers_12_31_002",
		"authorsofAnswers_01_01_001",
		"authorsofAnswers_01_01_002",
		"authorsofAnswers_01_01_003",
	]
	
	link = ".\\"

	# 命名规范 QuestionId_authorsCombination
	targetFilename = "306537777_authorsCombination"
	for i in range(0,len(filesList)):
		# 读取json文件
		readFile_JSON(link,filesList[i],encoding)
		print("authors len:" + str(len(authors)))

	writeJSONList(authors,link,targetFilename,encoding)

	print("处理完成")

if __name__ == "__main__":
	main()