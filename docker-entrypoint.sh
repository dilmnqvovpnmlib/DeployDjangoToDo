#!/bin/sh

echo Helloooooooooooooooooooooooooooooooooooooooooooooooooooooo

export connected="no"
while [ $connected = "no" ]
do
  mysql -h db -u root -proot -e 'show databases;'
  echo $?
  echo "do"
  if [ $? -eq 0 ] ; then
    export connected="yes"
  fi
  sleep 1
done

python todo/manage.py migrate

echo nnnnnnnnnnnn

python todo/manage.py collectstatic

echo mmmmmmmmmmmmmmmmm

supervisord
