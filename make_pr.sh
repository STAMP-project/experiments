#!/bin/sh
################################################################################

args="$*"

CurrentDir=`pwd`

fileName="README.md"
templateName="README.template"

cp $templateName $fileName
Date=`date`
echo $Date >> $fileName

git checkout branchForTest
git commit -a -m "$Date"
git push

git checkout master

./make_pr.py
