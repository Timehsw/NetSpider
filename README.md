# NetSpider
python3网络爬虫|我日常需要的数据，只好自己爬取了。

# 普通爬虫

# scrapy爬虫

爬取豌豆荚

```
# 创建一个scrapy项目
scrapy startproject mySpider

# 制作爬虫
scrapy genspider wandoujia "www.wandoujia.com"

# 执行爬虫
scrapy crawl wandoujia

# 保存数据
# json格式，默认为Unicode编码
scrapy crawl wandoujia -o package.json

# json lines格式，默认为Unicode编码
scrapy crawl wandoujia -o package.jsonl

# csv 逗号表达式，可用Excel打开
scrapy crawl wandoujia -o package.csv

# xml格式
scrapy crawl wandoujia -o package.xml
```

# scrapy shell

```
scrapy shell "http://www.wandoujia.com/search/16717912156701033019_page4"
```

## 腾讯应用宝
