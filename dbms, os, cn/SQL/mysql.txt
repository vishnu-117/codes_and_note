1)sudo mysql -u root -p
=> To login shell
2)CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
=>To create user
3)GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
=>To give access to user
4)select user from mysql.user;
=>To get user list


mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_new_password';
mysql> FLUSH PRIVILEGES;
mysql> exit;

then to confirm

mysql -u root -p 
Enter password: ********

Success!!!




LINKS:
https://hevodata.com/learn/installing-mysql-on-ubuntu-20-04/






sudo apt-get install python3.8-dev libmysqlclient-dev

