import logging
import pymysql

logger = logging.getLogger(__name__)

def insert_hisq_data(row):
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 password='12345',
                                 database='nasdaq')

    try:
        with connection.cursor() as cursor:
            sql = 'insert into historicalquote '\
                    '(HDate,Open,High,Low,Close,Volume,Symbol)'\
                    'valuees (%(Date)s,%(Open)s,%(High)s,%(Low)s,%(Close)s,%(Volume)s,%(Symbol)s)'

            affectedcount = cursor.execute(sql, row)
            logger.debug("影响的数据行数{0}".format(affectedcount))
            connection.commit()
    except pymysql.DatabaseError as error:
        connection.rollback()
        logger.debug('插入数据失败'+error)
    finally:
        connection.close()

