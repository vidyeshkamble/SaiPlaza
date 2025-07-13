from datetime import datetime
import io
import random as rand
from flask import Flask, jsonify, redirect, render_template, request, send_file, session, url_for
from ConnectionDatabase import FetchDataFromDatabase
from PaymentGetway import PaymentGetway
import config
from emailphoneOTP import FetchOTP
import pandas as pd

app = Flask(__name__)
app.secret_key = 'applicationSaiPlaza'


@app.route('/')
def loginpage():
    
    obj = FetchDataFromDatabase()
    arrayflatno = obj.fetchFlatNo()
    list_of_integers = [item[0] for item in arrayflatno]
    
    return render_template('login.html', arrayFlatno = list_of_integers)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('loginpage'))


@app.route('/login',methods = ['POST'])
def login():
    data = request.get_json()
    userId = data.get('id')
    passw = data.get('pass')
    
    if not userId or not passw:
        return jsonify({'message': 'Missing credentials'}), 400
    
    obj = FetchDataFromDatabase()
    TF = obj.checkPassword(userId,passw)
    if TF:     
        session['flatno'] = userId
        session['admin'] = int(userId) == 701
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message':'Invalid Login'}),401
    
@app.route('/dashbord', methods=['GET', 'POST'])
def OptionSelected():
    flatno = session.get('flatno')

    adminobject = session.get('admin')

    
    obj = FetchDataFromDatabase()
    array = obj.fetchCalculator(flatno)
    
    arrayflatno = obj.fetchFlatNo()
    list_of_integers = [item[0] for item in arrayflatno]
    
    billmonths = obj.fetchBillData(flatno)
    monthofbill = [item[1].split(' ')[0] for item in billmonths]
    monthofbill = list(set(monthofbill))
    
    message = obj.FetchMessage()
    if not message:
        message = ""
    
    return render_template('index.html',adminobj = adminobject,arrayFlatno = list_of_integers, displayTableCustomer = array, monthofbill = monthofbill,messages = message)    

@app.route('/sendmessage', methods=['POST'])
def sendmessage():
    data = request.get_json()
    message = data.get('message')
    flatno = session.get('flatno')
    
    obj = FetchDataFromDatabase()
    obj.insertMessage(flatno,message)
    
    return jsonify({'message': 'Message sent successfully'})

@app.route('/get-available-dates', methods=['GET'])
def get_available_dates():
    obj = FetchDataFromDatabase()
    results = obj.fetchAvailableMonthYears()
    return jsonify(results)

@app.route('/month-year-filter', methods=['POST'])
def month_year_filter():
    data = request.get_json()
    month = data.get('month')
    year = data.get('year')

    obj = FetchDataFromDatabase()
    results = obj.filterDataByMonthYear(month, year)

    return jsonify({'results': results})


                                                        # too Add New Month 
@app.route('/NewMonth',methods=['POST'])
def NewMonth():
    date = request.form['date']
    
    db_fetcher = FetchDataFromDatabase()
    db_fetcher.addNewMonth(date) 
    
    obj = FetchDataFromDatabase()
    arrayflatno = obj.fetchFlatNo()
    list_of_integers = [item[0] for item in arrayflatno]
    
    return redirect(url_for('OptionSelected'))


@app.route('/gotopaymentreceived', methods=['GET', 'POST'])
def gotopaymentreceived():
    obj = FetchDataFromDatabase()
    
    array = obj.fetchAllCalculator()

    if not array:
        return render_template('paymentreceived.html', message="No payment records found.")
    
    unic = set(row[0] for row in array)  # Get unique flat numbers
    
    arrayflatno = obj.fetchFlatNo()
    allFlatno = [item[0] for item in arrayflatno]

    # Convert the array to a list of dictionaries for easier rendering
    records = [{"month": row[0], "flatno": row[1], "name": row[2], "OSAmount": row[3], "paymentdone" : row[4] } for row in array]
    
    return render_template('paymentreceived.html', records=records, unic=unic,flatnos = allFlatno)

@app.route('/filterbyflatno',methods=['POST' , 'GET'])
def filterbyflatno():
    data = request.get_json()
    month = data.get('month')
    flatno = session.get('flatno')
    
    obj = FetchDataFromDatabase()
    array = obj.fetchCalculatorByMonthAndFlatno(flatno,month)
    
    if not array:
        return jsonify({'message': 'No records found for the selected flat number.'}), 404
    
    
    records = [{"month": row[0], "flatno": row[1], "name": row[2], "OSAmount": row[5], "paymentdone" : row[4]} for row in array]
    
    return jsonify({'records': records})

