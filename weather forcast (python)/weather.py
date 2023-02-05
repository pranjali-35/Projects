from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470")
root.configure(bg="#57adff")
root.resizable(False,False)

def moreInfo(city):
    top=Toplevel()
    top.title("More Info")
    top.geometry("900x500+300+200")
    top.configure(bg="#57adff")
    top.resizable(False,False)

    c = Label(top,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
    c.place(x=380,y=12)

    c.config(text=city)

    """timezone = Label(top,font=("Helvetica",20),fg="black",bg="#57adff")
    timezone.place(x=30,y=10)

    geolocator= Nominatim(user_agent="geopiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)"""
        
    api = "https://api.openweathermap.org/data/2.5/forecast?q="+city+"&units=metric&appid=f778015abc2d6cecf62baa9b62848035"
    json_data = requests.get(api).json()

    #boxes
    r1 = Label(top,image=PhotoImage(file="Images/Rounded Rectangle 1 new.png"),bg="#212120").place(x=20,y=100)
    r2 = Label(top,image=PhotoImage(file="Images/Rounded Rectangle 1 new.png"),bg="#212120").place(x=240,y=100)
    r3 = Label(top,image=PhotoImage(file="Images/Rounded Rectangle 1 new.png"),bg="#212120").place(x=465,y=100)
    r4 = Label(top,image=PhotoImage(file="Images/Rounded Rectangle 1 new.png"),bg="#212120").place(x=692,y=100)
    r5 = Label(top,image=PhotoImage(file="Images/Rounded Rectangle 1 new.png"),bg="#212120").place(x=20,y=310)
    r6 = Label(top,image=PhotoImage(file="Images/Rounded Rectangle 1 new.png"),bg="#212120").place(x=240,y=310)
    r7 = Label(top,image=PhotoImage(file="Images/Rounded Rectangle 1 new.png"),bg="#212120").place(x=465,y=310)
    r8 = Label(top,image=PhotoImage(file="Images/Rounded Rectangle 1 new.png"),bg="#212120").place(x=692,y=310)

    #date time of each box
    d1 = Label(top,font=("Helvetica",11),fg="white",bg="#203243") 
    d1.place(x=45,y=70)
    dt1 = json_data['list'][0]['dt_txt']
    d1.config(text=(dt1))

    d2 = Label(top,font=("Helvetica",11),fg="white",bg="#203243") 
    d2.place(x=265,y=70)
    dt2 = json_data['list'][1]['dt_txt']
    d2.config(text=(dt2))

    d3 = Label(top,font=("Helvetica",11),fg="white",bg="#203243") 
    d3.place(x=490,y=70)
    dt3 = json_data['list'][2]['dt_txt']
    d3.config(text=(dt3))

    d4 = Label(top,font=("Helvetica",11),fg="white",bg="#203243") 
    d4.place(x=720,y=70)
    dt4 = json_data['list'][3]['dt_txt']
    d4.config(text=(dt4))

    d5 = Label(top,font=("Helvetica",11),fg="white",bg="#203243") 
    d5.place(x=45,y=280)
    dt5 = json_data['list'][4]['dt_txt']
    d5.config(text=(dt5))

    d6 = Label(top,font=("Helvetica",11),fg="white",bg="#203243") 
    d6.place(x=265,y=280)
    dt6 = json_data['list'][5]['dt_txt']
    d6.config(text=(dt6))

    d7 = Label(top,font=("Helvetica",11),fg="white",bg="#203243") 
    d7.place(x=490,y=280)
    dt7 = json_data['list'][6]['dt_txt']
    d7.config(text=(dt7))

    d8 = Label(top,font=("Helvetica",11),fg="white",bg="#203243") 
    d8.place(x=720,y=280)
    dt8 = json_data['list'][7]['dt_txt']
    d8.config(text=(dt8))

    #details

    #box1
    label1a = Label(top,text = "Temperature",font=('Helvetica',11),fg="white",bg="#212120")
    label1a.place(x=25,y=100)
    t1a = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    t1a.place(x=130,y=100)
    tt1a = json_data['list'][0]['main']['temp']
    t1a.config(text=(tt1a,"°C"))

    label2a = Label(top,text = "Humidity",font=('Helvetica',11),fg="white",bg="#212120")
    label2a.place(x=25,y=125)
    h1a = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    h1a.place(x=130,y=125)
    hh1a = json_data['list'][0]['main']['humidity']
    h1a.config(text=(hh1a,"%"))

    label3a = Label(top,text = "Pressure",font=('Helvetica',11),fg="white",bg="#212120")
    label3a.place(x=25,y=150)
    p1a = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    p1a.place(x=130,y=155)
    pp1a = json_data['list'][0]['main']['pressure']
    p1a.config(text=(pp1a,"hPa"))

    label4a = Label(top,text = "Wind Speed",font=('Helvetica',11),fg="white",bg="#212120")
    label4a.place(x=25,y=175)
    w1a = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    w1a.place(x=130,y=175)
    ww1a = json_data['list'][0]['wind']['speed']
    w1a.config(text=(ww1a,"m/s"))

    label5a = Label(top,text = "Description",font=('Helvetica',11),fg="white",bg="#212120")
    label5a.place(x=25,y=200)
    ds1a = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    ds1a.place(x=130,y=200)
    dds1a = json_data['list'][0]['weather'][0]['description']
    ds1a.config(text=(dds1a))

    #box2
    label1b = Label(top,text = "Temperature",font=('Helvetica',11),fg="white",bg="#212120")
    label1b.place(x=245,y=100)
    t1b = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    t1b.place(x=350,y=100)
    tt1b = json_data['list'][1]['main']['temp']
    t1b.config(text=(tt1b,"°C"))

    label2b = Label(top,text = "Humidity",font=('Helvetica',11),fg="white",bg="#212120")
    label2b.place(x=245,y=125)
    h1b = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    h1b.place(x=350,y=125)
    hh1b = json_data['list'][1]['main']['humidity']
    h1b.config(text=(hh1b,"%"))

    label3b = Label(top,text = "Pressure",font=('Helvetica',11),fg="white",bg="#212120")
    label3b.place(x=245,y=150)
    p1b = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    p1b.place(x=350,y=155)
    pp1b = json_data['list'][1]['main']['pressure']
    p1b.config(text=(pp1b,"hPa"))

    label4b = Label(top,text = "Wind Speed",font=('Helvetica',11),fg="white",bg="#212120")
    label4b.place(x=245,y=175)
    w1b = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    w1b.place(x=350,y=175)
    ww1b = json_data['list'][1]['wind']['speed']
    w1b.config(text=(ww1b,"m/s"))

    label5b = Label(top,text = "Description",font=('Helvetica',11),fg="white",bg="#212120")
    label5b.place(x=245,y=200)
    ds1b = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    ds1b.place(x=350,y=200)
    dds1b = json_data['list'][1]['weather'][0]['description']
    ds1b.config(text=(dds1b))

    #box3
    label1c = Label(top,text = "Temperature",font=('Helvetica',11),fg="white",bg="#212120")
    label1c.place(x=470,y=100)
    t1c = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    t1c.place(x=575,y=100)
    tt1c = json_data['list'][2]['main']['temp']
    t1c.config(text=(tt1c,"°C"))

    label2c = Label(top,text = "Humidity",font=('Helvetica',11),fg="white",bg="#212120")
    label2c.place(x=470,y=125)
    h1c = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    h1c.place(x=575,y=125)
    hh1c = json_data['list'][2]['main']['humidity']
    h1c.config(text=(hh1c,"%"))

    label3c = Label(top,text = "Pressure",font=('Helvetica',11),fg="white",bg="#212120")
    label3c.place(x=470,y=150)
    p1c = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    p1c.place(x=575,y=150)
    pp1c = json_data['list'][2]['main']['pressure']
    p1a.config(text=(pp1c,"hPa"))

    label4c = Label(top,text = "Wind Speed",font=('Helvetica',11),fg="white",bg="#212120")
    label4c.place(x=470,y=175)
    w1c = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    w1c.place(x=575,y=175)
    ww1c = json_data['list'][2]['wind']['speed']
    w1c.config(text=(ww1c,"m/s"))

    label5c = Label(top,text = "Description",font=('Helvetica',11),fg="white",bg="#212120")
    label5c.place(x=470,y=200)
    ds1c = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    ds1c.place(x=575,y=200)
    dds1c = json_data['list'][2]['weather'][0]['description']
    ds1c.config(text=(dds1c))

    #box4
    label1d = Label(top,text = "Temperature",font=('Helvetica',11),fg="white",bg="#212120")
    label1d.place(x=697,y=100)
    t1d = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    t1d.place(x=802,y=100)
    tt1d = json_data['list'][3]['main']['temp']
    t1d.config(text=(tt1d,"°C"))

    label2d = Label(top,text = "Humidity",font=('Helvetica',11),fg="white",bg="#212120")
    label2d.place(x=697,y=125)
    h1d = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    h1d.place(x=802,y=125)
    hh1d = json_data['list'][3]['main']['humidity']
    h1d.config(text=(hh1d,"%"))

    label3d = Label(top,text = "Pressure",font=('Helvetica',11),fg="white",bg="#212120")
    label3d.place(x=697,y=150)
    p1d = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    p1d.place(x=802,y=155)
    pp1d = json_data['list'][3]['main']['pressure']
    p1d.config(text=(pp1d,"hPa"))

    label4d = Label(top,text = "Wind Speed",font=('Helvetica',11),fg="white",bg="#212120")
    label4d.place(x=697,y=175)
    w1d = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    w1d.place(x=802,y=175)
    ww1d = json_data['list'][3]['wind']['speed']
    w1d.config(text=(ww1d,"m/s"))

    label5d = Label(top,text = "Description",font=('Helvetica',11),fg="white",bg="#212120")
    label5d.place(x=697,y=200)
    ds1d = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    ds1d.place(x=802,y=200)
    dds1d = json_data['list'][3]['weather'][0]['description']
    ds1d.config(text=(dds1d))

    #box5
    label1e = Label(top,text = "Temperature",font=('Helvetica',11),fg="white",bg="#212120")
    label1e.place(x=25,y=310)
    t1e = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    t1e.place(x=130,y=310)
    tt1e = json_data['list'][4]['main']['temp']
    t1e.config(text=(tt1e,"°C"))

    label2e = Label(top,text = "Humidity",font=('Helvetica',11),fg="white",bg="#212120")
    label2e.place(x=25,y=335)
    h1e = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    h1e.place(x=130,y=335)
    hh1e = json_data['list'][4]['main']['humidity']
    h1e.config(text=(hh1e,"%"))

    label3e = Label(top,text = "Pressure",font=('Helvetica',11),fg="white",bg="#212120")
    label3e.place(x=25,y=360)
    p1e = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    p1e.place(x=130,y=360)
    pp1e = json_data['list'][4]['main']['pressure']
    p1e.config(text=(pp1e,"hPa"))

    label4e = Label(top,text = "Wind Speed",font=('Helvetica',11),fg="white",bg="#212120")
    label4e.place(x=25,y=385)
    w1e = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    w1e.place(x=130,y=385)
    ww1e = json_data['list'][4]['wind']['speed']
    w1e.config(text=(ww1e,"m/s"))

    label5e = Label(top,text = "Description",font=('Helvetica',11),fg="white",bg="#212120")
    label5e.place(x=25,y=410)
    ds1e = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    ds1e.place(x=130,y=410)
    dds1e = json_data['list'][4]['weather'][0]['description']
    ds1e.config(text=(dds1e))

    #box6
    label1f = Label(top,text = "Temperature",font=('Helvetica',11),fg="white",bg="#212120")
    label1f.place(x=245,y=310)
    t1f = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    t1f.place(x=350,y=310)
    tt1f = json_data['list'][5]['main']['temp']
    t1f.config(text=(tt1f,"°C"))

    label2f = Label(top,text = "Humidity",font=('Helvetica',11),fg="white",bg="#212120")
    label2f.place(x=245,y=335)
    h1f = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    h1f.place(x=350,y=335)
    hh1f = json_data['list'][5]['main']['humidity']
    h1f.config(text=(hh1f,"%"))

    label3f = Label(top,text = "Pressure",font=('Helvetica',11),fg="white",bg="#212120")
    label3f.place(x=245,y=360)
    p1f = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    p1f.place(x=350,y=360)
    pp1f = json_data['list'][5]['main']['pressure']
    p1f.config(text=(pp1f,"hPa"))

    label4f = Label(top,text = "Wind Speed",font=('Helvetica',11),fg="white",bg="#212120")
    label4f.place(x=245,y=385)
    w1f = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    w1f.place(x=350,y=385)
    ww1f = json_data['list'][5]['wind']['speed']
    w1f.config(text=(ww1f,"m/s"))

    label5f = Label(top,text = "Description",font=('Helvetica',11),fg="white",bg="#212120")
    label5f.place(x=245,y=410)
    ds1f = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    ds1f.place(x=350,y=410)
    dds1f = json_data['list'][5]['weather'][0]['description']
    ds1f.config(text=(dds1f))

    #box7
    label1g = Label(top,text = "Temperature",font=('Helvetica',11),fg="white",bg="#212120")
    label1g.place(x=470,y=310)
    t1g = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    t1g.place(x=575,y=310)
    tt1g = json_data['list'][6]['main']['temp']
    t1g.config(text=(tt1g,"°C"))

    label2g = Label(top,text = "Humidity",font=('Helvetica',11),fg="white",bg="#212120")
    label2g.place(x=470,y=335)
    h1g = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    h1g.place(x=575,y=335)
    hh1g = json_data['list'][6]['main']['humidity']
    h1g.config(text=(hh1g,"%"))

    label3g = Label(top,text = "Pressure",font=('Helvetica',11),fg="white",bg="#212120")
    label3g.place(x=470,y=360)
    p1g = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    p1g.place(x=575,y=360)
    pp1g = json_data['list'][6]['main']['pressure']
    p1g.config(text=(pp1g,"hPa"))

    label4g = Label(top,text = "Wind Speed",font=('Helvetica',11),fg="white",bg="#212120")
    label4g.place(x=470,y=385)
    w1g = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    w1g.place(x=575,y=385)
    ww1g = json_data['list'][6]['wind']['speed']
    w1g.config(text=(ww1g,"m/s"))

    label5g = Label(top,text = "Description",font=('Helvetica',11),fg="white",bg="#212120")
    label5g.place(x=470,y=410)
    ds1g = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    ds1g.place(x=575,y=410)
    dds1g = json_data['list'][6]['weather'][0]['description']
    ds1g.config(text=(dds1g))

    #box8
    label1h = Label(top,text = "Temperature",font=('Helvetica',11),fg="white",bg="#212120")
    label1h.place(x=697,y=310)
    t1h = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    t1h.place(x=802,y=310)
    tt1h = json_data['list'][7]['main']['temp']
    t1h.config(text=(tt1h,"°C"))

    label2h = Label(top,text = "Humidity",font=('Helvetica',11),fg="white",bg="#212120")
    label2h.place(x=697,y=335)
    h1h = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    h1h.place(x=802,y=335)
    hh1h = json_data['list'][7]['main']['humidity']
    h1h.config(text=(hh1h,"%"))

    label3h = Label(top,text = "Pressure",font=('Helvetica',11),fg="white",bg="#212120")
    label3h.place(x=697,y=360)
    p1h = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    p1h.place(x=802,y=360)
    pp1h = json_data['list'][7]['main']['pressure']
    p1h.config(text=(pp1h,"hPa"))

    label4h = Label(top,text = "Wind Speed",font=('Helvetica',11),fg="white",bg="#212120")
    label4h.place(x=697,y=385)
    w1h = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    w1h.place(x=802,y=385)
    ww1h = json_data['list'][7]['wind']['speed']
    w1h.config(text=(ww1h,"m/s"))

    label5h = Label(top,text = "Description",font=('Helvetica',11),fg="white",bg="#212120")
    label5h.place(x=697,y=410)
    ds1h = Label(top,font=("Helvetica",11),fg="white",bg="#212120")
    ds1h.place(x=802,y=410)
    dds1h = json_data['list'][7]['weather'][0]['description']
    ds1h.config(text=(dds1h))
####################################################################################################################################################################################
def getWeather():
    city=textfield.get()

    ##weather
    api = "https://api.openweathermap.org/data/2.5/forecast?q="+city+"&units=metric&appid=f778015abc2d6cecf62baa9b62848035"
    json_data = requests.get(api).json()

    if(json_data["message"] != "city not found") :
        geolocator= Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)

        #current
        temp = json_data['list'][0]['main']['temp']    
        humidity = json_data['list'][0]['main']['humidity']
        pressure = json_data['list'][0]['main']['pressure']
        wind = json_data['list'][0]['wind']['speed']
        description = json_data['list'][0]['weather'][0]['description']

        t.config(text=(temp,"°C"))
        h.config(text=(humidity,"%"))
        p.config(text=(pressure,"hPa"))
        w.config(text=(wind,"m/s"))
        d.config(text=description)

        #first cell
        firstdayimage = json_data['list'][0]['weather'][0]['icon']
        photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
        firstimage.config(image=photo1)
        firstimage.image=photo1
        tempday1 = json_data['list'][0]['main']['temp_max']
        tempnight1 = json_data['list'][0]['main']['temp_min']
        day1temp.config(text=f"Max : {tempday1} °C\nMin : {tempnight1} °C")    
        
        #second cell
        seconddayimage = json_data['list'][8]['weather'][0]['icon']
        img = (Image.open(f"icon/{seconddayimage}@2x.png"))
        resized_image = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_image)
        secondimage.config(image=photo2)
        secondimage.image = photo2
        tempday2 = json_data['list'][8]['main']['temp_max']
        tempnight2 = json_data['list'][8]['main']['temp_min']
        day2temp.config(text=f"Max : {tempday2} °C\nMin : {tempnight2} °C")
       
        #third cell
        thirddayimage = json_data['list'][16]['weather'][0]['icon']
        img = (Image.open(f"icon/{thirddayimage}@2x.png"))
        resized_image = img.resize((50,50))
        photo3 = ImageTk.PhotoImage(resized_image)
        thirdimage.config(image=photo3)
        thirdimage.image = photo3
        tempday3 = json_data['list'][16]['main']['temp_max']
        tempnight3 = json_data['list'][16]['main']['temp_min']
        day3temp.config(text=f"Max : {tempday3} °C\nMin : {tempnight3} °C")
       

        #fourth cell
        fourthdayimage = json_data['list'][24]['weather'][0]['icon']
        img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
        resized_image = img.resize((50,50))
        photo4 = ImageTk.PhotoImage(resized_image)
        fourthimage.config(image=photo4)
        fourthimage.image = photo4
        tempday4 = json_data['list'][24]['main']['temp_max']
        tempnight4 = json_data['list'][24]['main']['temp_min']
        day4temp.config(text=f"Max : {tempday4} °C\nMin : {tempnight4} °C")
        
        #fifth cell
        fifthdayimage = json_data['list'][32]['weather'][0]['icon']
        img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
        resized_image = img.resize((50,50))
        photo5 = ImageTk.PhotoImage(resized_image)
        fifthimage.config(image=photo5)
        fifthimage.image = photo5
        tempday5 = json_data['list'][32]['main']['temp_max']
        tempnight5 = json_data['list'][32]['main']['temp_min']
        day5temp.config(text=f"Max : {tempday5} °C\nMin : {tempnight5} °C")

        #days
        first = datetime.now()
        day1.config(text=first.strftime("%A"))
        second = first+timedelta(days=1)
        day2.config(text=second.strftime("%A"))
        third = first+timedelta(days=2)
        day3.config(text=third.strftime("%A"))
        fourth = first+timedelta(days=3)
        day4.config(text=fourth.strftime("%A"))
        fifth = first+timedelta(days=4)
        day5.config(text=fifth.strftime("%A"))

        infobtn = tk.Button(root,text = "Get Detailed Updates",font=('Helvetica',11),fg="white",bg="#203243",width=22,command=lambda: moreInfo(city))   #####################
        infobtn.place(x=45,y=235)

    else :
        messagebox.showerror("Invalid","Invalid location!!")
