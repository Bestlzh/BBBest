import sys
import json
import logging
from pipelines import MysqlPipeline
import redis
r = redis.Redis()
logging.basicConfig()
logger = logging.getLogger('pipelines')
logger.info('begin to process item...')


def get_item(spider):
    key = '%s:items' % spider
    print(key)
    item = r.blpop(key)
    # print(item[1])
    if item:
        return json.loads(item[1].decode())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        logger.info('need spider name')
        exit(1)
    spider = sys.argv[1]
    print(spider)
    db = MysqlPipeline()
    print('db好了')
    db.open_spider(spider)
    print('db.open_spider也好了')
    item = get_item(spider)
    print('item也好了')
    while item:
        db.process_item(item,spider)
        item = get_item(spider)
    db.close_spider(spider)

