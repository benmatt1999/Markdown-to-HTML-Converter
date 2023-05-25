def calcHeader(line):
    numPounds = 1
    while (line[numPounds] == '#'):
        numPounds += 1
    return numPounds

def isHeader(line, numPounds):
    spaceIndex = line.find(" ")
    trimmedLine = line[spaceIndex:].strip()
    numPoundsStr=str(numPounds)
    return '<h'+numPoundsStr+'>'+trimmedLine+'</h'+numPoundsStr+'>'+'\n'

def isParagraph(line, isNewPar):
    if isNewPar:
        line = '<p>'+line+'</p>\n'
    else:
        line += '</p>\n'
    return line

def hasLink(line):
    bracketIndex1 = line.find('[')
    bracketIndex2 = line.find(']')
    parIndex1 = line.find('(')
    parIndex2 = line.find(')')
    newLine = line[:bracketIndex1] + '<a href="' + line[parIndex1+1:parIndex2]+'">'\
        + line[bracketIndex1+1:bracketIndex2]+'</a>' + line[parIndex2+1:]
    return newLine

def convertToHTML(text):
    textArr = text.splitlines()
    newHTMLText = ''
    for lineNum, line in enumerate(textArr):
        if ('[' in line and ']' in line and '(' in line and ')' in line):
            line = hasLink(line)
        if (len(line) <= 0):
            continue
        elif (line[0] == '#'):
            headerSize = calcHeader(line)
            newHTMLText += isHeader(line, headerSize)
        elif (line=='...'):
            newHTMLText += '...\n'
        else:
            HTMLTextLen = len(newHTMLText)
            isNewPar = True
            if (HTMLTextLen > 4 and len(textArr[lineNum-1]) > 0 and newHTMLText[HTMLTextLen-5:HTMLTextLen-1] == '</p>'):
                newHTMLText = newHTMLText[:HTMLTextLen-5] + newHTMLText[HTMLTextLen-1:]
                isNewPar = False
            newHTMLText += isParagraph(line, isNewPar)
    return newHTMLText

            