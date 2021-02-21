# 1.Установите СУБД MySQL. Создайте в домашней директории файл .my.cnf, задав в нем логин и пароль, который указывался
# при установке.
#
# Среда установлена.
# Файл создан и перемещен в домушнюю директорию C:\Program Files\MySQL\MySQL Server 8.0
# my.cnf
# [client]
#
# user=root
# password=12345

# 2. Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и
# строкового name.
#
# mysql> CREATE DATABASE example;
# mysql> USE example
# mysql>  CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);

#  3. Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample.
# mysql> CREATE DATABASE sample;
# C:\Program Files\MySQL\MySQL Server 8.0\bin>mysqldump -uroot -p example > C:/sample.sql
# Enter password: *****
# C:\Program Files\MySQL\MySQL Server 8.0\bin>mysqldump -uroot -p sample < C:/sample.sql
# Enter password: *****
#
# 4. (по желанию) Ознакомьтесь более подробно с документацией утилиты mysqldump.
# Создайте дамп единственной таблицы help_keyword базы данных mysql. Причем добейтесь того,
# чтобы дамп содержал только первые 100 строк таблицы.
# C:\Program Files\MySQL\MySQL Server 8.0\bin>mysqldump -uroot -p mysql help_keyword --where="1 limit 100" > new_keys.sql
# Enter password: *****
