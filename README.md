# SYSZUXocr
一个高质量的OCR测试集。

SYSZUXocr具有如下特点：

- 划分为不同的领域，可以测试OCR算法在不同领域上的表现；
- 贴近实际环境，分数高低直接体现算法落地的成熟度；
- 标准的OcrReport模块来打分，公平程度犹如高考；
- 以汉字为主，未来也会兼顾其它语种；
- 提供图片和标签，检测和识别均需用户自定义实现，更贴近产业；

dataset目录中的图片文件使用git lfs维护，克隆该项目前，你需要首先安装git-lfs：
```bash
#on Linux
apt install git-lfs

#on macOS
brew install git-lfs
```
然后：
```bash
#克隆该项目
git clone https://github.com/DeepVAC/SYSZUXocr

#拉取dataset图片
git lfs pull
```

## 使用说明

项目的目录说明如下：
|  目录   |  说明   |
|---------|---------|
|dataset  |数据集   |
|src     |测试示例代码|
|dataset/ocr_on_film | 测试图片，来自影视剧的字幕|
|dataset/ocr_on_news | 测试图片，来自新闻的字幕|
|dataset/ocr_on_plate | 测试图片，来自车牌|
|dataset/ocr_on_social | 测试图片，来自网络的斗图|
|dataset/ocr_on_film.txt | ocr_on_film的标签|
|dataset/ocr_on_news.txt | ocr_on_news的标签|
|dataset/ocr_on_plate.txt | ocr_on_plate的标签 |
|dataset/ocr_on_social.txt | ocr_on_social的标签 |


## 如何计算分数

测试集上的分数可以通过deepvac项目lib库的syszux_report模块（OcrReport类，来自https://github.com/DeepVAC/deepvac/blob/master/lib/syszux_report.py）给出。OcrReport类会给出两种成绩，按样本统计的、按字符统计的。

#### 按样本统计
也就是整个样本（多数情况下就是一整行文字）只要有一个字符是错的，则整个样本就是错的。

定义如下概念：
- TP: 在有文字的图片上，预测出正确的文字；
- FP: 在有文字或没文字的图片上，预测出错误的文字；
- TN: 在没文字的图片上，没预测出文字（正确）；
- FN: 在有文字的图片上，没预测出文字（错误）；

定义样本的准确率、精确率、召回率如下：
- 准确率(accuracy) = (TP+TN)/(TP+FP+TN+FN)
- 精确率(precision) = TP/(TP+FP)
- 召回率(recall) = TP/(TP+FN)
- 漏检率(漏检率) = FN/(TP+FP+TN+FN)
- 错误率(错误率) = (FP+FN)/(TP+FP+TN+FN)）


#### 按字符统计
OcrReport类统计所有的文字数量、使用可编辑距离计算正确文字的数量、计算字符级别的准确率。

#### 使用OcrReport模块来进行以上分数的计算
```python
#use the OcrReport class
report = OcrReport('gemfield',4)
report.add('朝辞白帝彩云间', '朝辞白彩云间')
report.add('君不见黄河之水天上来', '君不见黄河之水天上来')
report.add('非汝之为美，美人之贻', '非汝之为美，美人之遗')
report.add('gemfield', 'gem fie,ld')
report()
```
程序会输出markdown格式的报告：
```bash
|dataset|total|duration|accuracy|precision|recall|miss|error|
|--|--|--|--|--|--|--|--|
|gemfield|4|0.001|0.25|0.25|1.0|0.0|0.75|
        

|dataset|total_per_char|correct_per_char|accuracy_per_char|
|--|--|--|--|
|gemfield|35|31|0.8857142857142857|
```

放入项目的md文件中，在web上会显示为：
|dataset|total|duration|accuracy|precision|recall|miss|error|
|--|--|--|--|--|--|--|--|
|gemfield|4|0.001|0.25|0.25|1.0|0.0|0.75|
        

|dataset|total_per_char|correct_per_char|accuracy_per_char|
|--|--|--|--|
|gemfield|35|31|0.8857142857142857|


## 使用许可
本项目仅限用于纯粹的学术研究，如：
- 个人学习；
- 比赛排名；
- 公开发表且开源其实现的论文；

不得用于任何形式的商业牟利，包括但不限于：
- 任何形式的商业获利行为；
- 任何形式的商务机会获取；
- 任何形式的商业利益交换；


## 项目贡献
我们欢迎各种形式的贡献，包括但不限于：
- 提交自己的作品/产品在SYSZUXocr上的成绩；
- 发现和Fix项目的bug；
- 提交高质量的测试集数据；
