import sys
import requests
import ast

def main(args):

    #Declare variables
    output = ""
    lat = args[1]
    long = str(float(args[2]) * -1)
    key = "*****"

    #Primary program logic
    try:
        #Get data in json format and catch invalid location error
        data = get_weather(lat, long, key)        
        return_output(data)       
    except Exception as e:
        #return_error(str(e))
        raise e

def get_weather(lat, long, key):

    request = "http://api.weatherbit.io/v2.0/current?units=I&lat=" + lat + "&lon=" + long + "&key=" + key;
    response = requests.get(request)
    data = str(response.content)[11 : len(str(response.content)) - 15]
    return ast.literal_eval(data)

def return_error(text):

    output = "<h3>Server Error</h3>"
    output += "<p>Error: " + text + "</p>"
    print(output)

def get_image(code):

    output = "clear-day"

    if(code[3 : 4] == "d"):
        output = "partly-cloudy-day"
    else:
        output = "partly-cloudy-night"
        
    if(code == "c01d"):
        output = "clear-day"
    elif(code == "c01n"):
        output = "clear-night"
    elif(code[0 : 3] == "c04"):
        output = "cloudy"
    elif(code[0 : 3] == "a05"):
        output = "fog"
    elif(code == "c02d" or code == "c03d"):
        output = "partly-cloudy-day"
    elif(code == "c02n" or code == "c03n"):
        output = "partly-cloudy-night"
    elif((["d01", "d02", "d03", "r01", "r02", "r03", "f01", "r04", "r05", "r06"].count(code[0 : 3])) > 0):
        output = "rain"
    elif(code[0 : 3] == "s05"):
        output = "sleet"
    elif(code[0 : 3] == "s01" or code[0 : 3] == "s02" or code[0 : 3] == "s06"):
        output = "snow"

    return output

def return_output(data):

    #Parse weather information
    icon = "images/weather/" + get_image(str(data["weather"]["icon"])) + ".svg"
    summary = str(data["weather"]["description"])    
    pressure = str(data["slp"])
    temperature = str(data["temp"])
    humidity = str(data["rh"])
    windspeed = str(data["wind_spd"])
    direction = str(data["wind_dir"])
    city = str(data["city_name"])

    output = "<table>"
    output += "<tr>"
    
    output += "<td>"
    output += "<img src='" + icon + "' height='250' width='250' />"
    output += "<h3 class='dynamicWeatherH3'>" + summary + "</h3>"    
    output += "</td>"

    output += "<td class='dynamicWeatherTD'>"
    output += "<canvas class='dynamicWeatherCANVAS' id='dynamicWeatherTemperature' width='300' height='300'></canvas>"  
    output += "<h3 class='dynamicWeatherH3'>Temperature</h3>"
    output += "</td>"

    output += "<td class='dynamicWeatherTD'>"
    output += "<canvas class='dynamicWeatherCANVAS' id='dynamicWeatherWindSpeed' width='300' height='300'></canvas>"  
    output += "<h3 class='dynamicWeatherH3'>Wind Speed</h3>"
    output += "</td>"
    
    output += "</tr>"    
    output += "<tr>"
        
    output += "<td class='dynamicWeatherTD'>"
    output += "<canvas class='dynamicWeatherCANVAS' id='dynamicWeatherHumidity' width='300' height='300'></canvas>"  
    output += "<h3 class='dynamicWeatherH3'>Humidity</h3>"
    output += "</td>"

    output += "<td class='dynamicWeatherTD'>"
    output += "<canvas class='dynamicWeatherCANVAS' id='dynamicWeatherAirPressure' width='300' height='300'></canvas>"  
    output += "<h3 class='dynamicWeatherH3'>Air Pressure</h3>"
    output += "</td>"

    output += "<td class='dynamicWeatherTD'>"
    output += "<canvas class='dynamicWeatherCANVAS' id='dynamicWeatherWindDirection' width='300' height='300'></canvas>"  
    output += "<h3 class='dynamicWeatherH3'>Wind Direction</h3>"
    output += "</td>"

    output += "</tr>"
    output += "</table>"    
    output += "<style>" + build_styling() + "</style>"
    output += "<script>" + build_javascript(temperature, windspeed, humidity, pressure, direction) + "</script>"
    output += "<p>Powered by <a href='https://www.weatherbit.io/'>Weatherbit</a>, images from <a href='https://www.flaticon.com/categories/weather'>FlatIcon.com</a>, City: " + city + "</p>"
    output += ""
        
    print(output)  

