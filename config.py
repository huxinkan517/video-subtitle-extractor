# -*- coding: utf-8 -*-
"""
@Author  : Fang Yao 
@Time    : 2021/3/24 9:36 上午
@FileName: config.py
@desc: 项目配置文件，可以在这里调参，牺牲时间换取精确度，或者牺牲准确度换取时间
"""
import configparser
import os
import re
import time
from pathlib import Path
from enum import Enum
from fsplit.filesplit import Filesplit
from paddle import fluid

fluid.install_check.run_check()
# 判断代码路径是否合法
IS_LEGAL_PATH = True
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'settings.ini')
if not os.path.exists(config_path):
    # 如果没有配置文件，默认使用中文
    with open(config_path, mode='w') as f:
        f.write('[DEFAULT]\n')
        f.write('Language = ch\n')
        f.write('Mode = fast')
config.read(config_path)

# 设置识别语言
REC_CHAR_TYPE = config['DEFAULT']['Language']
print(f'识别字幕语言：{REC_CHAR_TYPE}')

# 设置识别模式
MODE_TYPE = config['DEFAULT']['Mode']
print(f'识别模式：{MODE_TYPE}')
ACCURATE_MODE_ON = False
if MODE_TYPE == 'accurate':
    ACCURATE_MODE_ON = True
if MODE_TYPE == 'fast':
    ACCURATE_MODE_ON = False

# --------------------- 请你不要改 start-----------------------------
# 项目的base目录
BASE_DIR = str(Path(os.path.abspath(__file__)).parent)
# 是否包含中文
if re.search(r"[\u4e00-\u9fa5]+", BASE_DIR):
    IS_LEGAL_PATH = False
# 是否包含空格
if re.search(r"\s", BASE_DIR):
    IS_LEGAL_PATH = False
while not IS_LEGAL_PATH:
    print('【警告】程序运行中断！路径不合法！请不要将程序放入带有空格和中文的路径下！！！请修改程序路径名后重新运行程序')
    time.sleep(3)
# 模型文件目录
# 文本检测模型
DET_MODEL_BASE = os.path.join(BASE_DIR, 'backend', 'models')
DET_MODEL_PATH = os.path.join(DET_MODEL_BASE, 'ch_det')
DET_MODEL_FAST_PATH = os.path.join(DET_MODEL_BASE, 'ch_det_fast')
# 设置文本识别模型 + 字典
REC_MODEL_BASE = os.path.join(BASE_DIR, 'backend', 'models')
# 默认文本识别模型为中文
REC_MODEL_PATH = os.path.join(REC_MODEL_BASE, 'backend', 'models', 'ch_rec')
REC_MODEL_FAST_PATH = os.path.join(REC_MODEL_BASE, 'ch_rec_fast')
# 默认字典路径为中文
DICT_BASE = os.path.join(BASE_DIR, 'backend', 'ppocr', 'utils', 'dict')
DICT_PATH = os.path.join(BASE_DIR, 'backend', 'ppocr', 'utils', 'ppocr_keys_v1.txt')


# 如果设置了识别文本语言类型，则设置为对应的语言
if REC_CHAR_TYPE in ('ch', 'japan', 'korean', 'en', 'EN_symbol', 'french', 'german', 'it', 'es', 'pt', 'ru', 'ar',
                     'ta', 'ug', 'fa', 'ur', 'rs_latin', 'oc', 'rs_cyrillic', 'bg', 'uk', 'be', 'te', 'kn', 'ch_tra', 'hi', 'mr', 'ne', 'EN'):
    REC_MODEL_PATH = os.path.join(BASE_DIR, 'backend', 'models', f'{REC_CHAR_TYPE}_rec')
    REC_MODEL_FAST_PATH = os.path.join(REC_MODEL_BASE, f'{REC_CHAR_TYPE}_rec_fast')
    DICT_PATH = os.path.join(BASE_DIR, 'backend', 'ppocr', 'utils', 'dict', f'{REC_CHAR_TYPE}_dict.txt')
    if not os.path.exists(REC_MODEL_FAST_PATH):
        REC_MODEL_FAST_PATH = REC_MODEL_PATH

# 查看该路径下是否有文本模型识别完整文件，没有的话合并小文件生成完整文件
if 'inference.pdiparams' not in (os.listdir(REC_MODEL_PATH)):
    fs = Filesplit()
    fs.merge(input_dir=REC_MODEL_PATH)


# 默认字幕出现的大致区域
class SubtitleArea(Enum):
    # 字幕区域出现在下半部分
    LOWER_PART = 0
    # 字幕区域出现在上半部分
    UPPER_PART = 1
    # 不知道字幕区域可能出现的位置
    UNKNOWN = 2
    # 明确知道字幕区域出现的位置
    CUSTOM = 3


class BackgroundColor(Enum):
    # 字幕背景
    WHITE = 0
    DARK = 1
    UNKNOWN = 2
# --------------------- 请你不要改 end-----------------------------


# --------------------- 请根据自己的实际情况改 start-----------------------------
# 是否使用GPU
# 使用GPU可以提速20倍+，你要是有N卡你就改成 True
USE_GPU = False
# 如果paddlepaddle编译了gpu的版本
if fluid.is_compiled_with_cuda():
    # 查看是否有可用的gpu
    if len(fluid.cuda_places()) > 0:
        # 如果有GPU则使用GPU
        USE_GPU = True
        print('使用GPU进行加速')

# 使用快速字幕检测算法时，背景颜色
BG_MOD = BackgroundColor.DARK
# 黑色背景被减矩阵阈值
BG_VALUE_DARK = 200
# 其他背景颜色被减矩阵阈值
BG_VALUE_OTHER = 63
# ROI比例
ROI_RATE = 0.4

# 默认字幕出现区域为下方
SUBTITLE_AREA = SubtitleArea.UNKNOWN

# 余弦相似度阈值
# 数值越小生成的视频帧越少，相对提取速度更快但生成的字幕越不精准
# 1表示最精准，每一帧视频帧都进行字幕检测与提取，生成的字幕最精准
# 0.925表示，当视频帧1与视频帧2相似度高达92.5%时，视频帧2将直接pass，不字检测与提取视频帧2的字幕
COSINE_SIMILARITY_THRESHOLD = 0.95 if SUBTITLE_AREA == SubtitleArea.UNKNOWN else 0.9

# 当前帧与之后的多少帧比较
FRAME_COMPARE_TIMES = 10

# 每一秒抓取多少帧进行OCR识别
EXTRACT_FREQUENCY = 3
# 每几帧抽取一帧进行OCR识别
EXTRACT_INTERVAL = 8

# 欧式距离相似值
EUCLIDEAN_SIMILARITY_THRESHOLD = 0.9

# 容忍的像素点偏差
PIXEL_TOLERANCE_Y = 50  # 允许检测框纵向偏差50个像素点
PIXEL_TOLERANCE_X = 100  # 允许检测框横向偏差100个像素点

# 字幕区域偏移量
SUBTITLE_AREA_DEVIATION_PIXEL = 50

# 最有可能出现的水印区域
WATERMARK_AREA_NUM = 5

# 文本相似度阈值
# 用于去重时判断两行字幕是不是统一行
# 采用动态算法实现相似度阈值判断: 对于短文本要求较低的阈值，对于长文本要求较高的阈值
THRESHOLD_TEXT_SIMILARITY = 0.8

# 字幕提取中置信度低于0.8的不要
DROP_SCORE = 0.8
# --------------------- 请根据自己的实际情况改 end-----------------------------

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
