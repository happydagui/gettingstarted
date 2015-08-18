mkdir -p ~/.vim/autoload ~/.vim/bundle
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
cd ~/.vim/bundle
git clone https://github.com/scrooloose/nerdtree.git
sudo pip install jedi
git clone https://github.com/davidhalter/jedi-vim.git
git clone https://github.com/terryma/vim-multiple-cursors.git
