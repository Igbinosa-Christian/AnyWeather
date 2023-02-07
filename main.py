from flask import Flask, render_template, request, flash
import requests




app = Flask(__name__)

app.config['SECRET_KEY']='ddhhyedewdyurwiu4u838'


# Home page route
@app.route('/', methods = ['GET','POST'])
def index():

    weather_data = []
 
    # To display current city weather
    url_ip = 'https://ipinfo.io/json?token=3da5e5f0b554e7'

    re = requests.get(url_ip).json()

        
        
    city_name = re['city']

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=04d6a59f7d372177853b85deb5c0379c&units=imperial'
    city = city_name


    r = requests.get(url.format(city)).json()

    if r['cod'] == '404':
        flash("City Not Found")

    else:

        weather = {
            'city': city,
            'country': r['sys']['country'],
            'temperature': round((r['main']['temp']), 2),
            'temperature_celcius': round((r['main']['temp']-32) * (5/9), 2),
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
         }

        weather_data.append(weather)


    # Display serached city weather
    if request.method == 'POST':
        
        weather_data.pop(0)
        city_name = request.form.get('search_city')

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=04d6a59f7d372177853b85deb5c0379c&units=imperial'
        city = city_name


        r = requests.get(url.format(city)).json()

        if r['cod'] == '404':
            flash("City Not Found")

        else:

            weather = {
                'city': city,
                'country': r['sys']['country'],
                'temperature': round((r['main']['temp']), 2),
                'temperature_celcius': round((r['main']['temp']-32) * (5/9), 2),
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon']
            }

            weather_data.append(weather)


            
    return render_template('index.html', weather_data=weather_data)


if __name__ == "__main__":
    app.run(debug=True)