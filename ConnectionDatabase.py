import datetime
import mysql.connector

import config


class FetchDataFromDatabase:        

    @staticmethod
    def Connection():
        return mysql.connector.connect(
            host= config.DB_HOST, # Vidyesh.mysql.pythonanywhere-services.com
            user= config.DB_USER, #  Vidyesh
            password= config.DB_PASSWORD, # 
            database= config.DB_NAME #  Vidyesh$saiplaza
        )
        
    def fetchUpi(self,flatno):
        try: 
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            mycursor.execute("SELECT upi_id FROM payementmode WHERE flatno = %s",(flatno,))
            upi_tuples = mycursor.fetchall()
            if upi_tuples:
                upi_list = [r[0] for r in upi_tuples]
                return upi_list
            else: 
                return None
            
        except Exception as e:
            print(e)  
            
            
    def AddUpi(self,flatno,upiid):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            print("Flat No in add upi : ",flatno ,"And upi id is : ",upiid)
            
            mycursor.execute("INSERT INTO payementmode (upi_id,flatno) VALUES (%s,%s)",(upiid,flatno))
            mydb.commit()
            
        except Exception as e:
            print(e)


            
                        
        
    def checkPassword(self,userid,passw):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            mycursor.execute("SELECT Password FROM customer WHERE UserId = %s",(userid,))
            dbpassw = mycursor.fetchone()
            print(dbpassw[0])
            dbpassw = dbpassw[0]
            
            if passw == dbpassw:
                return True
            else:
                return False
            
        except Exception as e:
            print(e)     

     
    
    def addNewMonth(self, date):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            first_day_of_month = date
            print(first_day_of_month)
            for i in range(1,22):
                
                mycursor.execute("SELECT OSAmount,FlatNo,Name FROM customer WHERE srno = %s",(i,))
                myarray = mycursor.fetchone()
                print(myarray[0],myarray[1],myarray[2])
                
                InsertQures = "INSERT INTO calculator (Month, FlatNo, Name, CurrentPayable, PaymentDone, OSAmount) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (first_day_of_month, myarray[1], str(myarray[2]), myarray[0] + 1000, 0,myarray[0])
                
                mycursor.execute(InsertQures,values)
                
                updateQures = "UPDATE customer SET OSAmount = %s WHERE srno = %s"
                updatevalues = (myarray[0]+1000,i)
                
                mycursor.execute(updateQures,updatevalues)
            
                mydb.commit()
                    
                
        except Exception as e:
            print(e)     

                
    def fetchCalculator(self,flatno):
        try: 
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            mycursor.execute("SELECT * FROM calculator WHERE FlatNo = %s",(flatno,))
            arraRecord = mycursor.fetchall()
            
            return arraRecord
            
        except Exception as e:
            print("Error : ",e)
 
          
    def fetchAllCalculator(self):
        try: 
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            mycursor.execute("SELECT * FROM calculator")
            arraRecord = mycursor.fetchall()
            
            return arraRecord
            
        except Exception as e:
            print("Error : ",e)

            
    def fetchCalculatorByMonth(self, month):                                    
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            query = """
            SELECT * 
            FROM calculator 
            WHERE month = %s
            """
            mycursor.execute(query, (month,))
            records = mycursor.fetchall()
            
            return records
        except Exception as e:
            print("Error in fetchCalculatorByMonth:", e)
        finally:
            mydb.close()
            mycursor.close()
            
    def fetchCalculatorByMonthAndFlatno(self,flatno, month):                                    
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            query = """
            SELECT * 
            FROM calculator 
            WHERE month = %s AND FlatNo = %s
            """
            mycursor.execute(query, (month,flatno))
            records = mycursor.fetchall()
            
            return records
        except Exception as e:
            print("Error in fetchCalculatorByMonth:", e)
     
        
        
                
    def fetchCustomer(self,flatno):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            mycursor.execute("SELECT * FROM customer WHERE FlatNo = %s",(flatno,))
            arrayRecord = mycursor.fetchone()
            
            return arrayRecord      
        except Exception as e:
            print(e)
        finally:
            mydb.close()
            mycursor.close()            
                
    def fetchFlatNo(self):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            mycursor.execute("SELECT FlatNo FROM customer")
            arrayFlatNo = mycursor.fetchall()
            return arrayFlatNo
        except Exception as e:
            print(e)

           
    def fetchBillData(self,id):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            mycursor.execute("SELECT billno,paymentDatetime,amount,status FROM bill WHERE user_id = %s",(id,))
            array = mycursor.fetchall()

            return array
        except Exception as e:
            print(e)

            
    def fetchBillByFlatno(self,flatno, month):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            print("Flat No in fetchBillByFlatno : ",flatno ,"And month is : ",month)
            mycursor.execute("SELECT BillNo,paymentDatetime,Amount,status FROM bill WHERE user_id = %s AND DATE(paymentDatetime) = %s",(flatno,month))
            array = mycursor.fetchall()
        
            return array
        except Exception as e:
            print(e)
      
            
    def fetchupi(self,flatno):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM payementmode WHERE flatno = %s",(flatno,))
            record = mycursor.fetchall()
            return record
        except Exception as e:
            print(e)

            
    def delete_upi(self,upid):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            mycursor.execute("DELETE FROM payementmode WHERE upi_id = %s",(upid,))
            mydb.commit()
            return 
        except Exception as e:
            print(e)
            
    def FetchMessage(self):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM chatbox ORDER BY datetime DESC")
            messages = mycursor.fetchall()
            return messages
        except Exception as e:
            print(e)
    
    def insertMessage(self,flatno, message):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            datenow = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            
            name = self.fetchCustomer(flatno)[5] 
            
            insertQuery = "INSERT INTO chatbox (flatno,name,message,datetime) VALUES (%s,%s,%s,%s)"
            values = (flatno,name,message,datenow)
            
            mycursor.execute(insertQuery, values)
            mydb.commit()
            return
        except Exception as e:
            print("Error in insertMessage Function:", e)        
                     
            
    def fetchAvailableMonthYears(self):
        mydb = self.Connection()
        cursor = mydb.cursor()
        query = """
        SELECT DISTINCT 
            MONTH(STR_TO_DATE(month, '%Y-%m')) AS month, 
            YEAR(STR_TO_DATE(month, '%Y-%m')) AS year 
        FROM calculator 
        ORDER BY year DESC, month DESC
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        return [{'month': f"{row[0]:02d}", 'year': str(row[1])} for row in rows]
        
    def filterDataByMonthYear(self, month, year):
        query = "SELECT DISTINCT PaymentDone, OSAmount FROM calculator WHERE 1=1"
        params = []

        if year:
            query += " AND YEAR(STR_TO_DATE(month, '%Y-%m')) = %s"
            params.append(int(year))

        if month:
            query += " AND MONTH(STR_TO_DATE(month, '%Y-%m')) = %s"
            params.append(int(month))

        self.cursor.execute(query, tuple(params))
        rows = self.cursor.fetchall()

        # Use a set to avoid duplicates
        unique_rows = list(set(rows))
        
        return [{'PaymentDone': row[0], 'OSAmount': row[1]} for row in unique_rows]


                                   
            
    def insertToBill(self,amount,payment_id,flatno,month,condition):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            arrayCustomer = self.fetchCustomer(flatno)
            
            amount = int(amount)    
    
            OutstandingAmount = int(arrayCustomer[6])-amount 
            
    
            
            if condition:
                self.insertIntoBill(payment_id,month,arrayCustomer,amount,OutstandingAmount,"Done")
            
            
            updateQuery = "UPDATE customer SET OSAmount = %s WHERE UserId = %s"
            updateValue = (
                        OutstandingAmount, #os amount 0
                        arrayCustomer[0] #id 
                    )
            
            mycursor.execute(updateQuery,updateValue)
            
            paymenDone = self.sumOfBill(flatno,month)
    
            
            updateQueryCalculator = "UPDATE calculator SET PaymentDone = %s,OSAmount = %s,CurrentPayable = %s WHERE FlatNo = %s AND Month = %s"
            updateValueCalculator = (paymenDone, 
                                    OutstandingAmount,
                                    OutstandingAmount,
                                    flatno,
                                    month
                                )
            
            mycursor.execute(updateQueryCalculator,updateValueCalculator)
        
            mydb.commit()
 
        except Exception as e:
            print(e)

            
    def insertIntoBill(self,payment_id,month,arrayCustomer,amount,OutstandingAmount,status):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            datenow = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            
            insertQuery = "INSERT INTO bill (BillNo,month,user_id,name,email_id,PhoneNo,Amount,OSAmount,paymentDatetime,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (
                    payment_id, #bill no
                    month, #month
                    arrayCustomer[0], #userid
                    arrayCustomer[5], #name
                    arrayCustomer[4], #emailid
                    arrayCustomer[3], #phoneno
                    amount, #amount
                    OutstandingAmount, #os amount 0
                    datenow,
                    status
                )
            
            mycursor.execute(insertQuery,values)
            mydb.commit()
            return
        except Exception as e:
            print("Error in InsertIntoBill Function :",e)
            return 0        
            
    def uploadImage(self,payment_id,filename,binary_data,flatno):
        mydb = self.Connection()
        cursor = mydb.cursor()
        
        cursor.execute("INSERT INTO images(id,name,image_data,flatno) VALUES (%s,%s,%s,%s)",(payment_id,filename,binary_data,flatno))
        mydb.commit()
        mydb.close()
        cursor.close()  
            
            
    def sumOfBill(self,flatno,month):  
        try: 
            mydb = self.Connection() 
            myCallingCurcor = mydb.cursor()
                
            myCallingCurcor.execute("SELECT sum(Amount) FROM bill WHERE user_id = %s AND month = %s",(flatno,month))
            paymenDone = myCallingCurcor.fetchone()
            paymenDone = paymenDone[0]
            
            return paymenDone
        except Exception as e:
            print(e)
            return 0 
            
    def allpendingbill(self):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            mycursor.execute("SELECT id,name,flatno FROM images;")
            bills = mycursor.fetchall()
            return bills
        except Exception as e:
            print(e)
            
    def get_bill_image(self, bill_id):
        mydb = self.Connection()
        cursor = mydb.cursor()
        cursor.execute("SELECT image_data,name FROM images WHERE id = %s", (bill_id,))
        return cursor.fetchone()
    
    def reject_bill(self, bill_id):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            # Delete the bill from the images table
            mycursor.execute("DELETE FROM images WHERE id = %s", (bill_id,))
            mydb.commit()
            
            # Update the bill status to 'Rejected'
            mycursor.execute("UPDATE bill SET status = 'Rejected' WHERE BillNo = %s", (bill_id,))
            mydb.commit()
            
        except Exception as e:
            print(e)
            
    
    def approvebill(self,billno):
        try:
            mydb = self.Connection()
            mycursor = mydb.cursor()
            
            mycursor.execute("UPDATE bill SET status = 'Done' WHERE BillNo =%s",(billno,))
            mydb.commit()
            
            mycursor.execute("DELETE FROM images WHERE id = %s",(billno,))
            mydb.commit()
            
            mycursor.execute("SELECT * FROM bill WHERE BillNo = %s;",(billno,))
            bill = mycursor.fetchone()
            
            amount = bill[5]
            flatno = bill[1]
            month = bill[7]
            
            self.insertToBill(amount,None,flatno,month,False)
            
            return
        except Exception as e:
            print(e)
                