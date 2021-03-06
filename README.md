# yzw
scrapy爬取研招网研究生考试专业信息(末尾有度盘全部数据)

含有考试范围、专业等，可输出到Excel或SQLite。

数据大概这个样子，获得数据之后我们就能方便地进行筛选了。

![图1](https://github.com/Hthing/yzw/blob/master/img/excel.png) 

## 安装：  

可直接使用pip自主安装

```
pip install --upgrade yzwspider
```

其中使用了pymysq、scrapy、xlwt第三方库



## 运行环境：
python3.7以上（使用了argparse模块的新参数）

## 数据格式：

建表语句存于yzwspider/yzw/settings.py中， 爬取时会自动建表（数据库要提前建立）。

```sql
CREATE TABLE `major` (
  `id` char(21) PRIMARY KEY, # id 为爬取页面的id参数+考试范围序号
  `招生单位` varchar(40) NOT NULL,
  `院校特性` varchar(10) DEFAULT NULL,
  `院系所` varchar(40) DEFAULT NULL,
  `专业` varchar(40) DEFAULT NULL,
  `研究方向` TINYTEXT DEFAULT NULL,
  `学习方式` varchar(30) DEFAULT NULL,
  `拟招生人数` varchar(40) DEFAULT NULL,
  `业务课一` varchar(40) DEFAULT NULL,
  `业务课二` varchar(40) DEFAULT NULL,
  `外语` varchar(40) DEFAULT NULL,
  `政治` varchar(40) DEFAULT NULL,
  `所在地` varchar(30) DEFAULT NULL,
  `指导老师` TINYTEXT DEFAULT NULL,
  `专业代码` varchar(10) DEFAULT NULL,
  `门类` varchar(20) DEFAULT NULL,
  `一级学科` varchar(40) DEFAULT NULL
)
```



## 使用方法

省市代码，学科门类，一级学科代码（学科类别） 可在研招网查得。 例，计算机科学与技术：0812

https://yz.chsi.com.cn/zsml/queryAction.do

```
python -m yzwspider [-h] [-ssdm] [-mldm] [-xxfs] [-yjxk] [-ywky] [-wy] [-feature] [--all] [--log] 输出目标 [其他参数]
```

yzwspider参数： （括号内为默认值）

> **-ssdm**： 省市代码(11)  支持中文名 即北京、上海等
>
> **-mldm：** 门类代码(01)  支持中文名： 理学、工学等
>
> **-yjxk:**  一级学科代码(0101)
> 
> **-xxfs:**  学习方式，可选全日制、非全日制(默认全部)
> 
> **-ywky-**  业务课一，可选数学一、数学二、其他（默认全部）
> 
> **-wy-**    外语，可选英语一、英语二（默认全部）
> 
> **-feature-** 学校特性，可选211、985（默认全部）
>
> **--all：**爬取全部专业信息并只可输出到sqlite
>
> **--log：** 保存日志文件至当前目录
>
> 命令 "excel" 参数：
>
> > **-o：** .xls文件输出路径， 默认为当前目录
>
> 命令 "mysql" 参数：
> >
> > **-db：**   数据库名(yanzhao)
> >
> > **-table：**数据表名（major）

例如，我们想获取北京市(11)的计算机科学与技术专业(0812)并输出为excel文件

```
 python -m yzwspider -ssdm 11 -yjxk 0812 excel
 python -m yzwspider -ssdm 北京 -yjxk 0854 -xxfs 全日制 -ywky 数学二 -wy 英语二 -feature 211 excel
```

上条语句可将"-ssdm 11"替换为"-ssdm 北京"同样生效。

最终将会得到如下的信息

```
2019-12-04 15:13:57 [scrapy.core.engine] INFO: Closing spider (finished)
2019-12-04 15:13:57 [YzwPipeline] INFO: excel文件已存储于 /home/研招网专业信息.xls
2019-12-04 15:13:57 [yzwspider.yzw.collector] INFO: 数据抓取完成, 共计 691 条数据，
                    程序开始时间 2019-12-04 15:13:44 , 结束时间 2019-12-04 15:13:57, 耗时 0 分钟
2019-12-04 15:13:57 [scrapy.core.engine] INFO: Spider closed (finished)
```

若输出至sqlite（默认参数可以不填）

```
python -m yzwspider -ssdm 11 -yjxk 0812 mysql -table test
```

输出信息类似于excel.  如果想保存日志则加上--log即可





附上最终数据

链接：https://pan.baidu.com/s/1T-ejrTdqMTodA1T2DWU9Dg 
提取码：xt3e

## 爬取页面

​	爬取的页面如下，另外每行数据的id由页面的id以及考试范围顺序组成

​	![图2](https://github.com/Hthing/yzw/blob/master/img/page.png)

