  <b><li> #Python code for Ex1 inclduing all the subtasks in one code: </b><br/>

   import psycopg2 <br/>
   from geopy.geocoders import Nominatim <br/>
   import psycopg2.extras <br/>

   hostname = 'localhost' <br/>
   database = 'dvdrental' <br/>
   username = 'postgres'  <br/>
   pwd = 'jyvr2891'  <br/>
   port_id = 5432

   conn = None <br/>
   cur = None <br/>
   try: <br/>
        conn = psycopg2.connect ( <br/>
            host = hostname, <br/>
            dbname = database, <br/>
            user = username, <br/>
            password = pwd, <br/>
            port = port_id <br/>
        ) <br/>
        
        # Inclusive task, creates 2 new columns latitude and longitude
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('''ALTER TABLE address
        ADD COLUMN latitude float,
        ADD COLUMN longitude float;''')
        
        
        
        #Sub task 1:
        cur_record = cur.execute(''' SELECT * FROM address
        WHERE city_id>=400 AND city_id<=600 AND 
        address.address LIKE '%11%' ''')
      
        data = cur.fetchall()
        for record in data:
                print(record['address'])

        city = cur.execute(''' SELECT district, postal_code FROM address ''')
        data = cur.fetchall()
        for record in data:
                print((record['district'], record['postal_code']))
        
        const = 0
        update = '''
        
        
        
        # Sub task 2 and 3 are comprised in the following:
        UPDATE address 
        SET 
        latitude = %s,
        longitude = %s
        WHERE district = %s;
        '''
    
      
        insert_values = []
        geolocator = Nominatim(user_agent="my_request")
        
        for record in data:
         const = const+1
         loc = record['district']
         try:
             location = geolocator.geocode(loc)
             insert_values.append((location.latitude,location.longitude))
             cur.execute(update,(location.latitude, location.longitude,loc))
    
             print((location.latitude,location.longitude))
         except Exception:
             lat = 0
             long = 0
             insert_values.append((lat,long))
             cur.execute(update,(lat,long,loc))
             print((lat,long))[Uploading lab9ex1.py…]()

             pass
  
        conn.commit()

except Exception as error: <br/>
     print(error) <br/>

finally : <br/>
    if conn is not None: <br/>
        conn.close() <br/>
    if cur is not None: <br/>
        cur.close() <br/>
        
        
   <br/>
<br/>     

########################################## SQL Queries #####################################<br/>
<br/>
<br/>
<p><b><li>Inclusive task to add 2 columns latitude and longitude: </b> <br/>
ALTER TABLE address <br/>
        ADD COLUMN latitude float, <br/>
        ADD COLUMN longitude float; <br/>
        
Screenshot with those columns: <br/>
![Screenshot (885)](https://user-images.githubusercontent.com/69463767/163729407-affb4f72-1e07-43be-87a7-33916fe1cbc1.png)

</p>
<br/>
<br/>
<br/>
<p><b><li>
1. Sub Task 1: </b><br/>
 SELECT * FROM address <br/>
        WHERE city_id>=400 AND city_id<=600 AND <br/>
        address.address LIKE '%11%' <br/>
        
  Screenshot: <br/>
     ![Screenshot (886)](https://user-images.githubusercontent.com/69463767/163729467-9697fe98-b2e5-4e91-8e53-4c84f7b9cf59.png)
                                           </p>
  <p><b><li>
 2.  Sub Task 2: </b><br/>
UPDATE address <br/>
        SET <br/>
        latitude = %s, <br/>
        longitude = %s <br/>
        WHERE district = %s; <br/>
        
Screenshot: <br/>
![Screenshot (887)](https://user-images.githubusercontent.com/69463767/163729541-8d2cd97b-569c-464c-8734-b45864bfc711.png)
</p>
<p><b><li>
3. Sub Task 3: </b><br/>
   Although, screenshot of 2 covers some 0s, but some more are here: <br/>
   Screenshot: <br/>

![Screenshot (888)](https://user-images.githubusercontent.com/69463767/163730167-a045fbe7-6b40-44b9-b186-ac9d1a58c22f.png)
<br/>
  <br/>![Screenshot (889)](https://user-images.githubusercontent.com/69463767/163730183-2004b6c8-95e3-487f-82be-3ae4023a3f14.png)

 
