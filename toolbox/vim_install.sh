mkdir -p ~/.vim/autoload ~/.vim/bundle
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
cd ~/.vim/bundle
git clone https://github.com/scrooloose/nerdtree.git
sudo pip install jedi
git clone https://github.com/davidhalter/jedi-vim.git
#git clone https://github.com/rkulla/pydiction.git
# 按下 <C-n> 选中光标下的单词,继续按下 <C-n> 两次选中另外两个相同的单词,按下c进行修改,键入修改,按下 <Esc> 退出
git clone https://github.com/terryma/vim-multiple-cursors.git
git clone git://github.com/altercation/vim-colors-solarized.git
sudo apt-get install ctags
git clone https://github.com/vim-scripts/Tagbar.git
git clone https://github.com/vim-scripts/fugitive.vim
git clone https://github.com/ervandew/supertab.git
# html:5 <C-Y> ,
git clone https://github.com/mattn/emmet-vim.git
git clone https://github.com/plasticboy/vim-markdown.git
