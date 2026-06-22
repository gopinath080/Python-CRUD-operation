import pymysql
class dbcode:
    def __init__(self):
        self.con=pymysql.connect(host='localhost',user='root',password='gopi8442',database='inventory')
    def insertdata(self,n,ca,pr,q):
        t='insert into info(Name,Category,price,Quantity) values("{0}","{1}",{2},{3})'.format(n,ca,pr,q)
        cur=self.con.cursor()
        r=cur.execute(t)
        self.con.commit()
        print('saved' if r!=0 else "failed")

    def updatedata(self,p,i):
        t="update info set price={0} where productID={1}".format(p,i)
        cur=self.con.cursor()
        r=cur.execute(t)
        self.con.commit()
        print("updated" if r!=0 else "failed" )
    def deletedata(self,i):
        t="delete from info where productID={0}".format(i)
        cur=self.con.cursor()
        s=input("Are you sure? type Y,N")
        if s in "Yy" :
            r=cur.execute(t)
            self.con.commit()
            print(" Product deleted" if r!=0 else "failed")
        else:
            print("canceled")
    def viewdata(self):
        cur=self.con.cursor()
        cur.execute("select * from info")
        r=cur.fetchall()
        for i in r:
            for j in i:
                print(j,end=" ")
            print()