@app.route('/filterbyflatnobill',methods=['POST' , 'GET'])
def filterbyflatnobill():
    data = request.get_json()
    month = data.get('month')
    flatno = session.get('flatno')
    obj = FetchDataFromDatabase()
    array = obj.fetchBillByFlatno(flatno, month)

    if not array:
        return jsonify({'message': 'No records found for the selected flat number.'}), 404
    
    records = [{"bill_no": row[0], "month": row[1], "amount": row[2],"status" : row[3]} for row in array]
    return jsonify({'records': records})

@app.route('/filterbyflatnoCalculator', methods=['POST'])
def filterbyflatnoCalculator():
    data = request.get_json()
    month = data.get('month')
    flatno = data.get('flatno')
    
    obj = FetchDataFromDatabase()
    if month and flatno:
        array = obj.fetchCalculatorByMonthAndFlatno(flatno, month)
    elif month:
        array = obj.fetchCalculatorByMonth(month)
    elif flatno:
        array = obj.fetchCalculator(flatno)    
    
    if not array:
        return jsonify({'message': 'No records found for the selected flat number.'}), 404
    
    total_os = sum(int(r[3]) for r in array)
    total_payment = sum(int(r[4]) for r in array)
    

    records = [{"month": row[0], "flatno": row[1], "name": row[2], "OSAmount": row[3], "paymentdone" : row[4]} for row in array]
    
    return jsonify({'records': records,"totalOS": total_os,"totalPayment": total_payment})



@app.route('/FetchBill', methods=['POST'])
def FetchBill():
    user_id = session.get('flatno')
    
    obj = FetchDataFromDatabase()
    array = obj.fetchBillData(user_id)

    if array:
        bill = [{"bill_no": row[0], "month": row[1], "amount": row[2],"status":row[3]} for row in array]
        return jsonify(bill)
    else:
        return jsonify([])

    
    
    
    
@app.route('/monthlyRecord',methods = ['POST'])
def monthlyRecord():
    return jsonify(True)    





@app.route('/Payment', methods = ['POST'])              # Going to the Payment Page 
def Payment():
    Flatno = request.form['flatno']
    Amount = request.form['amountPayable']
    
    
    obj = FetchDataFromDatabase()
    arrays = obj.fetchCalculator(Flatno)
    arrays = arrays[-1]
    
    flatno = session.get('flatno')
    session['PayAmount'] = Amount 
    
    responce = obj.fetchUpi(flatno)
    
    return render_template('payment.html',amount = Amount, Array = arrays,responce = responce)


@app.route('/gotoupihtml', methods=['GET', 'POST'])
def gotoupihtml():
    obj = FetchDataFromDatabase()
    flatno = session.get('flatno')
    record = obj.fetchupi(flatno)
    
    if record:
        return render_template("addupi.html",record = record)
    else:
        return render_template("addupi.html",record = "No Upi ID Avalable !")
        


@app.route('/addupi', methods=['POST'])   
def addupi():
    data = request.get_json()
    upiId = data.get('upiId')

    obj = FetchDataFromDatabase()
    flatno = session.get('flatno')
    obj.AddUpi(flatno, upiId)

    return jsonify({'status': 'added'})

@app.route('/deleteUPI/<upi_id>')
def deleteUPI(upi_id):
    
    obj = FetchDataFromDatabase()
    obj.delete_upi(upi_id)
    return redirect(url_for('OptionSelected'))

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')


@app.route('/gotopendingbills', methods=['GET', 'POST'])
def gotopendingbills():
    
    obj = FetchDataFromDatabase()
    bills = obj.allpendingbill()

    return render_template("BillPending.html",bills = bills)

@app.route('/download-bill-image/<int:bill_id>')
def download_bill_image(bill_id):
    obj = FetchDataFromDatabase()
    result = obj.get_bill_image(bill_id)  # Custom method you write
    
    if result:
        image_data, image_name = result
        return send_file(
            io.BytesIO(image_data),
            mimetype='image/jpeg',
            download_name=image_name,
            as_attachment=True
        )
    return "Image not found", 404

@app.route('/reject_bill/<int:bill_id>')
def reject_bill(bill_id):
    obj = FetchDataFromDatabase()
    obj.reject_bill(bill_id)
    return redirect(url_for('gotopendingbills'))



 
@app.route('/callPhonePay',methods = ['POST'])              #phone Pay Code
def callPhonePay():
    try :
        data = request.get_json()
        amount = data.get('amount')
        upiId = data.get('upiid')
        
        if upiId is None:
        
            return jsonify({"status": "stopped", "message": "UPI is not registered!"})
        
        obj = PaymentGetway()
        RetrunPaymenrResult = obj.clientCall(amount,upiId)
            
        transactionID = RetrunPaymenrResult
        
        if RetrunPaymenrResult:
            return jsonify({"status": "success", "message": "Redirecting to PhonePe","transactionID":transactionID }), 200
        else:
          
            return jsonify({"status": "fail", "message" : "Payment is on Pending State Until the Admin Varification!"}), 200    
    except Exception as e:
        
        return None    
        
