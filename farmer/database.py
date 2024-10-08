import sqlite3
conn=sqlite3.connect('farmer.db')
query="create table farmerdata [N int,P int,k int,t int,h int,ph int,r int,prediction int]"
curs_obj=conn.cursor()
curs_obj.execute(query)
conn.commit()
curs_obj.close()
conn.close()