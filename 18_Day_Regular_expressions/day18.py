import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you  do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph = paragraph.lower()
plist = re.split(r'[. ]', paragraph)
newPlist = []
for i in plist:
    if i.strip(): 
        newPlist.append(i) 
print(newPlist)
plistSet = set(newPlist)
print(plistSet)
print(len(plistSet))
a = 0
outputFreq = 0
outputWord = ''
for w in plistSet:
    match = re.findall(w, paragraph, re.I)
    count = len(match)
    if count > a:
        outputFreq = count
        outputWord = w

print(outputWord,':', outputFreq)
#parmu na thik korte icche kortese na 
