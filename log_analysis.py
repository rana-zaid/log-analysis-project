# Python 3.7.0
# Database code for the DB news.

import psycopg2

DBNAME = "news"


def db_connect(query):
    """connect code and database, fetch data and execute the SQL statements"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def get_top_articles():
    """Return the most popular three articles of all time"""
    popular_articles_sql = """
        SELECT slug AS article, COUNT(*) AS views
        FROM articles,log
        WHERE slug = SUBSTRING(path,10)
        GROUP BY slug
        ORDER BY views DESC
        LIMIT 3
        """
    result = db_connect(popular_articles_sql)
    print("\nThe most popular three articles of all time:")
    for (slug, views) in result:
        print(' "{}"'.format(slug)),
        print(" - {} views".format(views))


def get_top_authors():
    """Return the most popular article authors of all time"""
    popular_authors_sql = """
    SELECT name, COUNT(*) AS views
    FROM authors,articles,log
    WHERE slug=SUBSTRING(path,10) AND articles.author= authors.id
    GROUP BY name
    ORDER BY views DESC
    """
    result = db_connect(popular_authors_sql)
    print("\nThe most popular article authors of all time:")
    for (name, views) in result:
        print(" {} - {} views".format(name, views))


def get_requests_error():
    """Return days with more than 1% of requests lead to errors is"""
    requests_error_sql = """
    SELECT subtotalview.date,
    ROUND((100.0*subtotalview.subtotal/totalview.total),2) AS percentage
    FROM subtotalview,totalview
    WHERE subtotalview.date= totalview.date
    AND ROUND((100.0*subtotalview.subtotal/totalview.total),2)>1.0
    ORDER BY percentage DESC
    """
    result = db_connect(requests_error_sql)
    print("\nDays with more than 1% of requests lead to errors is:")
    for (date, percentage) in result:
        print(' {} - {}% '
              'errors'.format(date.strftime('%B %d, %Y'), percentage))


get_top_articles()
get_top_authors()
get_requests_error()
