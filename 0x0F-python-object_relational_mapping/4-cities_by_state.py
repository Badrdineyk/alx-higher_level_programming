#!/usr/bin/python3
# lists all cities from the database hbtn_0e_4_usa
import sys
import MySQLdb

if __name__ == "__main__":
    data_base = MySQLdb.connect(user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3])
    cur = data_base.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in cur.fetchall()]
