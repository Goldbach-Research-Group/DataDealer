
import Tools as tools

def featuresToAuthor(author):
	author = author["author"]
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

	# author = json.loads(author)

	features["id"] = author["id"]
	features["url_token"] = author["url_token"]
	features["name"] = author["name"]
	features["gender"] = author["gender"]
	features["headline"] = author["headline"]
	features["badge"] = author["badge"]

	return features

def featuresAllSave(data):
	return data

def main():

	print("encoding:")
	# encoding = utf-8
	encoding = "UTF-8"

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
	jsonList = tools.foreachFolder(link,encoding,featuresToAuthor)
	print("遍历完成：" + link)


	jsonList = tools.linkByAuthor_url_token(jsonList)

	print("开始写入：" + targetFilename + ".json")
	tools.writeJSONList(jsonList,targetLink,targetFilename,encoding)
	print("写入完成：" + targetFilename +".json")


if __name__ == '__main__':
	main()