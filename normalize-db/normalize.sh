#! /bin/sh

if [ $# -lt 1 ]; then
    echo
    echo "Usage: $0 <db_hostname> <db_port> " >&2
    echo
    echo "Example:" >&2
    echo "   $0  mariadb-service 31306" >&2
    echo
    exit 2
fi

## use vars
DB_NAME=$1
PORT=$2

## need to be sure we import after MariaDB is UP !!!
sleep 10

echo "..............................................................."
echo "----------> DB hostname= $DB_NAME"
echo "----------> DB     port= $PORT"
# sleep 2
# netcat -z -v 0.0.0.0 $PORT
# netcat -z -v $DB_NAME $PORT
# netcat -z -v localhost $PORT
echo "..............................................................."
echo "..............................................................."
echo "..............................................................."
echo "Going to IMPORT titanic.csv file into MariaDB database ........"
echo "..............................................................."

## create table from csv 
csvsql --dialect mysql --snifflimit 100000 titanic.csv > titanic.sql

## create table in the mysql
mysql -uroot -ppassword -h $DB_NAME -P $PORT titanic <titanic.sql

## import first from csv
mysqlimport --ignore-lines=1 --fields-terminated-by=, --local -uroot -ppassword -h $DB_NAME -P $PORT titanic titanic.csv

## add id column with int auto_increment on
mysql -uroot -ppassword -h $DB_NAME -P $PORT -e "alter table titanic.titanic add column Id int auto_increment primary key first";

echo "..............................................................."
echo "..............................................................."
echo "..............................................................."
echo "..........Titanic DB IMPORTED from csv file................... "
echo "..............................................................."
echo "..............................................................."
echo "..............................................................."

## lets see what was imported, and if titanic.titanic really exists ???
mysql -uroot -ppassword -h $DB_NAME -P $PORT -e "desc titanic.titanic;"

echo "..............................................................."
echo "..............................................................."
echo "..............................................................."

exit 0
