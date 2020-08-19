# 使用百度ocr评估在SYSZUXocr验收集上的准确度

## 环境

安装百度aip: `pip install baidu-aip`

克隆deepvac: `git clone https://github.com/DeepVAC/deepvac`

## 配置

百度云注册账号 https://cloud.baidu.com/?from=console

管理应用 https://console.bce.baidu.com/ai/#/ai/ocr/overview/index 创建一个文字识别应用，获取AppID 、API Key、Secret Key，这三个密钥写入config.py, test_file未标注的txt文件，test_dataset为图片目录

>config.test.APP_ID = 

>config.test.API_KEY = 

>config.test.SECRET_KEY = 

>config.test.test_file = 

>config.test.test_dataset = 

在test.py中引入deepvac的目录: `sys.path.append('/your deepvac_path/lib/')`

## 运行

`python3 test.py`

## 结果

ocr_on_news

|dataset|total|duration|accuracy|precision|recall|miss|error|
|--|--|--|--|--|--|--|--|
|ocr_on_news|200|269.228|0.825|0.8375634517766497|0.9821428571428571|0.015|0.175|

|dataset|total_per_char|correct_per_char|accuracy_per_char|
|--|--|--|--|
|ocr_on_news|2056|1987|0.9664396887159533|

ocr_on_film

|dataset|total|duration|accuracy|precision|recall|miss|error|
|--|--|--|--|--|--|--|--|
|ocr_on_film|100|140.005|0.98|0.98|1.0|0.0|0.02|

|dataset|total_per_char|correct_per_char|accuracy_per_char|
|--|--|--|--|
|ocr_on_film|579|577|0.9965457685664939|

ocr_on_social

...

ocr_on_plate

...
