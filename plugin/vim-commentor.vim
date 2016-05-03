" Commenting without a hassle.
" Maintainer:	Skusku <skusku@skusku.org>
" Last Change:  2016-02-05
" Version: 0.0.1 
" Repository: https://github.com/skusku/vim-commenter
" License: MIT


" Initialization
"""""""""""""""""""""""""""""""""""""""
if(exists('g:CommenterLoaded') || &cp)
  finish
end

python3 << pythonend
import sys, vim
sys.path.append(vim.eval("expand('<sfile>:p:h')") + '/libs/')
import growing_comment, growing_block
pythonend

let g:CommenterLoaded = 1

function! g:CreateGrowingComment()
  python3 growing_comment.CreateGrowingComment()
endfunction

function! g:CreateGrowingCommentBlock()
  python3 growing_block.CreateGrowingCommentBlock()
endfunction

" Keybindings
"""""""""""""""""""""""""""""""""""""""
nnoremap <Leader>c :call g:CreateGrowingComment()<CR>
nnoremap <Leader>q :call g:CreateGrowingCommentBlock()<CR>
