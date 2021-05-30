
/*run using superuser*/
CREATE DATABASE projeto;
CREATE USER bd_user WITH ENCRYPTED PASSWORD 'bd2021';
GRANT ALL PRIVILEGES ON DATABASE projeto TO bd_user;

/*run api.py logging with bd_user*/
/*
username: bd_user
password: bd2021
*/
