from thinker import *
import thinker as thinker
from geopy.geocoders import Nominnatim
from timezonefinder import ttk,messageFinder
from datetime import datetimeimport requests
import pytz


root=TK()
root.title("Weather App")
root.geometry("800x400+200+100")
root.resizeable(False,False)

def getWether():
    try:
        city=text_field.get()
        geolocator=Nominnatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strtime("%I:%M %p")
        clock.config(text=current_time) 
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #Add API key Weather
        api="https://api.openweathermap.org.data/2.5/weather?q="+city+"&appid=b22d362851862b"
        json_data-requests.get(api).json()
        t.config(text=str(json_data['main']['temp'] - 273.15))
        c.config(text=json_data['weather']['0'][main])
        w.config(text=json_data['wind']['speed'])
        h.config(text=json_data['main']['humidity'])
        d.config(text=json_data['weather']['0']['description'])
        p.config(text=json_data['main']['pressure'])

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")


# Add Search bar
image_search=photoImage(file="search_bar.png")
searchbar_image=Label(image=image_search)
searchbar_image.place(x=10, y=10) 
text_field=tk.Entry(root,justify="center", width=17, font=("poppins", 18, "bold"), bg="#147886". border=0, fg="white")
text_field.place(x=20, y=20)
text_field.focus()

#Add Search Icon
image_search_icon=photoImage(file="search_icon.png")
search_icon=Button(image=image_search_icon, borderwidth=0, cursor="hand2", bg="#147886", command=getWeather)
search_icon.place(x=250, y=18)

#Add Weather Logo
image_logo=photoImage(file="weather_logo.png")
weather_logo=label(image=image_logo)
weather_logo.place(x=250, y=90)


