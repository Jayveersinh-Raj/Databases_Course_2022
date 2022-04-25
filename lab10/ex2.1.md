Read committed:
Screenshot of the result:
![Screenshot (896)](https://user-images.githubusercontent.com/69463767/165077330-70d1b110-98fe-4162-9420-c3f337095629.png)

Reason for the above:
Read Committed is the default isolation level in PostgreSQL. When a transaction uses this isolation level, a SELECT query (without a FOR UPDATE/SHARE clause) sees only data committed before the query began; it never sees either uncommitted data or changes committed during query execution by concurrent transactions.
However after commiting, we can see both tables updated.

Further subtask to update:
Screenshot of the result terminal:
![Screenshot (897)](https://user-images.githubusercontent.com/69463767/165078291-dd92605a-f149-4766-8141-7a6853cfbd44.png)


Reason for the above:
If the first updater commits, the second updater will ignore the row if the first updater deleted it, 
otherwise it will attempt to apply its operation to the updated version of the row. The search condition of the command (the WHERE clause) is re-evaluated to see
if the updated version of the row still matches the search condition. If so, the second updater proceeds with its operation using the updated version of the row.
In the case of SELECT FOR UPDATE and SELECT FOR SHARE, this means it is the updated version of the row that is locked and returned to the client.
<br>
<br>
<br>
<br>
<br>
<br>
Repetable read: <br>
Screenshot:

![Screenshot (898)](https://user-images.githubusercontent.com/69463767/165079688-4c8a3446-dd6b-49be-ac95-e5b27d0c8d10.png)

Reasons for above: <br>
Yet another problem is that of non-repeatable reads. These happen when a transaction reads a row, and then reads it again a bit later but gets a different 
result – because the row was updated in between by another transaction. To fix this problem, set the isolation level of the transaction to “repeatable read”. PostgreSQL will then ensure that the second
(or any) read will also return the same result as the first read. Here is the same scenario at the upgraded isolation level.
<br>
<br>
<br>
Further tasks to update balance:
<br> Screenshot:

![Screenshot (899)](https://user-images.githubusercontent.com/69463767/165080586-efe3fd10-1ce0-4e29-86ac-1a34e21bef2b.png)
Reason :<br>
Because a repeatable read transaction cannot modify or lock rows changed by other transactions after the repeatable read transaction began.
