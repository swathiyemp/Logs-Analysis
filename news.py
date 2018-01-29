#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = 'news'


def articles():

    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute("""SELECT articles.title, COUNT(log.path) AS views FROM
                articles,log where articles.slug=SUBSTRING(log.path,10,100)
                GROUP BY articles.title ORDER BY views DESC LIMIT 3""")
    data1 = cur.fetchall()
    print '''
1)Top 3 Articles based on views
'''

    for row in data1:
        print 'Article: %s -- %s Views' % (row[0], row[1])

    db.close()


def authors():

    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute("""SELECT authors.name,COUNT(log.path) AS fmt from authors left
                join articles on authors.id=articles.author left join log on
                substring(log.path,10,100)=articles.slug group by authors.name
                order by fmt desc""")
    data2 = cur.fetchall()
    print '''
2)Top 4 Authors based on views
'''

    for row in data2:
        print 'Author: %s -- %s Views' % (row[0], row[1])

    db.close()


def Errors():

    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute("""select tot2.time,cast(tot2.tot_errs * 100 as float)
                /tot1.tot_logs as err_days from tot1,tot2 where tot1.time
                =tot2.time and cast(tot2.tot_errs *100 as float)/tot1.
                tot_logs>1""")
    data3 = cur.fetchall()
    print '''
3)Days with more than 1% errors
'''

    for row in data3:
        print '%s -- %s%%errors' % (row[0], round(row[1], 2))

    db.close()


if __name__ == '__main__':
    articles()
    authors()
    Errors()
