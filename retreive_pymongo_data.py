from pymongo import MongoClient
import pandas as pd
class database:
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.attendanceDB
        self.name=[]
        self.attendance=[]

    def update(self,name):
        self.db.attendance.update_one({"name":name},{"$inc":{"attendance":1}})

    def addStudent(self, name):
        self.db.attendance.insert_one({"name":name},{"attendance":0})


    def view(self):
        self.name=[]
        self.attendance=[]
        records=self.db.attendance.find()
        j=0
        for i in records:
            j=j+1
            self.name.append(i["name"])
            self.attendance.append(i["attendance"])
        for i in range(j):
            print(self.name[i],self.attendance[i])

    def export_csv(self):
        self.view()
        data={"name":self.name,"attendance":self.attendance}
        df=pd.DataFrame(data,columns=["name","attendance"])
        df.to_csv("attendance.csv",index=True)