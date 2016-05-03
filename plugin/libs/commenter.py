#Symbols
Python_Symbols = ( "#", "-", "#")
JavaScript_Symbols = ( "//", "-", "//")

# Gets the Symbols that fit the current filetype.
#---------------------------------------------------
def GetSymbols(filetype):
    if filetype == "python":
        return Python_Symbols
    elif filetype == "javascript":
        return JavaScript_Symbols

# Create the head of the line at the cursor (e.g. // )
# Enter insert mode after doing so
def CreateCommentStart(symbols, cr, cb, cw):
    cb.append(symbols[0] + " ", cr)

def CommentCurrentLine(symbols, cr, cb):
    if cb[cr - 1][0:len(symbols[0])] == symbols[0]:
       return 
    cb[cr - 1] = symbols[0] + " " + cb[cr - 1]

# Create the head of the line below the cursor with 3 fillersymbols (e.g. //---)
def CreateLineBelow(symbols, cr, cb):
    cb.append(symbols[0] + symbols[1] + symbols[1] + symbols[1],  cr) 

def CreateTerminatedLine(symbols, length):
    string = symbols[0]
    for i in range(length):
        string += symbols[1]
    string += symbols[0]
    return string

def CreateTerminatedBlock(symbols, cr, cb):
    cb.append(symbols[0] + "   " + symbols[0],  cr) 

def CreateBoxAround(symbols, cr, cb, cw):
    cb.append(CreateTerminatedLine(symbols, 3), cr)
    CreateTerminatedBlock(symbols, cr, cb)
    cb.append(CreateTerminatedLine(symbols, 3), cr)

    cw.cursor = (cr + 2, len(symbols[0]) + 1)
