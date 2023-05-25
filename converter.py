# Calculates the header size. Essentially it takes in the number of #s 
# and converts it to a number to be placed in the html header tag
def calcHeader(line):
    numPounds = 1
    while (line[numPounds] == '#'):
        numPounds += 1
    return numPounds

def isHeader(line):
    # Finds the first space after the pound signs
    spaceIndex = line.find(" ")
    trimmedLine = line[spaceIndex:].strip()
    # Calls calcHeader function to find header size
    numPounds=str(calcHeader(line))
    return '<h'+numPounds+'>'+trimmedLine+'</h'+numPounds+'>'+'\n'

def isParagraph(line, isNewPar):
    # If the previous line was also a paragraph, the beginning paragraph tag is not needed
    if isNewPar:
        line = '<p>'+line+'</p>\n'
    else:
        line += '</p>\n'
    return line

def hasLink(line):
    # Grabs indices of brackets and parenthesis for string manipulation into HTML
    bracketIndex1 = line.find('[')
    bracketIndex2 = line.find(']')
    parIndex1 = line.find('(')
    parIndex2 = line.find(')')
    # Reorganizes the link into HTML format
    newLine = line[:bracketIndex1] + '<a href="' + line[parIndex1+1:parIndex2]+'">'\
        + line[bracketIndex1+1:bracketIndex2]+'</a>' + line[parIndex2+1:]
    return newLine

def convertToHTML(text):
    # Splits all of the lines into an array for iteration purposes
    textArr = text.splitlines()
    newHTMLText = ''
    for lineNum, line in enumerate(textArr):
        # This check is here to see if a line has a link. 
        # Since any tag can have a link, it is seperate from the other if statements.
        if ('[' in line and ']' in line and '(' in line and ')' in line):
            line = hasLink(line)

        # Checks if line is empty
        if (len(line) <= 0):
            continue
        # Checks if it is a header
        elif (line[0] == '#'):
            newHTMLText += isHeader(line)
        # Checks for ellipsis
        elif (line=='...'):
            newHTMLText += '...\n'
        # If all of the previous checks fail, it is assumed to be a paragraph
        else:
            HTMLTextLen = len(newHTMLText)
            isNewPar = True
            # The previous line needs to be checked to see if it is a continuation of a previous paragraph from the previous line
            if (HTMLTextLen > 4 and len(textArr[lineNum-1]) > 0 and newHTMLText[HTMLTextLen-5:HTMLTextLen-1] == '</p>'):
                # If there are back to back paragraphs, the closing paragraph tag </p> is removed
                newHTMLText = newHTMLText[:HTMLTextLen-5] + newHTMLText[HTMLTextLen-1:]
                isNewPar = False
            newHTMLText += isParagraph(line, isNewPar)
    return newHTMLText

            