set nocompatible               " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
call plug#begin('~/.vim/plugged')

set splitbelow
set splitright

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

"Fast run python
nnoremap <silent> <F2> :!clear;python %<CR>
nnoremap <silent> <F3> :!clear;python3 %<CR>

" Enable folding
set foldmethod=indent
set foldlevel=99

" Enable folding with the spacebar
nnoremap <space> za

Plug 'tmhedberg/SimpylFold'
let g:SimpylFold_docstring_preview=1

au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=79 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

Plug 'vim-scripts/indentpython.vim'

set encoding=utf-8

Plug 'Valloric/YouCompleteMe'
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

Plug 'scrooloose/syntastic'
Plug 'nvie/vim-flake8'
let python_highlight_all=1

Plug 'altercation/vim-colors-solarized'

Plug 'scrooloose/nerdtree'
Plug 'jistr/vim-nerdtree-tabs'

Plug 'kien/ctrlp.vim'


set nu

Plug 'tpope/vim-fugitive'
call plug#end()
filetype plugin indent on    " required

set background=dark
syntax enable
colorscheme solarized


