from bs4 import BeautifulSoup
import requests
import tkinter as tk

root = tk.Tk()
root.geometry("320x280")
root.title("Weather App")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Function to get the weather
def weather():
    city=input_city.get()
    city=city+"+weather"
    
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching in google......\n")
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()  
    time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    
    city_label.config(text=location)
    day_label.config(text=time) 
    condition_label.config(text=info) 
    temp_label.config(text=weather+"°C") 

# GUI
input_city = tk.StringVar()
enter_label = tk.Label(root, text="Enter city", font=("Poppins", 14))
enter_label.place(x=20, y= 20)
enter_input = tk.Entry(root, textvariable=input_city, font=("Poppins", 14), width=15)
enter_input.place(x=130, y= 20)
enter_button = tk.Button(root, text="Enter", command=weather,font=("Poppins", 12), width=10)
enter_button.place(x=110, y= 60)

city_label = tk.Label(root, text="",font=("Poppins", 14))
city_label.place(x=100, y= 120)
day_label = tk.Label(root, text="",font=("Poppins", 14))
day_label.place(x=100, y= 150)
condition_label = tk.Label(root, text="",font=("Poppins", 14))
condition_label.place(x=100, y= 180)
temp_label = tk.Label(root, text="",font=("Poppins", 14))
temp_label.place(x=100, y= 210)


root.mainloop()