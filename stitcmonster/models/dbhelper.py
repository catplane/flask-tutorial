import time 
import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql, #use pymysql 数据库驱动（基础DB-API）不是线程安全的
    maxconnections=6,
    mincached=2,
    maxcached=5,
    maxshared=3, #0 or None means all connections are dedicated
    blocking=True,
    maxusage=None,
    setsession=[],
    ping=0,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='password',
    database='xixida',
    charset='utf8'
)


class SQLHelper(object):

    @staticmethod
    def fetch_one(sql, args):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        conn.close()
        return result
    
    @staticmethod
    def fetch_all(self, sql, args):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        conn.close()
        return result
    