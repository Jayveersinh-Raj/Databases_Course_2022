Read commited: <br>
Screenshot:
![Screenshot (901)](https://user-images.githubusercontent.com/69463767/165081646-b5faacfe-6181-445a-a006-ea272634ed3b.png)
<br>
<br>
Reason for the above:
The Repeatable Read isolation level only sees data committed before the transaction began; it never sees either uncommitted data or 
changes committed during transaction execution by concurrent transactions. 
(However, the query does see the effects of previous updates executed within its own transaction, even though they are not yet committed.) 

<br>
<br><br>
<br><br>
<br><br>
<br>

Repeatable Read:
