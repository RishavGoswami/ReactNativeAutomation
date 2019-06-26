#!/usr/bin/env python

function react-native() {
    cd /Users/<Your Name>/Automate\ Git\ Repo/ # Exit from anywhere to where the files are located

    python react-native.py $1 # Run the python file
    cd /Users/<Your Name>/Desktop/Project/

    # Create a react js project 7 navi
    react-native init ${1}
    cd $1

    # Initialized & add the project to your git
    git init
    git remote add origin git@github.com:<Your Github Name>/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    # Open Vs Code
    code .

}