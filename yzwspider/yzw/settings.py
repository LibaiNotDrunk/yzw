# -*- coding: utf-8 -*-


BOT_NAME = 'yzw'
SPIDER_MODULES = ['yzwspider.yzw.spiders']
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
CONCURRENT_REQUESTS = 128
ITEM_PIPELINES = {
    'yzwspider.yzw.pipelines.YzwPipeline': 300,
}

# 日志级别与输出路径
LOG_LEVEL = 'INFO'
LOG_FILE = 'log.txt'



SSDM = '11'
MLDM = '01'
YJXKDM = '0101'
XXFS = ''
YWKY = ''
WY = ''
FEATURE = ''

# MYSQL
MYSQL = True
HOST = 'localhost'
USER = 'root'
PASSWORD = ''
PORT = 3306
DATABASE = 'yanzhao'
TABLE = 'major'
CHARSET = 'utf8'
# EXCEL
EXCEL_FILE_NAME = "研招网专业信息"
EXCEL_FILE_PATH = "."



# 固定内容
FCSI_FILE = 'first_class_subject_index.txt'
PROVINCE_LISE = ['11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37',
                '41', '42', '43', '44', '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64', '65', '71',
                '81', '82']
PROVINCE_DICT = {'35': '福建', '21': '辽宁', '51': '四川', '34': '安徽', '63': '青海', '42': '湖北', '64': '宁夏', '33': '浙江', '46': '海南',
        '82': '台湾', '61': '陕西', '37': '山东', '41': '河南', '13': '河北', '45': '广西', '54': '西藏', '14': '山西', '81': '澳门',
        '36': '江西', '52': '贵州', '50': '重庆', '44': '广东', '32': '江苏', '53': '云南', '71': '香港', '11': '北京', '31': '上海',
        '23': '黑龙江', '62': '甘肃', '22': '吉林', '65': '新疆', '43': '湖南', '15': '内蒙古', '12': '天津'}
LIST_985 = {"北京大学", "清华大学", "中国科学技术大学", "南京大学", "复旦大学", "上海交通大学", "西安交通大学", "浙江大学", "哈尔滨工业大学", "北京理工大学", "南开大学", "天津大学",
            "东南大学", "武汉大学", "华中科技大学", "吉林大学", "厦门大学", "山东大学", "中国海洋大学", "湖南大学", "中南大学", "大连理工大学", "北京航空航天大学", "重庆大学",
            "四川大学", "电子科技大学", "中山大学", "华南理工大学", "兰州大学", "西北工业大学", "东北大学", "同济大学", "北京师范大学", "中国人民大学", "中国农业大学",
            "国防科技大学", "中央民族大学", "华东师范大学", "西北农林科技大学"}
LIST_211 = {"北京大学", "中国人民大学", "清华大学", "北京交通大学", "北京工业大学", "北京航空航天大学", "北京理工大学", "北京科技大学", "北京化工大学", "北京邮电大学", "中国农业大学",
            "北京林业大学", "北京中医药大学", "北京师范大学", "北京外国语大学", "中国传媒大学", "中央财经大学", "对外经济贸易大学", "北京体育大学", "中央音乐学院", "中央民族大学",
            "中国政法大学", "华北电力大学", "华北电力大学(保定)", "南开大学", "天津大学", "天津医科大学", "河北工业大学", "太原理工大学", "内蒙古大学", "辽宁大学", "大连理工大学",
            "东北大学", "大连海事大学", "吉林大学", "延边大学", "东北师范大学", "哈尔滨工业大学", "哈尔滨工程大学", "东北农业大学", "东北林业大学", "复旦大学", "同济大学",
            "上海交通大学", "华东理工大学", "东华大学", "华东师范大学", "上海外国语大学", "上海财经大学", "上海大学", "第二军医大学", "南京大学", "苏州大学", "东南大学",
            "南京航空航天大学", "南京理工大学", "中国矿业大学", "中国矿业大学(北京)", "河海大学", "江南大学", "南京农业大学", "中国药科大学", "南京师范大学", "浙江大学", "安徽大学",
            "中国科学技术大学", "合肥工业大学", "厦门大学", "福州大学", "南昌大学", "山东大学", "中国海洋大学", "中国石油大学", "中国石油大学(华东)", "中国石油大学(北京)",
            "郑州大学", "武汉大学", "华中科技大学", "中国地质大学", "中国地质大学(北京)", "中国地质大学(武汉)", "武汉理工大学", "华中农业大学", "华中师范大学", "中南财经政法大学",
            "湖南大学", "中南大学", "湖南师范大学", "国防科学技术大学", "中山大学", "暨南大学", "华南理工大学", "华南师范大学", "广西大学", "海南大学", "四川大学", "西南交通大学",
            "电子科技大学", "四川农业大学", "西南财经大学", "重庆大学", "西南大学", "贵州大学", "云南大学", "西藏大学", "西北大学", "西安交通大学", "西北工业大学",
            "西安电子科技大学", "长安大学", "西北农林科技大学", "陕西师范大学", "第四军医大学", "兰州大学", "青海大学", "宁夏大学", "新疆大学", "石河子大学"}
