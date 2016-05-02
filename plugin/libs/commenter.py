import vim

# Symbols:
Python_Symbols = ( "#", "-", "#")
JavaScript_Symbols = ( "//", "-", "//")

# Gets the Symbols that fit the current filetype.
#---------------------------------------------------
def GetSymbols(filetype):
    if filetype == "python":
        return Python_Symbols
    elif filetype == "javascript":
        return JavaScript_Symbols

# Creates a growing Comment for the current filetype.
#-------------------------------------------------------
def CreateGrowingComment():
    filetype=vim.eval("&filetype")
    symbols = GetSymbols(filetype)

    cb = vim.current.buffer
    cw = vim.current.window
    cr = cw.cursor[0]

    CreateLineBelow(symbols, cr, cb)
    CreateCommentStart(symbols, cr, cb)

    cw.cursor = (cr+1, cw.cursor[1])
    vim.command("startinsert!")

    vim.command(":augroup vim-commenter")
    vim.command(":autocmd CursorMovedI * :python3 commenter.MakeLineGrowTowards(('"+str(symbols[0]) + "', '" + str(symbols[1]) + "', '"+str(symbols[2]) + "'), " + str(cr) +", ["+ str(cr+1) +"])")
    vim.command(":autocmd InsertLeave * :autocmd! vim-commenter")
    vim.command(":augroup END")
    return


# Create the head of the line at the cursor (e.g. // )
# Enter insert mode after doing so
def CreateCommentStart(symbols, cr, cb):
    cb.append(symbols[0] + " ", cr)

# Create the head of the line below the cursor with 3 fillersymbols (e.g. //---)
def CreateLineBelow(symbols, cr, cb):
    cb.append(symbols[0] + symbols[1] + symbols[1] + symbols[1],  cr) 


# TODO: Make this more flexible. Currently Hitting return breaks it.
#----------------------------------------------------------------------
# togrow is a tuple with zero-based indices which lines should grow. 0 is the current line. positive is down, negative is up
def MakeLineGrowTowards(symbols, cr, togrow):
    cb = vim.current.buffer # We can't pass this as an argument because we call this with an autocommand through vim
    for line in togrow:
        cb[line] = cb[line][0:len(cb[cr])+3]
        while len(cb[cr])+3 > len(cb[line]):
            cb[line] += symbols[1]

