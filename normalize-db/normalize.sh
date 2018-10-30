#! /bin/sh

## need to be sure we import after MariaDB is UP !!!
sleep 10

echo "..............................................................."
echo "Going to IMPORT titanic.csv file into MariaDB database ........"
echo "..............................................................."

## create table from csv 
csvsql --dialect mysql --snifflimit 100000 titanic.csv > titanic.sql

## create table in the mysql
mysql -uroot -ppassword -h mariadb-service -P 3306 titanic <titanic.sql

## import first from csv
mysqlimport --ignore-lines=1 --fields-terminated-by=, --local -uroot -ppassword -h mariadb-service -P 3306 titanic titanic.csv

## add id column with int auto_increment on
mysql -uroot -ppassword -h mariadb-service -P 3306 -e "alter table titanic.titanic add column Id int auto_increment primary key first";

echo "..............................................................."
echo "..............................................................."
echo "..............................................................."
echo "..........Titanic DB IMPORTED from csv file................... "
echo "..............................................................."
echo "..............................................................."
echo "..............................................................."

## lets see what was imported, and if titanic.titanic really exists ???
mysql -uroot -ppassword -h mariadb-service -P 3306 -e "desc titanic.titanic;"

echo "..............................................................."
echo "..............................................................."
echo "..............................................................."
