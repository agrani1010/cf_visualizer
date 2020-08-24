import requests

def search():#returns dictionary of verdicts and tags of the problems solved by user
	name = input("Enter user handle: ")
	response = requests.get("https://codeforces.com/api/user.status?handle={}&from=1&count=10000".format(name))
	r = response.json()
	search = r['result']
	verdict = {}
	tags = {}
	for i in search:
		if i['verdict'] in verdict:
			verdict[i['verdict']] += 1
		else:
			verdict[i['verdict']] = 1
		for j in i['problem']['tags']:
			if j in tags:
				tags[j] +=1
			else:
				tags[j] = 1
	return verdict, tags
if __name__ == "__main__":
	v,t = search()
	print(v)
	print(t)