def build_javascript(temp, speed, hum, pres, dir):

    #Draw the temperature guage
    output = "var cvTemperature = document.getElementById('dynamicWeatherTemperature');"
    output += "var ctxTemperature = cvTemperature.getContext('2d');"
    output += "ctxTemperature.beginPath();"
    output += "ctxTemperature.arc(150, 150, 140, 0, 2 * Math.PI);"
    output += "ctxTemperature.fillStyle = 'black';"
    output += "ctxTemperature.stroke();"
    output += "ctxTemperature.beginPath();"
    output += "ctxTemperature.arc(150, 150, 10, 0, 2 * Math.PI);"
    output += "ctxTemperature.fillStyle = 'black';"
    output += "ctxTemperature.fill();"
    output += "ctxTemperature.font = 'bold 20px Arial';"
    output += "ctxTemperature.fillStyle = 'black';"
    output += "ctxTemperature.fillText('-30', 64, 260);"
    output += "ctxTemperature.fillText('-20', 39, 231);"
    output += "ctxTemperature.fillText('-10', 20, 198);"
    output += "ctxTemperature.fillText('0', 14, 158);"
    output += "ctxTemperature.fillText('10', 20, 118);"
    output += "ctxTemperature.fillText('20', 39, 85);"
    output += "ctxTemperature.fillText('30', 64, 57);"
    output += "ctxTemperature.fillText('40', 100, 37);"   
    output += "ctxTemperature.fillText('50', 141, 30);"
    output += "ctxTemperature.fillText('130', 200, 260);"
    output += "ctxTemperature.fillText('120', 227, 231);"
    output += "ctxTemperature.fillText('110', 247, 198);"
    output += "ctxTemperature.fillText('100', 254, 158);"
    output += "ctxTemperature.fillText('90', 256, 118);"
    output += "ctxTemperature.fillText('80', 240, 85);"
    output += "ctxTemperature.fillText('70', 213, 57);"
    output += "ctxTemperature.fillText('60', 178, 37);"
    output += "var value = (1.8 * " + temp + " + 135);"
    output += "ctxTemperature.beginPath();"
    output += "ctxTemperature.lineWidth = 5;"
    output += "ctxTemperature.translate(150, 150);"
    output += "ctxTemperature.strokeStyle = 'black';"
    output += "ctxTemperature.rotate(value * (Math.PI / 180));"
    output += "ctxTemperature.moveTo(0, 0);"
    output += "var length = 90;"
    output += "ctxTemperature.lineTo(length, length);"
    output += "ctxTemperature.stroke();"

    #Draw the humidity guage
    output += "var cvHumidity = document.getElementById('dynamicWeatherHumidity');"
    output += "var ctxHumidity = cvHumidity.getContext('2d');"
    output += "ctxHumidity.beginPath();"
    output += "ctxHumidity.arc(150, 150, 140, 0, 2 * Math.PI);"
    output += "ctxHumidity.fillStyle = 'black';"
    output += "ctxHumidity.stroke();"
    output += "ctxHumidity.beginPath();"
    output += "ctxHumidity.arc(150, 150, 10, 0, 2 * Math.PI);"
    output += "ctxHumidity.fillStyle = 'black';"
    output += "ctxHumidity.fill();"
    output += "ctxHumidity.font = 'bold 20px Arial';"
    output += "ctxHumidity.fillStyle = 'black';"
    output += "ctxHumidity.fillText('0', 71, 262);"
    output += "ctxHumidity.fillText('10', 24, 212);"
    output += "ctxHumidity.fillText('20', 13, 150);"
    output += "ctxHumidity.fillText('30', 33, 91);"
    output += "ctxHumidity.fillText('40', 78, 45);"
    output += "ctxHumidity.fillText('50', 139, 29);"
    output += "ctxHumidity.fillText('60', 200, 47);"
    output += "ctxHumidity.fillText('70', 246, 93);"
    output += "ctxHumidity.fillText('80', 263, 149);"
    output += "ctxHumidity.fillText('90', 250, 212);"
    output += "ctxHumidity.fillText('100', 200, 262);"
    output += "value = (2.93 * " + hum + " + 78.5);"    
    output += "ctxHumidity.beginPath();"
    output += "ctxHumidity.lineWidth = 5;"       
    output += "ctxHumidity.translate(150, 150); "  
    output += "ctxHumidity.strokeStyle = 'black';"
    output += "ctxHumidity.rotate(value * (Math.PI / 180));"    
    output += "ctxHumidity.moveTo(0, 0);"    
    output += "ctxHumidity.lineTo(length, length);"    
    output += "ctxHumidity.stroke();"

    #Draw the wind speed guage
    output += "var cvWindSpeed = document.getElementById('dynamicWeatherWindSpeed');"
    output += "var ctxWindSpeed = cvWindSpeed.getContext('2d');"
    output += "ctxWindSpeed.beginPath();"
    output += "ctxWindSpeed.arc(150, 150, 140, 0, 2 * Math.PI);"
    output += "ctxWindSpeed.fillStyle = 'black';"
    output += "ctxWindSpeed.stroke();"
    output += "ctxWindSpeed.beginPath();"
    output += "ctxWindSpeed.arc(150, 150, 10, 0, 2 * Math.PI);"
    output += "ctxWindSpeed.fillStyle = 'black';"
    output += "ctxWindSpeed.fill();"
    output += "ctxWindSpeed.font = 'bold 20px Arial';"
    output += "ctxWindSpeed.fillStyle = 'black';"
    output += "ctxWindSpeed.fillText('0', 71, 262);"
    output += "ctxWindSpeed.fillText('5', 30, 216);"
    output += "ctxWindSpeed.fillText('10', 13, 153);"
    output += "ctxWindSpeed.fillText('15', 33, 91);"
    output += "ctxWindSpeed.fillText('20', 78, 45);"
    output += "ctxWindSpeed.fillText('25', 139, 29);"
    output += "ctxWindSpeed.fillText('30', 200, 47);"
    output += "ctxWindSpeed.fillText('35', 245, 88);"
    output += "ctxWindSpeed.fillText('40', 263, 149);"
    output += "ctxWindSpeed.fillText('45', 250, 212);"
    output += "ctxWindSpeed.fillText('50', 207, 262);"
    output += "value = (5.86 * " + speed + " + 78.5);"    
    output += "ctxWindSpeed.beginPath();"
    output += "ctxWindSpeed.lineWidth = 5;"       
    output += "ctxWindSpeed.translate(150, 150); "  
    output += "ctxWindSpeed.strokeStyle = 'black';"
    output += "ctxWindSpeed.rotate(value * (Math.PI / 180));"    
    output += "ctxWindSpeed.moveTo(0, 0);"    
    output += "ctxWindSpeed.lineTo(length, length);"    
    output += "ctxWindSpeed.stroke();"

    #Draw the air pressure guage
    output += "var cvAirPressure = document.getElementById('dynamicWeatherAirPressure');"
    output += "var ctxAirPressure = cvAirPressure.getContext('2d');"
    output += "ctxAirPressure.beginPath();"
    output += "ctxAirPressure.arc(150, 150, 140, 0, 2 * Math.PI);"
    output += "ctxAirPressure.fillStyle = 'black';"
    output += "ctxAirPressure.stroke();"
    output += "ctxAirPressure.beginPath();"
    output += "ctxAirPressure.arc(150, 150, 10, 0, 2 * Math.PI);"
    output += "ctxAirPressure.fillStyle = 'black';"
    output += "ctxAirPressure.fill();"
    output += "ctxAirPressure.font = 'bold 20px Arial';"
    output += "ctxAirPressure.fillStyle = 'black';"
    output += "ctxAirPressure.fillText('960', 71, 262);"
    output += "ctxAirPressure.fillText('970', 27, 213);"
    output += "ctxAirPressure.fillText('980', 13, 150);"
    output += "ctxAirPressure.fillText('990', 39, 86);"
    output += "ctxAirPressure.fillText('1000', 78, 45);"
    output += "ctxAirPressure.fillText('1010', 142, 35);"
    output += "ctxAirPressure.fillText('1020', 200, 63);"
    output += "ctxAirPressure.fillText('1030', 234, 117);"
    output += "ctxAirPressure.fillText('1040', 241, 177);"
    output += "ctxAirPressure.fillText('1050', 214, 235);"
    output += "ctxAirPressure.fillText('1060', 162, 275);"
    output += "value = (3.102 * " + pres + " - 20);"    
    output += "ctxAirPressure.beginPath();"
    output += "ctxAirPressure.lineWidth = 5;"       
    output += "ctxAirPressure.translate(150, 150); "  
    output += "ctxAirPressure.strokeStyle = 'black';"
    output += "ctxAirPressure.rotate(value * (Math.PI / 180));"    
    output += "ctxAirPressure.moveTo(0, 0);"    
    output += "ctxAirPressure.lineTo(length, length);"    
    output += "ctxAirPressure.stroke();"

    #Draw the compass for the wind direction
    output += "var cvWindDirection = document.getElementById('dynamicWeatherWindDirection');"
    output += "var ctxWindDirection = cvWindDirection.getContext('2d');"
    output += "ctxWindDirection.beginPath();"
    output += "ctxWindDirection.arc(150, 150, 140, 0, 2 * Math.PI);"
    output += "ctxWindDirection.fillStyle = 'black';"
    output += "ctxWindDirection.stroke();"
    output += "ctxWindDirection.beginPath();"
    output += "ctxWindDirection.arc(150, 150, 10, 0, 2 * Math.PI);"
    output += "ctxWindDirection.fillStyle = 'black';"
    output += "ctxWindDirection.fill();"
    output += "ctxWindDirection.font = 'bold 20px Arial';"
    output += "ctxWindDirection.fillStyle = 'black';"
    output += "ctxWindDirection.fillText('W', 13, 156);"
    output += "ctxWindDirection.fillText('N', 142, 29);"
    output += "ctxWindDirection.fillText('E', 272, 156);"
    output += "ctxWindDirection.fillText('S', 142, 285);"
    output += "value = (-359 * " + dir + " - 135);"    
    output += "ctxWindDirection.beginPath();"
    output += "ctxWindDirection.lineWidth = 5;"       
    output += "ctxWindDirection.translate(150, 150); "  
    output += "ctxWindDirection.strokeStyle = 'black';"
    output += "ctxWindDirection.rotate(value * (Math.PI / 180));"    
    output += "ctxWindDirection.moveTo(0, 0);"    
    output += "ctxWindDirection.lineTo(length, length);"    
    output += "ctxWindDirection.stroke();"
    
    return output
    
def build_styling():

    output = " .dynamicWeatherCANVAS { width: 100%; height: 100%; }"
    output += " .dynamicWeatherH3 { width: 100%; height: 50%; text-align: center }"
    return output
    
main(sys.argv)
