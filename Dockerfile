FROM mysql/mysql-server:latest

ENV MYSQL_ROOT_PASSWORD root

CMD ["mysqld"]