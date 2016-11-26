cd ~/GitHub

" Auto reload .vimrc
autocmd! bufwritepost .vimrc source %

set nocompatible               " required
filetype on 		       " required

"set the runtime path to include Vundle and initialize
call plug#begin('~/.vim/plugged')

set splitbelow
set splitright

"split navigations
nnoremap <C-J> <C-W><C-J>

nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

nnoremap tt <C-W><C-V>

" New tab split
nnoremap <C-N> :vne<CR>

" Tab navigations
nnoremap th :bp<CR>
nnoremap tl :bn<CR>

" Autosave
noremap <C-Z> :update<CR>
vnoremap <C-Z> <C-C>:update<CR>
inoremap <C-Z> <C-O>:update<CR>

" Tab closing
Plug 'moll/vim-bbye'

" Remap \wq and \q for only closing buffer
nnoremap twq :w<bar>Bdelete<CR>
nnoremap tq :Bdelete<CR>

" Enable folding
set foldlevel=50

" Enable folding with the spacebar
nnoremap <space> za

Plug 'tmhedberg/SimpylFold'
let g:SimpylFold_docstring_preview=1

set encoding=utf-8
	

" Install YCM for autocomplete
Plug 'Valloric/YouCompleteMe'
let g:ycm_collect_identifiers_from_tags_files = 1 " Let YCM read tags from Ctags file
let g:ycm_use_ultisnips_completer = 1 " Default 1, just ensure
let g:ycm_seed_identifiers_with_syntax = 1 " Completion for programming language's keyword
let g:ycm_complete_in_comments = 1 " Completion in comments
let g:ycm_complete_in_strings = 1 " Completion in string
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" Install syntax checker for python, uses recommended syntax for python2
" Plug 'scrooloose/syntastic'
let g:syntastic_python_python_exec='/usr/bin/python2'
let g:syntastic_python_flake8_exe='python -m flake8'
let g:syntastic_check_on_open=1

" Plug 'nvie/vim-flake8'
let python_highlight_all=1

" Install colors for vim
Plug 'altercation/vim-colors-solarized'

" Add nerdtree to navigate files
Plug 'scrooloose/nerdtree'
Plug 'jistr/vim-nerdtree-tabs'
" Ignore .pyc files
let NERDTreeIgnore = ['\.pyc$']

" Shows files' git status in nerdtree
Plug 'Xuyuanp/nerdtree-git-plugin'
autocmd vimenter * NERDTree
nmap <silent> <C-D> :NERDTreeToggle<CR>

" For searching current file tree
Plug 'kien/ctrlp.vim'

" Check for diffs in current file
Plug 'airblade/vim-gitgutter'

" Powerline for VIM
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" air-line 

let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'
let g:airline_powerline_fonts = 1

if !exists('g:airline_symbols')
	    let g:airline_symbols = {}
endif

" unicode symbols
let g:airline_left_sep = '»'
let g:airline_left_sep = '▶'
let g:airline_right_sep = '«'
let g:airline_right_sep = '◀'
let g:airline_symbols.linenr = '␊'
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = 'ρ'
let g:airline_symbols.paste = 'Þ'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.whitespace = 'Ξ'

" airline symbols
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.readonly = ''
let g:airline_symbols.linenr = ''

set nu

Plug 'tpope/vim-fugitive'

Plug 'tpope/vim-surround'
let b:surround_{char2nr("v")} = "{{ \r }}"
let b:surround_{char2nr("{")} = "{{ \r }}"
let b:surround_{char2nr("%")} = "{% \r %}"
let b:surround_{char2nr("b")} = "{% block \1block name: \1 %}\r{% endblock \1\1 %}"
let b:surround_{char2nr("i")} = "{% if \1condition: \1 %}\r{% endif %}"
let b:surround_{char2nr("w")} = "{% with \1with: \1 %}\r{% endwith %}"
let b:surround_{char2nr("f")} = "{% for \1for loop: \1 %}\r{% endfor %}"
let b:surround_{char2nr("c")} = "{% comment %}\r{% endcomment %}"

Plug 'SirVer/ultisnips'
let g:UltiSnipsExpandTrigger       = "<c-b>"
let g:UltiSnipsJumpForwardTrigger  = "<c-b>"
let g:UltiSnipsJumpBackwardTrigger = "<c-z>"
let g:UltiSnipsListSnippets        = "<c-e>" "List possible snippets based on current file

Plug 'honza/vim-snippets'

Plug 'bingaman/vim-sparkup'

Plug 'vim-scripts/taglist.vim'
nnoremap <silent> <c-t> :TlistToggle<CR>
let Tlist_Use_Right_Window = 1
let Tlist_WinWidth = 50

call plug#end()

set background=dark
syntax enable
colorscheme solarized


set modelines=0
set nomodeline 
