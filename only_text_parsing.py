import urllib.request

# Grab HTML
targetURL = 'http://www.wikipedia.com'
with urllib.request.urlopen(targetURL) as response:
    html = response.read()

# Setup the big string
parsedFile = open("parsed_response.txt", "w+")
workingString = str(html)
workingString = workingString[2:len(workingString)]

# Parse, line-by-line
lines = workingString.split('\\n')

for i in lines:
    for tags in range(0, i.count('<')):
        inlineDiff = i.find(' ') - i.find('<')
        newlineDiff = i.find('>') - i.find('<')
        if inlineDiff < newlineDiff:
            tagType = i[i.find('<')+1 : i.find(' ')]
        else:
            tagType = i[i.find('<')+1 : i.find('>')-1]
        if tagType == "a" and i.find('/>') >= i.find('>'):
            i = i[0:i.find('<')] + "(link) " + i[i.find('>')+1:len(i)]
        elif tagType == "script" and newlineDiff < inlineDiff:
            i = i[0:i.find('<script>')] + i[i.find('</script>')+9:len(i)]
        else:
            i = i[0:i.find('<')] + i[i.find('>')+1:len(i)]
    
    if len(i) > 0:
        print(i)

parsedFile.close()
