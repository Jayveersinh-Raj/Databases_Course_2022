1.1 Light weight Fighters:

     match (n)-[r:beats]->(c) 
     where  n.weight='155' XOR n.weight='170' XOR n.weight='185' 
     return *
     
 <img width="804" alt="Screenshot 2022-05-01 230826" src="https://user-images.githubusercontent.com/69463767/166157609-51980192-544f-4193-ae78-46037a30a3fb.png">

1.2 With record of 1-1, I do not understand if both has to defeat each other once, since there are no record where both has defeated each other once, I returned data for the fighters who atleast defeated a particular figher once.

    match (n)-[r:beats]->(c) return *, count(r)=1
    
 <img width="938" alt="Screenshot 2022-05-01 233119" src="https://user-images.githubusercontent.com/69463767/166158559-7909c9fd-6886-4a12-a0e7-95d6256930a0.png">
 
 1.3.1 Undefeated champions: (0) loss
 
 
    match (n)-[r:beats]->(c) where not ()-[:beats]->(n) return *
 <img width="908" alt="image" src="https://user-images.githubusercontent.com/69463767/166164748-dd51c179-4680-4289-a26d-e27bc2e61d86.png">


1.3.2 No win loosers:
    
    match (n) where not (n)-->() return distinct n
![ex1_part2_2](https://user-images.githubusercontent.com/69463767/166166294-5784595f-4086-43f9-a597-3c73567cc211.jpg)


1.4 Khabib beat them and have not fight them:
 
   match (a:Fighter)-[:beats*2..]->(b:Fighter) where a.name = "Khabib Nurmagomedov" return distinct b;
   
   ![ex1_part2_3](https://user-images.githubusercontent.com/69463767/166166329-cd2e5031-27fb-4fc3-9ead-aab6d376cfa7.jpg)
