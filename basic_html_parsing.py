import urllib.request
targetURL = 'http://www.runescape.com'
with urllib.request.urlopen(targetURL) as response:
    html = response.read()
parsedFile = open("parsed_response.txt", "w+")
workingString = str(html)
workingString = workingString[2:len(workingString)]
for i in range(0, workingString.count('\\n') + 1):
    lineMark = workingString.find('\\n')
    thisLine = workingString[0:lineMark]
    thisLine = thisLine.replace('\\t', '    ')
    thisLine = thisLine.replace("\\'", "'")
    workingString = workingString[lineMark+2:len(workingString)]
    parsedFile.write(thisLine + '\n')
parsedFile.close()
