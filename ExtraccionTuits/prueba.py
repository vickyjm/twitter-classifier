import webbrowser

finput = open('dcabellor.dat','r')
inputLines = finput.read().splitlines()

url = "http://www.twitter.com/"
#webbrowser.open_new('http://www.twitter.com/'+inputLines[52])
for i in range(93,101):
	webbrowser.open_new_tab(url+inputLines[i])
