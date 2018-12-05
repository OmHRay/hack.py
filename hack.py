import urllib

testfile = urllib.URLopener()
for x in range(29):
	fileName = "Section" + format(x + 1, "04") + ".xhtml"
	print fileName
	testfile.retrieve("http://yoganiketan.net/books/d543e38c86f2c20c505465897dce88b8/OEBPS/Text/" + fileName, fileName)
