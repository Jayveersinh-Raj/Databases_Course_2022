
<b><li> SQL Function query in plpgsql: </b><br/>

    CREATE OR REPLACE FUNCTION retrievecustomer(starting integer, ending integer) 
    RETURNS TABLE (id INT,
                   name TEXT,
                   address TEXT,
                   review TEXT) AS $$
    BEGIN 
    RETURN QUERY SELECT * 
    FROM 
    customer 
    WHERE  
    customer.id BETWEEN starting AND ending; 
    END; $$ 
    
    LANGUAGE 'plpgsql';
  </p>
  <br/>
  <br/>
  
 <b><li> Python function to call and function and retreieve the data: </b><br/>
 
    import psycopg2 
    con = psycopg2.connect(database="faker", user="postgres", 
                       password="jyvr2891", host="127.0.0.1", port="5432") 

    cur = con.cursor() 

    def customerRetrieval(start, end):
    try: 
       cur.callproc('retrievecustomer', (start,end))
 
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



    if __name__ == '__main__'
    
    #Example to retreive data between 10 and 40 
    customerRetrieval(10,40) 
  
   <b><li> The following is the screenshot with id and name (So it is easier to access) in the example 10 to 40 range: </b><br/>
  <br/>
  <br/>
   ![image](https://user-images.githubusercontent.com/69463767/163733128-56769b0c-8e15-4114-ac01-4ca8f007488b.png)

   
