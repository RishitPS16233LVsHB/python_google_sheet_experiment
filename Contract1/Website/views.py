from flask import Blueprint,render_template,request

views = Blueprint("views",__name__)

@views.route("/",methods=['GET','POST'])
def home():
    # if submitted the form
    if(request.form):
        #get all three fields
        user = request.form['username']
        phone = request.form['phone']
        email = request.form['email']

        #connect to google service account and append new data to the spread sheet
        import gspread        
        service_account = gspread.service_account("C:\\Users\\hp\\Desktop\\Contract1\\Website\\templates\\Service_account.json")
        Sheet = service_account.open("MyTemp")
        WorkSheet = Sheet.worksheet("Sheet1")
        newData = [user,phone,email]
        WorkSheet.append_row(newData)

    #then render again the page
    return render_template("first.html")