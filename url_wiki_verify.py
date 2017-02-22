import urllib2
import json

file = open('/home/ubuntu/docs/product_wiki.txt','r')
output_file = open('/home/ubuntu/docs/url_exist.csv','w')
out1 = open('/home/ubuntu/docs/url_not_exist.csv','w')
count = 0

for line in file:
	count = count + 1
	keyword = line.strip()
	req = urllib2.urlopen('http://en.wikipedia.org/w/api.php?action=query&titles=%s&prop=info&inprop=url&format=json'% keyword)
	data = json.load(req)

	x = data['query']['pages'].keys()
	x=x[0]
	page_id=int(x)

	if(page_id!=-1):
		req1 = urllib2.urlopen('https://en.wikipedia.org/w/api.php?action=query&titles=%s&prop=info&inprop=url&format=json&redirects'% keyword)
		data1 = json.load(req1)
		try:
			s = data1["query"]["redirects"][0]["to"]
			s = str(s)
			l = s.split()
			m = "_".join(n for n in l)
			if keyword.lower() != m.lower():
				output_file.write(keyword+";"+ m + "  not same "+"\n")
			else:
				output_file.write(keyword+";"+ m + "SAME "+"\n")
		except KeyError:
			try:
				y = data["query"]["pages"].keys()
				y = y[0]
				y = str(y)
				s1 = data1["query"]["pages"][y]["fullurl"]
				s1 = str(s1)
				name = s1.split('/')
				if keyword.lower() != name[4].lower():
					output_file.write(keyword+";"+ name[4] + "  not same \n")
				else:
					output_file.write(keyword+";"+ name[4] + "  same \n")
			except KeyError:
				print keyword + "not check"
				out1.write(keyword + "  :" + count +" not checked \n")
	else:
		out1.write(keyword+"  :" + str(count) + "\n")

file.close()
output_file.close()
out1.close()
