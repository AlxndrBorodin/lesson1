numbers = [3, 5, 7, 9, 10.5]
#print(numbers)
numbers.append('Python')
print(len(numbers))
print(numbers[0])
print(numbers[-1])
print(numbers[1:5])
numbers.remove('Python')
print(numbers)
city_weather ={
    "city": "Москва",
    "temperature": 20,
}
print(city_weather["city"])
city_weather["temperature"] += 5
print(city_weather.get("country", "Россия"))
city_weather["date"] = "27.05.2019"
print(len(city_weather))
