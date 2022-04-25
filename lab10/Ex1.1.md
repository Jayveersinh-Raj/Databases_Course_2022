    CREATE TABLE accounts
       (
       id INT PRIMARY KEY     NOT NULL,
       name          CHAR(20)    NOT NULL,
       Credit        INT       NOT NULL,
       Currency       CHAR(10) NOT NULL
       );

    INSERT INTO ACCOUNTS (id,name,Credit,Currency) VALUES (1,'raj',1000,'rubles');
    INSERT INTO ACCOUNTS (id,name,Credit,Currency) VALUES (2,'jay',1000,'rubles');
    INSERT INTO ACCOUNTS (id,name,Credit,Currency) VALUES (3,'veer',1000,'rubles');






    begin;
    update accounts set credit = credit - 500 where id = 1;
    savepoint T1;
    update accounts set credit = credit + 500 where id = 3;

    begin;
    update accounts set credit = credit - 700 where id = 2;
    savepoint T2;
    update accounts set credit = credit + 700 where id = 1;


    begin;
    update accounts set credit = credit - 100 where id = 2;
    savepoint T3;
    update accounts set credit = credit + 100 where id = 3;






#Rollbacks
    rollback to T1;
    update accounts set credit = credit + 500 where id = 2;

    rollback to T2;
    update accounts set credit = credit + 700 where id = 3;

    rollback to T3;
    update accounts set credit = credit + 100 where id = 1;
  
 Screenshots: <br>
![Screenshot (891)](https://user-images.githubusercontent.com/69463767/165023740-fcc97d4d-9a43-41e0-b431-c17d6c1e8931.png)
