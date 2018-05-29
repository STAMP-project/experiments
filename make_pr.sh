#!/bin/sh
################################################################################

args="$*"

CurrentDir=`pwd`

fileName="README.md"
templateName="README.template"

cp $templateName $fileName
Date=`date`
echo $Date >> $fileName

if git checkout branchForTest
then
   if git commit -a -m "$Date"
   then
      if git push
      then
         git checkout master
         ./make_pr.py
      fi
   fi
fi
