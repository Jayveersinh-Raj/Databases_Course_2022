    alter table accounts add column BankName char(10);

    update accounts set bankname = 'SberBank' where id = 1 or id = 3;
    update accounts set bankname = 'Tinkoff' where id = 2;
    
    
Postgres Function:

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
    end if;
               
    if sender_bank != receiver_bank then
               update accounts set credit = accounts.credit - amount - fees where accounts.id = sender;
               update accounts set credit = accounts.credit + amount where accounts.id = receiver;
    end if;

               
               RETURN QUERY SELECT * 
    FROM 
    accounts;
    END; $$ 

    LANGUAGE 'plpgsql';
    
Python Script:

    import psycopg2
    
    con = psycopg2.connect(database="bank", user="postgres",
                       password="jyvr2891", host="127.0.0.1", port="5432")

    cur = con.cursor()

    def customerRetrieval(sender_id, receiver_id, amount, sender_bank, receiver_bank):
    try:
     cur.callproc('transaction', (sender_id, receiver_id, amount, sender_bank, receiver_bank))

     # process the result set
     row = cur.fetchone()
     while row is not None:
            print(row)
            row = cur.fetchone()

     cur.close()
    
     except (Exception, psycopg2.DatabaseError) as error:
        print(error)
     finally:
        if con is not None:
            con.close()



    if __name__ == '__main__':
       #customerRetrieval(1,3,500,'SberBank','SberBank')
       #customerRetrieval(2,1,700,'SberBank','Tinkoff')
       customerRetrieval(2,3,100,'Tinkoff','SberBank')
       
  Screenshots:
  
 ![Screenshot (893)](https://user-images.githubusercontent.com/69463767/165024289-d703b86c-2126-4ca5-be50-854b575241d6.png)
![Screenshot (895)](https://user-images.githubusercontent.com/69463767/165024293-05d9bc44-d1a8-4546-bd4c-8b94a108a570.png)
![Screenshot (894)](https://user-images.githubusercontent.com/69463767/165024298-3aec8b18-bf5f-4e81-acfd-110d311092dc.png)

    
