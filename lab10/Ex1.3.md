Table ledger :

    create table ledger(id serial not null primary key,
				   sender int not null,
				   receiver int not null,
				   fee int not null,
				   amount int not null,
				   transactiondatetime timestamp not null 
				   )
           
           
Transactions and updating the table ledger on that basis :

    begin;
    update accounts set credit = credit - 500 where id = 1;
    savepoint T1;
    update accounts set credit = credit + 500 where id = 3;'
    INSERT INTO ledger (id,sender,receiver,fee,amount,transactiondatetime) VALUES (1,1,3,0,500,current_timestamp);
    
    begin;
    update accounts set credit = credit - 730 where id = 2;
    savepoint T2;
    update accounts set credit = credit + 700 where id = 1;
    INSERT INTO ledger (id,sender,receiver,fee,amount,transactiondatetime) VALUES (2,2,1,30,700,current_timestamp);
    
    begin;
    update accounts set credit = credit - 130 where id = 2;
    savepoint T3;
    update accounts set credit = credit + 100 where id = 3;
    INSERT INTO ledger (id,sender,receiver,fee,amount,transactiondatetime) VALUES (3,2,3,30,100,current_timestamp);
    
    
Updated function from 1.2 to also insert values into ledger :

    CREATE OR REPLACE FUNCTION transaction(sender integer, receiver integer, amount integer, sender_bank character, receiver_bank character) 
    RETURNS TABLE (id INT,
           name CHAR,
           credit INT,
           currency CHAR,
           bankname CHAR) AS $$
    declare
    fees integer:=30;
    BEGIN 

    if sender_bank = receiver_bank then  
           update accounts set credit = accounts.credit - amount  where accounts.id = sender;
           update accounts set credit = accounts.credit + amount where accounts.id = receiver;
	   INSERT INTO ledger (id,sender,receiver,fee,amount,transactiondatetime) VALUES (sender,receiver,0,amount,current_timestamp);
    end if;
           
    if sender_bank != receiver_bank then
           update accounts set credit = accounts.credit - amount - fees where accounts.id = sender;
           update accounts set credit = accounts.credit + amount where accounts.id = receiver;
	   INSERT INTO ledger (id,sender,receiver,fee,amount,transactiondatetime) VALUES (sender,receiver,fees,amount,current_timestamp);
    end if;

           
           RETURN QUERY SELECT * 
    FROM 
    accounts;
    END; $$ 

    LANGUAGE 'plpgsql';
    
    
    
