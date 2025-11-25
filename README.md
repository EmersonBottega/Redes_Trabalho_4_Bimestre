# Redes_Trabalho_4-_Bimestre

Para executar a aplicação sem precisar de root:
```ruby
# Instalar rbenv localmente
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc

# Instalar ruby-build (para instalar versões Ruby)
git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build

# Instalar versão do ruby: 3.2.2
rbenv install 3.2.2
rbenv global 3.2.2

# Verificar versão
ruby -v
```