###########################################################################################################################################################################
##icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)

#label
label1 = Label(root,text = "Temperature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=120)
label2 = Label(root,text = "Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=140)
label3 = Label(root,text = "Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=160)
label4 = Label(root,text = "Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=180)
label5 = Label(root,text = "Description",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=50,y=200)

##search box
Search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image = PhotoImage(file="Images/Layer 7.png")
weatherimage = Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield = tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon = PhotoImage(file="Images/Layer 6.png")
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)

##Bottom main box
frame = Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

##bottom boxes
firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=450,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=750,y=30)

#clock (here we place time)
clock = Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone = Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat = Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)

#thpwd
t = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=150,y=120)
h = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)
p = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)
w = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)
d = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)

##first cell
firstframe = Frame(root,width=240,height=132,bg="#282829")
firstframe.place(x=35,y=315)
day1 = Label(firstframe,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=100,y=5)
firstimage = Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)
day1temp = Label(firstframe,bg="#282829",fg="#57adff",font="arial 15 bold")
day1temp.place(x=100,y=50)

#second cell
secondframe = Frame(root,width=114,height=115,bg="#282829")
secondframe.place(x=305,y=325)
day2 = Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10,y=5)
secondimage = Label(secondframe,bg="#282829")
secondimage.place(x=7,y=23)
day2temp = Label(secondframe,bg="#282829",fg="#fff")
day2temp.place(x=2,y=70)
    
#third cell
thirdframe = Frame(root,width=114,height=115,bg="#282829")
thirdframe.place(x=455,y=325)
day3 = Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=10,y=5)
thirdimage = Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=23)
day3temp = Label(thirdframe,bg="#282829",fg="#fff")
day3temp.place(x=2,y=70)

#fourth cell
fourthframe = Frame(root,width=114,height=115,bg="#282829")
fourthframe.place(x=605,y=325)
day4 = Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=10,y=5)
fourthimage = Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=23)
day4temp = Label(fourthframe,bg="#282829",fg="#fff")
day4temp.place(x=2,y=70)

#fifth cell
fifthframe = Frame(root,width=114,height=115,bg="#282829")
fifthframe.place(x=755,y=325)
day5 = Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=10,y=5)
fifthimage = Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=23)
day5temp = Label(fifthframe,bg="#282829",fg="#fff")
day5temp.place(x=2,y=70)

root.mainloop()
