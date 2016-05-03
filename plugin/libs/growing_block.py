import vim
import commenter

def CreateGrowingCommentBlock():
    filetype = vim.eval("&filetype")
    symbols  = commenter.GetSymbols(filetype)

    cb = vim.current.buffer
    cw = vim.current.window
    cr =  0 if cw.cursor[0] == 1 else cw.cursor[0] - 1

    commenter.CreateBoxAround(symbols, cr, cb, cw)

    vim.command(":augroup vim-commenter")
    vim.command(":autocmd CursorMovedI * py3 growing_block.GrowBlock(('"+str(symbols[0]) + "', '" + str(symbols[1]) + "', '"+str(symbols[2]) + "'), " + str(cr) +")")

    vim.command(":autocmd InsertLeave * :autocmd! vim-commenter")
    vim.command(":augroup END")

    vim.command("startinsert")

def GrowBlock(symbols, sr):
    cb = vim.current.buffer
    cw = vim.current.window
    cr = cw.cursor[0]

    currentmax = 0
    for i in range(1, cr-sr):
        currentmax = max(len(cb[sr + i]), currentmax)

    cb[sr] = commenter.CreateTerminatedLine(symbols, currentmax - 2 )
    cb[cr] = commenter.CreateTerminatedLine(symbols, currentmax - 2 )
    return
