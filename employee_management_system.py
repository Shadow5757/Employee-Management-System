import connection as c
import pymysql
from datetime import date

class Employee:     # Base Class Employee

    def getdata(self):
        self._eid = int(input("Enter Employee ID: "))
        self._ename = input("Enter Employee Name: ")
        self._dob = input("Enter Employee Date of Birth: ")
        d = date.today()
        self._doj = str(d)
        self._address = input("Enter Address: ")
        self._email = input("Enter Email_id: ")
        
        while True:
            try:
                self._mobile = int(input("Enter Mobile Number: "))  # Exception Handeling to Check Mobile number is entered correctly
            except ValueError as e:
                print("Please Enter Mobile No. in Integer")
            else:
                try:
                    x = len(str(self._mobile))
                    if x==10:
                        print("Mobile No. is Valid")
                    else:
                        raise Exception("Enter 10 Digit Mobile Number")
                except Exception as e:
                    print(e)
                else:
                    break

    def show(self):
        print()
        print("Employee ID: ",self._eid)
        print("Employee Name: ",self._ename)
        print("Employee Date of Birth: ",self._dob)
        print("Employee Date of Joining: ",self._doj)
        print("Employee Address: ",self._address)
        print("Employee Email-ID: ",self._email)
        print("Employee Mobile Number: ",self._mobile)


class Department(Employee):     # Derived class Department 

    def getdata(self):
        Employee.getdata(self)
        self._dptid = int(input("Enter Department ID: "))
        self._dptname = input("Enter Department Name: ")
        self._bs = int(input("Enter Employee Salary: "))

    def show(self):
        Employee.show(self)
        print("Employee Department ID: ",self._dptid)
        print("Employee Department Name: ",self._dptname)
        print("Employee Salary: ",self._bs)


class Payroll(Department):      # Derived class Payroll

    def compute(self):
        Department.getdata(self)
        if self._bs<3000:
            self._hra=self._bs*2/100
            self._ca=self._bs*2.5/100
            self._pf=self._bs*7.5 /100

        elif self._bs>=30000 and self._bs<70000:
            self._hra=self._bs*2.5/100
            self._ca=self._bs*3/100
            self._pf=self._bs*7.5 /100

        else:
            self._hra=self._bs*3.5/100
            self._ca=self._bs*3.5/100
            self._pf=self._bs*7.5 /100

        self._gp = self._bs + self._hra + self._ca - self._pf

    def show(self):
        Department.show(self)
        print("hra: ",self._hra)
        print("ca: ",self._ca)
        print("pf: ",self._pf)
        print("Gross salary: ", self._gp)

class Database(Payroll):        # Derived class Database
            
    def insertion(self):        # SQL Insertion Block
        Payroll.compute(self)
        con = c.connection1()
        conn=con.getconnection()                
        query="insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self._eid,self._ename,self._dob,self._doj,self._address,self._email,self._mobile,
               self._dptid,self._dptname,self._bs,self._hra,self._ca,self._pf,self._gp)
        cur = conn.cursor()
        cur.execute(query,val)
        conn.commit()
        print("Record Insert Successfully")
        conn.close()

    def record(self):        # SQL To View Record Block       
        con = c.connection1()
        conn=con.getconnection()
        query = "select * from employee"
        cur = conn.cursor()
        cur.execute(query)
        result=cur.fetchall()
        for row in result:
            print(row)
        conn.commit()
        conn.close()

    def deletion(self):        # SQL Deletion Block       
        con = c.connection1()
        conn=con.getconnection()
        self._eid = int(input("Enter employee Id to be deleted: "))
        query = "delete from employee where empid=%s"
        cur = conn.cursor()
        cur.execute(query,self._eid)
        conn.commit()
        print("Record successfully Deleted")
        conn.close()

    def updation(self):        # SQL Updation Block
        con = c.connection1()
        conn=con.getconnection()
        self._eid = int(input("Enter Employee ID: "))
        self._dptname = input("Enter the Department Name: ")
        query = "update employee set deptname=%s where empid=%s"
        val = (self._dptname,self._eid)
        cur = conn.cursor()
        cur.execute(query,val)
        conn.commit()
        print("Record successfully Updated")
        conn.close()

            
# Main Program

d = Database()
print('''
1. Insert Record
2. Show Record
3. Delete Record
4. Update Record
''')                

ch = int(input("Enter Your Choice: "))  # 4 Option Choices

if ch==1:
    d.insertion() 
elif ch==2:
    d.record()
elif ch==3:
    d.deletion()
elif ch==4:
    d.updation()
else:
    pass

