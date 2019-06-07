import requests 
import sys
import json

key = "442a7e4ea01d3f922fd8b631a86ee5a5"


with open("city.list.json")as f:
    cities = json.load(f)
    
class city:
    cities = cities 
    
    def __init__(self,name,cid, country="GB"):
        name = name.lower()
        self.call = 'placeholder'
        self.name = name[0].upper() + name[1:]

        self.country = country 
    
        def get_id(self): 
            if cities['country'] == self.country:  
                if cities['name'] == self.name: 
                    self.cid = cities['id']
            else: 
                self.id = None 
    
    def make_call(self, call_type): 
        if call_type =="weather": 
            call = "http://api.openweathermap.org/data/2.5/weather?id={self.cid}&APPID={key}&units=metric"
        elif call_type== "forecast": 
            call = "http://api.openweathermap.org/data/2.5/forecast?id={self.cid}&APPID={key}&units=metric"




                
def generate_api_call(report_type, cid, country="GB"): 
    call = f"http://api.openweathermap.org/data/2.5/{report_type}?id={cid}&APPID={key}&units=metric"
    return(call)

        

def download_city_ids():
    address = "http://bulk.openweathermap.org/sample/city.list.json.gz"
    response = requests.get(address)

##redo this function so that it has proper capitalisation for multi-word city names
def clean_input(city_name, county = "GB"): 
    city_name = city_name.lower()
    city_name = city_name[0].upper() + city_name[1:]

    return city_name


def find_id(name, country = "GB"): 
    for d in cities: 
        if d["country"] == country:
            if d["name"].lower() == name.lower(): 
                return d["id"]
    raise Exception("Could not find data for the provided city.")


def make_call(call): 
    try:
        response = requests.get(call)
    except: 
        print("Error making API call")
        return -1
    else:
        text = json.loads(response.text)
        return text

def report_current_weather(report, city): 
    description = report["weather"][0]["description"]
    main = report["main"]
    print(f"\nWeather report for {city}: \n\tThe current weather in {city} is: {description}")
    
    print(f"\tCurrent temperature: {main['temp']}\n" + 
            f"\tPredicted peak temperature: {main['temp_max']}\n" + 
            f"\tPredicted minimum temperature: {main['temp_min']}\n" +
            f"\tHumidity: {main['humidity']}%")

def detailed_report(city, weather):
    print(f"Detailed weather report for {city}: ")


def report_forecast(city): 
    cid = find_id(city)
    report = make_call(generate_api_call("forecast", cid))
    print(report['list'][0]['main'])


            

#print("testingi nititated")
#testing_city = "ely"
#
#test_id = find_id(testing_city)
#testing_call = generate_api_call("forecast", test_id)
#response = make_call(testing_call)
#
#print(response)



city_selected = False
print("Openweather app initiated.\n")

while True: 
    if city_selected == False: 
        city = input("Please input a city name that you would like to test: ")
    else:
        city_selected = False
        city = clean_input(city)
    try:
            cid = find_id(city)

    except: 
        print(f"No city called ' {city} ' found in database. Please ensure spelling is correct.")
        continue 
    else: 
        call =f"http://api.openweathermap.org/data/2.5/weather?id={cid}&APPID={key}&units=metric"
        report = make_call(call)
        report_current_weather(report, city)

        x =input("Press 1 to see the forecast for the week.\nPress 2 to see a more detailed forecast." + 
            "To see current weather in another city please input city name: ")
        
        try: 
            y = int(x)
        except: 
            city = clean_input(x)
            city_selected = True
            print("\nCity entered.\n")
            continue
        else:
           if y == 1: 
               report_forecast(city)
           elif y == -1: 
               sys.exit()
            
           else: 
               print("More details requested. Please wait.")
               break

        
        
        
        


