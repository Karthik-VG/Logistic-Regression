import zipfile
from FolderLabels import *
from Filterdata import *
from combination import *
from logger import *
from flask import Flask,flash,request,redirect,send_file,render_template
from flask_cors import CORS,cross_origin
from werkzeug.utils import secure_filename
import os
from modls import *


if not os.path.exists(os.getcwd()+"//"+"files") :
    os.mkdir(os.getcwd()+"//"+"files")

app=Flask("__name__")

logs=logger("app.py")
logg=logs.getLog("logs")

uploads=os.getcwd()+"//files//"
UPLOAD_FOLDER = uploads
basepath=uploads


@app.route("/")
@cross_origin()
def homepage():
    return render_template("homepage.html")


@app.route("/create")
@cross_origin()
def create():
    #Basepath refers to the path where fiiles gets stored.


    #Creating structure of folders to save filtered files.
    f=FolderLabels.FolderLabels(basepath)

    f.create_folders("Test",f.folder_names())
    logg.info("Folder names created successfully . . . !")

    #cleaning all the files which having extra lines
    filter=Filterdata(basepath,"Test")
    filter.clean_files()
    logg.info("All files cleaned successfully . . . !")
    #Combining all the data and storing in single file
    c=combination(basepath)
    c.combine_data("Test")
    logg.info("All files combined and created as single file . . . !")

    return redirect("/")


#Code for upload and download of report
@app.route('/uploadfile', methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('no file')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(uploads+filename)
            try:
                with zipfile.ZipFile(os.path.join(uploads+filename)) as zf:
                    zf.extractall(os.path.join(uploads))
            except Exception as e:
                logg.error("Got Error inside Upload module while unzip ! . . . .")
            print("saved file successfully")
            logg.info("File uploaded successfully ...")
            return redirect('/')

    return render_template('upload.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    #For rendering results on HTML GUI
    if request.method == 'POST':
        time=request.form.get("time")
        ip1=request.form.get("ip1")
        ip2=request.form.get("ip2")
        ip3=request.form.get("ip3")
        ip4=request.form.get("ip4")
        ip5=request.form.get("ip5")
        ip6=request.form.get("ip6")
        arr=[[time,ip1,ip2,ip3,ip4,ip5,ip6]]
        logg.info("input values for prediction {}".format(arr))
        temp=modls(uploads)
        temp.read_clean_model_build()
        predicted_value=temp.predict(arr)
        return render_template('prediction.html', original_input={'Time':time,'avg_rss12':ip1,
                                                           'var_rss12':ip2,
                                                           'avg_rss13':ip3,"var_rss13":ip4,"avg_rss23":ip5,"var_rss23":ip6},result=predicted_value)

    return render_template("prediction.html")
# Columns: time	avg_rss12	var_rss12	avg_rss13	var_rss13	avg_rss23	var_rss23


if __name__=="__main__":
    app.run()