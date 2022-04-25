import pymysql
class connection1:
   
    def getconnection(self):
        try:
            conn = pymysql.connect(host='localhost',user='root',
                                   password='',db='itvedant')
        except Exception as e:
            print(e)
        else:
            print("Connection Succesfull")
            return conn
            

            
