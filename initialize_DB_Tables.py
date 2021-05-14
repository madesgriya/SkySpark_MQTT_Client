import sqlite3

# SQLite DB Name
DB_Name =  "IoT.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists KFC_Water_Data ;
create table KFC_Water_Data (
  id integer primary key autoincrement,
  nodeName text,
  Report_Time text,
  Value text
);

drop table if exists MandaiMart_Water_Data ;
create table MandaiMart_Water_Data (
  id integer primary key autoincrement,
  nodeName text,
  Report_Time text,
  Value text
);

drop table if exists BenNJerry_Water_Data ;
create table BenNJerry_Water_Data (
  id integer primary key autoincrement,
  nodeName text,
  Report_Time text,
  Value text
);
"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()
