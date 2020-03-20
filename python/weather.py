import sys
import requests

def main(args):

    #Declare variables
    output = ""
    lat = args[1]
    long = str(float(args[2]) * -1)
    key = "****"

    #Primary program logic
    try:
        #Get data in json format and catch invalid location error
        data = get_weather(lat, long, key)
        if str(data) == "{'code': 400, 'error': 'The given location is invalid.'}":
            raise Exception("Invalid Location")
        return_output(data)       
    except Exception as e:
        return_error(str(e))

def get_weather(lat, long, key):

    request = "https://api.darksky.net/forecast/" + key + "/" + lat + "," + long;
    response = requests.get(request)
    return response.json()

def return_error(text):

    output = "<h3>Server Error</h3>"
    output += "<p>Error: " + text + "</p>"
    print(output)

def return_output(data):

    #Parse weather information
    icon = "images/weather/" + str(data["currently"]["icon"]) + ".svg"
    summary = str(data["currently"]["summary"])
    pressure = str(data["currently"]["pressure"])
    temperature = str(data["currently"]["temperature"])
    humidity = str(float(str(data["currently"]["humidity"])) * 100)
    windspeed = str(data["currently"]["windSpeed"])
    direction = str(data["currently"]["windBearing"])
    timezone = str(data["timezone"])

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
    output += "<p>Powered by <a href='https://darksky.net/'>Darksky</a>, images from <a href='https://www.flaticon.com/categories/weather'>FlatIcon.com</a>, Timezone: " + timezone + "</p>"
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
