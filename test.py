from weather import Weather

weather = Weather(verbose=1)
region = weather.getRegion()  # 支持的所有地区
cities = weather.getCity()  # 支持的所有城市
support = weather.getRegionCity(region='巴西')  # 支持的巴西的城市
result = weather.getWeather(city='广州')  # 查询广州的天气
print('支持的地区数', len(region))
print('支持的城市数', len(cities))
print('支持的巴西城市', support)
print('广州的天气', result)
