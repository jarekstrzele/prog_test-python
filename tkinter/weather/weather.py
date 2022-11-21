from tkinter import *
import requests

# Define window
root=Tk()
root.title("Weather Forecast")
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0,0)


# define fonts and colors
sky_color = '#76c3ef'
grass_color = '#aad207'
output_color = '#dcf0fb'
input_color = '#ecf2ae'
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)

# define functions
def search():
    """Use open weather api to look up current weather conditions given a city, country"""
    global response

    # get API repsonse
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = 'dda71caf405d01b0091c6ff97588f0b0'

    # search by the appropriate query, either city name ot zip
    if search_method.get() == 1:
        querystring = {'q':city_entry.get(), 'appid':api_key}
    elif search_method.get() == 2:
        querystring = {'zip':city_entry.get(), 'appid':api_key}

    # call API
    response = requests.request("GET", url, params=querystring)
    response = response.json()
    print(response)

    # example response return
    '''{'coord': {'lon': -71.0598, 'lat': 42.3584}, 'weather': 
    [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 
    'base': 'stations', 'main': {'temp': 275.22, 'feels_like': 269.43, 'temp_min': 273.76, 'temp_max': 276.36,
    'pressure': 1023, 'humidity': 54}, 'visibility': 10000, 'wind': {'speed': 8.23, 'deg': 210},
    'clouds': {'all': 40}, 'dt': 1669067304, 'sys': {'type': 2, 'id': 2013408, 'country': 'US',
    'sunrise': 1669030951, 'sunset': 1669065484}, 'timezone': -18000, 'id': 4930956, 
    'name': 'Boston', 'cod': 200}'''

    get_weather()



def get_weather():
    """GRab info from API response and update out weather lables."""
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])

    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']
    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    # Update labels
    city_info_lbl.config(text=f'{city_name} ( {city_lat}, {city_lon} ', font=large_font, bg=output_color )
    weather_lbl.config(text="Weather: " + main_weather + ", " + description, font=small_font, bg=output_color)
    temp_lbl.config(text=f"Temperature: {temp} F", font=small_font, bg=output_color)
    feels_lbl.config(text=f"Feels like: {feels_like} F", font=small_font, bg=output_color)
    temp_min_lbl.config(text=f"Min temp: {temp_min} F", font=small_font, bg=output_color)
    temp_max_lbl.config(text=f"Max temp: {temp_max} F", font=small_font, bg=output_color)
    humidity_lbl.config(text=f"Humidity: {humidity}", font=small_font, bg=output_color)


# define layout
# create frames
sky_frame = Frame(root, bg=sky_color, height=250)
grass_frame = Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)

# Output frame layout
city_info_lbl = Label(output_frame, bg=output_color, text="Testing city")
weather_lbl = Label(output_frame, bg=output_color, text="Testing weather")
temp_lbl = Label(output_frame, bg=output_color, text="Testing temp")
feels_lbl = Label(output_frame, bg=output_color, text="Testing feels")
temp_min_lbl = Label(output_frame, bg=output_color, text="Testing min ")
temp_max_lbl = Label(output_frame, bg=output_color, text="Testing  max ")
humidity_lbl = Label(output_frame, bg=output_color, text="Testing humi ")
photo_lbl = Label(output_frame, bg=output_color, text="Testing photo")

city_info_lbl.pack(pady=8)
weather_lbl.pack()
temp_lbl.pack()
feels_lbl.pack()
temp_min_lbl.pack()
temp_max_lbl.pack()
humidity_lbl.pack()
photo_lbl.pack(pady=8)

# input frame laout
#create  input frame bts and entry
city_entry = Entry(input_frame, width=20, font=large_font)
submit_btn = Button(input_frame, text="Submit", font=large_font, bg=input_color, command=search)

search_method = IntVar()
search_method.set(1)
search_city = Radiobutton(input_frame, text='Search by city name', variable=search_method, value=1, font=small_font,bg=input_color)
search_zip = Radiobutton(input_frame, text='Search by zipcode', variable=search_method, value=2, font=small_font, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10,0))
submit_btn.grid(row=0, column=1, padx=10, pady=(10,0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, padx=(0,10), pady=2)




root.mainloop()
