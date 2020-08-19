import sys
sys.path.append('/your deepvac_path/lib/')
from syszux_report import OcrReport
from syszux_log import LOG
from aip import AipOcr
import time
import os

class BaiduOcrTest:
    def __init__(self, config):
        """ 你的 APPID AK SK """
        APP_ID = config.APP_ID 
        API_KEY = config.API_KEY 
        SECRET_KEY = config.SECRET_KEY 
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        self.test_file = config.test_file
        self.test_dataset = config.test_dataset
        self.labels = {}
        with open(self.test_file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                sample = line.split()
                assert len(sample)==2, '{} file format error'.format(self.test_file)
                self.labels[sample[0]] = sample[1]

    """ 读取图片 """
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def __call__(self):
        img_names = os.listdir(self.test_dataset)
        ocr_report = OcrReport(ds_name='deepvac_ocr1.0_test_plate',total_num=len(img_names))
        for img_name in img_names:
            image = self.get_file_content(os.path.join(self.test_dataset,img_name))
            # 高精度版通用ocr api
            res = self.client.basicAccurate(image)
            # 通用ocr api
            #res = self.client.basicGeneral(image)
            pred = ''
            if 'error_code' in res.keys():
                ocr_report.add(self.labels[img_name],pred)
                LOG.logI('error code:{}'.format(res))
                continue
            for dic in res['words_result']:
                pred += dic['words'].strip()
            ocr_report.add(self.labels[img_name],pred)
            LOG.logI('{}: {}'.format(img_name,res))
            time.sleep(1)
        ocr_report()

if __name__ == '__main__':
    from config import config as deepvac_config
    ocr_test = BaiduOcrTest(deepvac_config.test)
    ocr_test()
