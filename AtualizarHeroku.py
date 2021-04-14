import os
os.chdir('..')
os.system('cls')

commit = input('Commit a ser enviada: ')

os.system('heroku git:remote -a zapper-bot')
os.system('git init')
os.system('git add .')
os.system('git commit -am ' + commit)
os.system('git push heroku master')
"""
git add .
git commit -am "Modificações no .rank e maior aleatoriedade na aposta"
git push
"""