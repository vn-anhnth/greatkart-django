- init git
  - Create repository on git
  - git init
  - Add .gitignore, README.md in your project
  - (Enter https://gitignore.io/ to get django git ignore)
  - git add -A
  - git config --global user.name "Anh Nguyen"
  - git config --global user.email anhlone3@gmail.com
  - git commit -m "first commit"
  - git remote add origin https://github.com/vn-anhnth/greatkart-django.git
  - git branch -M main
  - git push -u origin main

  - git remote -v
  - git remote remove origin

  - connect with ssh key
    - ssh-keygen
    - /home/anhlone3/.ssh/id_rsa.pub
    - git remote add origin git@github.com:vn-anhnth/greatkart-django.git
