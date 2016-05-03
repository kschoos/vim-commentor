import commenter
import vim

# Creates a growing Comment for the current filetype.
#-------------------------------------------------------
def CreateGrowingComment():
    filetype=vim.eval("&filetype")
    symbols = commenter.GetSymbols(filetype)

    cb = vim.current.buffer
    cw = vim.current.window
    cr = 0 if cw.cursor[0] == 1 else cw.cursor[0] 
    

    commenter.CreateLineBelow(symbols, cr, cb)
    commenter.CreateCommentStart(symbols, cr, cb, cw)
    cw.cursor = (cr+1, cw.cursor[1])

    vim.command("startinsert!")

    vim.command(":augroup vim-commenter")
    vim.command(":autocmd CursorMovedI * :python3 growing_comment.MakeLineGrowTowards(('"+str(symbols[0]) + "', '" + str(symbols[1]) + "', '"+str(symbols[2]) + "'), ["+ str(1) +"])")
    vim.command(":autocmd InsertLeave * :autocmd! vim-commenter")
    vim.command(":augroup END")
    return

# togrow is a tuple with zero-based indices which lines should grow. 0 is the current line. positive is down, negative is up
def MakeLineGrowTowards(symbols, togrow):
    cb = vim.current.buffer # We can't pass this as an argument because we call this with an autocommand through vim
    cr = vim.current.window.cursor[0] - 1 
    if len(cb[cr]) < 2:
        cb[cr] = symbols[0] + " "
        vim.current.window.cursor = (cr+1, 2)

    for line in togrow:
        cb[cr + line] = cb[cr + line][0:len(cb[cr])+3]
        while len(cb[cr])+3 > len(cb[cr + line]):
            cb[cr + line] += symbols[1]