SUBJECT_INDEX = {'01': '哲学', '02': '经济学', '03': '法学', '04': '教育学', '05': '文学', '06': '历史学', '07': '理学',
                '08': '工学', '09': '农学', '10': '医学', '11': '军事学', '12': '管理学', '13': '艺术学'}

CREATE_TEBLE_SQL = "CREATE TABLE `{0}` (" \
                   "`id` char(21) PRIMARY KEY,`招生单位` varchar(40) NOT NULL," \
                   "`院校特性` varchar(10) DEFAULT NULL," \
                   "`院系所` varchar(40) DEFAULT NULL," \
                   "`专业` varchar(40) DEFAULT NULL," \
                   "`研究方向` TINYTEXT DEFAULT NULL," \
                   "`学习方式` varchar(30) DEFAULT NULL," \
                   "`拟招生人数` varchar(40) DEFAULT NULL," \
                   "`业务课一` varchar(40) DEFAULT NULL," \
                   "`业务课二` varchar(40) DEFAULT NULL," \
                   "`外语` varchar(40) DEFAULT NULL," \
                   "`政治` varchar(40) DEFAULT NULL," \
                   "`所在地` varchar(30) DEFAULT NULL," \
                   "`指导老师` TINYTEXT DEFAULT NULL," \
                   "`专业代码` varchar(10) DEFAULT NULL," \
                   "`门类` varchar(20) DEFAULT NULL," \
                   "`一级学科` varchar(40) DEFAULT NULL)" \
                   " ENGINE=MyISAM DEFAULT CHARSET=utf8"

CREATE_TEBLE_SQLITE = "CREATE TABLE `{0}` (" \
                   "`id` char(21) PRIMARY KEY,`招生单位` varchar(40) NOT NULL," \
                   "`院校特性` varchar(10) DEFAULT NULL," \
                   "`院系所` varchar(40) DEFAULT NULL," \
                   "`专业` varchar(40) DEFAULT NULL," \
                   "`研究方向` TINYTEXT DEFAULT NULL," \
                   "`学习方式` varchar(30) DEFAULT NULL," \
                   "`拟招生人数` varchar(40) DEFAULT NULL," \
                   "`业务课一` varchar(40) DEFAULT NULL," \
                   "`业务课二` varchar(40) DEFAULT NULL," \
                   "`外语` varchar(40) DEFAULT NULL," \
                   "`政治` varchar(40) DEFAULT NULL," \
                   "`所在地` varchar(30) DEFAULT NULL," \
                   "`指导老师` TINYTEXT DEFAULT NULL," \
                   "`专业代码` varchar(10) DEFAULT NULL," \
                   "`门类` varchar(20) DEFAULT NULL," \
                   "`一级学科` varchar(40) DEFAULT NULL)"