@app.route('/cashPayment', methods=['POST'])
def cashPayment():
    try:
        data = request.get_json()
        amount = data['amount']
        
        
        flatno = session.get('flatno')
        
        obj = FetchDataFromDatabase()
        calmonth = obj.fetchCalculator(flatno)

        if not calmonth:
            return jsonify({"status": "error", "message": "No calculator data found for this flat number"}), 404
        
        month = sorted(calmonth, key=lambda x: x[0], reverse=True)[0][0]
        
        payment_id = f"cash_{flatno}"
        
        obj.insertToBill(amount, payment_id, flatno, month, True)
        
        return jsonify({"status": "success", "message": "Cash payment recorded successfully", "payment_id": payment_id}), 200
    except Exception as e:
        
        return jsonify({"status": "error", "message": str(e)}), 500        


@app.route('/success')
def payment_success():
    obj = FetchDataFromDatabase()
    amount = request.args.get('amount')
    payment_id = request.args.get('payment_id') 
    flatno = session.get('flatno') 
    
    
    calmonth = obj.fetchCalculator(flatno)
    
    month = sorted(calmonth,key=lambda x : x[0], reverse=True)
    month = month[0][0]
       

    
    obj.insertToBill(amount,payment_id,flatno,month,True)
    
    return render_template("success.html", payment_id=payment_id, amount=amount)

@app.route('/fail')
def payment_fail():
    amount = request.args.get('amount')
    return render_template("fail.html",amount = amount)

@app.route('/uploadscreenshort' , methods =['POST'])
def uploadscreenshort():
    obj = FetchDataFromDatabase()  
    file = request.files.get('Paymentss')
    
    allowed_extensions = ['.png', '.jpg', '.jpeg']
    filename = file.filename.lower()
    flatno = session.get('flatno')
    
    payment_id = request.form.get('payment_id')
    
    # Uploading File to the database
    if file and any(filename.endswith(ext) for ext in allowed_extensions):
        binary_data = file.read()
        obj.uploadImage(payment_id,filename,binary_data,flatno)
    else:
        return "Invalid file type. Only PNG allowed.", 400
    

    amount = int(request.form.get('amount'))
    
    calculato = obj.fetchCalculator(flatno)
    lastmonth = calculato[-1]
    month = lastmonth[0]
    
    
    
    
    arrayCustomer = obj.fetchCustomer(flatno)
    OutstandingAmount = int(arrayCustomer[6])-amount 
    
    obj.insertIntoBill(payment_id,month,arrayCustomer,amount,OutstandingAmount,"Pending")
    return redirect(url_for('OptionSelected'))

@app.route('/downloadrecords',methods = ['POST'])
def downloadrecords():
    data = request.get_json()
    date = data.get('date')
    if not date:
        return jsonify({'message': 'Date is required'}), 400
    obj = FetchDataFromDatabase()
    recoreds = obj.fetchCalculatorByMonth(date)
    if not recoreds:
        return jsonify({'message': 'No records found for the selected date'}), 404
    
    recoreds = [row[:5] for row in recoreds]
    colume = ['Month','Flat no','Name','OS Amount','Payment Done']
    
    
    df = pd.DataFrame(recoreds,columns=colume) 
    output = io.BytesIO()
    df.to_excel(output,index=False,sheet_name='Records',engine='openpyxl')
    output.seek(0)
    
    return send_file(output,
                     download_name=f"records_{date}.xlsx",
                     as_attachment=True,
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    
@app.route('/approvebill', methods = ['POST'])
def approvebill():
    
    data = request.get_json()
    billno = data['billno']
    obj = FetchDataFromDatabase()

    obj.approvebill(billno)
    
    return jsonify({'status': 'success'})
    
    
@app.route('/getBill',methods = ['POST'])
def getBill():    
    return redirect(url_for('OptionSelected'))

                                        # Fet Geting OTP, Text Message And Emails 
                    
@app.route('/clear_session')                                        
def clear_session():
    session.clear()
    return redirect(url_for('index'))                                     

@app.route('/sendTextMessage', methods=['POST'])
def sendTextMessage():

    phoneNo = config.WATCHMAN_PHONE_NUMBER
    OTP = rand.randint(100000, 999999)
    FetchOTP.sendTextMessage(phoneNo,OTP)
    
    return jsonify({'status': 'success', 'message': 'OTP sent successfully', 'otp': OTP})


@app.route('/sendEmail')
def sendEmail():
    subject = ''
    message = ''
    to = ''
    FetchOTP.sendEmailMessage(subject,message,to)
    pass


if __name__ == '__main__':
    # app.debug=True  
    app.run(debug=True,host='0.0.0.0')  