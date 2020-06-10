# Weather
Python调用WebService服务 查询天气预报

# 使用方法

初始化对象，需要较长时间

```bash
>>> from weather import Weather
>>> weather = Weather(verbose=1)
Building supported regions and cities ...
Built succesfully. Cost 29.724 seconds.
```

支持的所有地区
```bash
>>> region = weather.getRegion()  # 支持的所有地区
>>> print('支持的地区数', len(region))
支持的地区数 90
```

支持的所有城市
```bash
>>> cities = weather.getCity()  # 支持的所有城市
>>> print('支持的城市数', len(cities))
支持的城市数 2562
```

地区支持的城市
```bash
>>> support = weather.getRegionCity(region='巴西')  # 支持的巴西的城市
>>> print('支持的巴西城市', support)
支持的巴西城市 ['里约热内卢', '圣保罗']
```

查询城市的天气
```bash
>>> weather.getWeather(city='神州')
{'city': '神州', 'status': 0}
>>>
>>> result = weather.getWeather(city='广州')  # 查询广州的天气
>>> for k,v in result.items():
...     print(k, v)
...
city 广东 广州
reporttime 2020/06/10 14:05:27
live 今日天气实况：气温：32℃；风向/风力：西南风 2级；湿度：70%
brief 紫外线强度：最弱。空气质量：较差。
index 紫外线指数：最弱，辐射弱，涂擦SPF8-12防晒护肤品。
健臻·血糖指数：易波动，血糖易波动，注意监测。
穿衣指数：炎热，建议穿短衫、短裤等清凉夏季服装。
洗车指数：较适宜，无雨且风力较小，易保持清洁度。
空气污染指数：较差，气象条件较不利于空气污染物扩散。。

today 6月10日 阴 25℃/33℃ 无持续风向小于3级
tomorrow 6月11日 多云 26℃/33℃ 无持续风向小于3级
day1 6月10日 阴 25℃/33℃ 无持续风向小于3级
day2 6月11日 多云 26℃/33℃ 无持续风向小于3级
day3 6月12日 多云转阴 26℃/34℃ 无持续风向小于3级
day4 6月13日 多云转大雨 25℃/34℃ 无持续风向小于3级转南风4-5级
day5 6月14日 大雨 25℃/31℃ 南风转东南风4-5级
```