const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '37c1e405e8mshe1195c584962438p11df10jsn2d5136ac7f84',
		'X-RapidAPI-Host': 'weather-by-api-ninjas.p.rapidapi.com'
	}
};
var datetime = new Date();
console.log(datetime);
document.getElementById("time").textContent = datetime;
const getWeather = (city) => {
	cityName.innerHTML = city
	fetch('https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=' + city, options)
		.then(response => response.json())
		.then((response) => {
			console.log(response)
			temp.innerHTML = response.temp
			feels_like.innerHTML = response.feels_like
			humidity.innerHTML = response.humidity
			min_temp.innerHTML = response.min_temp
			max_temp.innerHTML = response.max_temp
			wind_speed.innerHTML = response.wind_speed
			wind_degrees.innerHTML = response.wind_degrees
		})
		.catch(err => console.error(err));
}

submit.addEventListener("click", (e) => {
	e.preventDefault()
	getWeather(city.value)
})
//by default delhi
getWeather("Delhi");


const setWeatherCommonCities = (city) => {
	const temp = document.getElementById("Temp" + city);
	const feels_like = document.getElementById("FeelsLike" + city);
	const humidity = document.getElementById("Humidity" + city);
	const min_temp = document.getElementById("MinTemp" + city);
	const max_temp = document.getElementById("MaxTemp" + city);
	const wind_speed = document.getElementById("WindSpeed" + city);
	const wind_degrees = document.getElementById("WindDegrees" + city);

	fetch('https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=' + city, options)
		.then(response => response.json())
		.then((response) => {
			console.log(response)
			temp.innerHTML = response.temp;
			feels_like.innerHTML = response.feels_like;
			humidity.innerHTML = response.humidity;
			min_temp.innerHTML = response.min_temp;
			max_temp.innerHTML = response.max_temp;
			wind_speed.innerHTML = response.wind_speed;
			wind_degrees.innerHTML = response.wind_degrees;
		})
		.catch(err => console.error(err));

}
setWeatherCommonCities("Delhi");
setWeatherCommonCities("Mumbai");
setWeatherCommonCities("Kolkata");
setWeatherCommonCities("Chennai");