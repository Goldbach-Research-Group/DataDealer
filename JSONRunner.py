import json
import os

def featuresToAuthor(author):
	# author JSON格式
	# 提取id、url_token、name、headline、gender、badge
	features = {
		"id":{},
		"url_token":{},
		"name":{},
		"gender":{},
		"headline":{},
		"badge":{},
	}

	author = json.loads(author)

	features["id"] = author["id"]
	features["url_token"] = author["url_token"]
	features["name"] = author["name"]
	features["gender"] = author["gender"]
	features["headline"] = author["headline"]
	features["badge"] = author["badge"]

	return features

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
	data = JSON["data"]

	authors = []
	for i in range(0,len(data)):
		singleAuthor = data[i]["author"]
		# print(singleAuthor)
		singleAuthor = featuresToAuthor(json.dumps(singleAuthor))
		authors.append(singleAuthor)
	return authors

def foreachFolder(link,encoding):
	# 遍历某一文件夹的子文件
	# dict
	filesName = getFilesName(link)
	jsonList = []
	for i in range(0,len(filesName)):
		temp = readFile_JSON(link,filesName[i],encoding)
		for k in range(0,len(temp)):
			jsonList.append(temp[k])
	return jsonList

def getFilesName(link):
	filesName = os.listdir(link)
	nameList = []
	for i in range(0,len(filesName)):
		# 文件夹过滤
		if (os.path.isfile(link+"\\"+filesName[i])):
			temp = filesName[i].split(".")
			# 只获取[*.json]的文件名,过滤器
			if (len(temp) == 2 and temp[1] == "json"):
				nameList.append(temp[0])
	return nameList

def writeJSONList(jsonList,targetLink,targetFilename,encoding):
	# 将author信息写入文件
	src = targetLink + "\\" + targetFilename + ".json"
	# print(src)
	file = open(src,"w",encoding=encoding)
	file.write(json.dumps(jsonList))
	file.close()

def linkByAuthor_url_token(jsonList):
	authors = {}
	for i in range(0,len(jsonList)):
		# 没有剔除原有id的item，因为，这样可以偷懒，，
		if jsonList[i]["url_token"] != "":
			authors[jsonList[i]["url_token"]] = jsonList[i]
	return authors

def main():
	print("encoding:")
	# encoding = utf-8
	encoding = input()

	print("link:")
	# link = "D:\GoldbachResearchGroup\data-master\\12.31\answers"
	link = input()

	print("targetLink:")
	# targetLink = "D:\GoldbachResearchGroup\data-master\\12.31"
	targetLink = input()

	print("targetFilename:")
	# targetFilename = "authorsofAnswers_12_31_18_23"
	targetFilename = input()

	print("开始遍历：" + link)
	jsonList = foreachFolder(link,encoding)
	print("遍历完成：" + link)


	jsonList = linkByAuthor_url_token(jsonList)

	print("开始写入：" + targetFilename + ".json")
	writeJSONList(jsonList,targetLink,targetFilename,encoding)
	print("写入完成：" + targetFilename +".json")


if __name__ == '__main__':
	main()