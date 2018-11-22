
import datetime
import hashlib
import logging
import os
import re
import threading
import time
import urllib.request

from bs4 import BeautifulSoup

from db.db_access import insert_hisq_data

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(threadName)s -'
                    '%(name)s - %(funcName)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

url = 'https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'

def validateUpdate(html):
    md5obj = hashlib.md5()
    md5obj.update(html.encode(encoding='utf-8'))
    md5code = md5obj.hexdigest()

    old_md5code = ''
    f_name = 'md5.txt'

    if os.path.exists(f_name):
        with open(f_name,'r',encoding='utf-8') as f :
            old_md5code = f.read()

    if md5code == old_md5code:
        return False
    else:
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        logger.info("数据更新")
        return True

isrunning = True
interval = 5

def controlthread_body():
    global interval,isrunning
    while isrunning:
        i = input("输入Bye终止爬虫，输入数字改变爬虫工作间隔，单位秒:")
        logger.info('控制输入{0}'.format(i))
        try:
            interval = int(i)
        except ValueError:
            if i.lower() == 'bye':
                isrunning = False

def istradtime():
    now = datetime.datetime.now()
    df = '%H%M%S'
    strnow = now.strftime(df)
    starttime = datetime.time(9,30).strftime(df)
    endtime = datetime.time(15,30).strftime(df)

    if now.weekday()==5 \
        or now.weekday() == 6\
        or (strnow<starttime or strnow>endtime):
        return False
    return True

def workthread_body():

    logger.info("爬虫开始工作")
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        data = response.read()
        html = data.decode()

        sp = BeautifulSoup(html,"html.parser")
        div = sp.select("div#quotes_content_left_pnlAJAX")
        divstring = div[0]
        isUpdated = validateUpdate(divstring)
        logger.info(["是否已经更新",isUpdated])
        if isUpdated:
            trlist = sp.select('div#quotes_content_left_pnlAJAX table tbody tr')
            data = []
            for tr in trlist:
                trtext = tr.text.strip('\n\r')
                if trtext == '':
                    continue

                logger.info(trtext)
                rows = re.split(r'\s+',trtext)
                logger.info(">>>>>>")
                logger.info(rows)
                fields = {}
                startIndex = 1
                try:
                    df = '%m/%d/%Y'
                    fields['Date'] = datetime.datetime.strptime(rows[startIndex],df)
                except ValueError:
                    logger.info(["日期解析错误",rows[startIndex]])
                    continue
                fields['Open'] = float(rows[startIndex+1])
                fields['High'] = float(rows[startIndex+2])
                fields['Low'] = float(rows[startIndex+3])
                fields['Close'] = float(rows[startIndex+4])
                fields['Volume'] = int(rows[startIndex+5].replace(',', ''))
                data.append(fields)

            logger.info(["数据2", data])
            for row in data:
                row['Symbol'] = 'AAPL'
                insert_hisq_data(row)

        logger.info("爬虫休眠{0}秒...".format(interval))
        time.sleep(interval)


def main():
    global interval,isrunning
    workthread = threading.Thread(target=workthread_body,name="WorkThread")
    workthread.start()

    controlthread = threading.Thread(target=controlthread_body, name='ControlThread')
    controlthread.start()


if __name__ == '__main__':
    main()


