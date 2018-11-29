## Leaking Table Name

### MySQL

- information_schema

```sql
SELECT table_name, column_name FROM information_schema.columns WHERE table_schema=database()
```

- procedure analyse()

```sql
SELECT * FROM table WHERE condition procedure analyse()
```

- mysql.innodb_table_stats ( >= 5.6 )
- mysql.innodb_index_stats ( >= 5.6 )

```sql
select * from mysql.innodb_table_stats where database_name=schema()
```

### SQLite

- sqlite_master table [FAQ](https://www.sqlite.org/faq.html#q7)

```sql
SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name;
```

#### TOBEUPDATED

- https://blog.pagez.kr/2015/04/19/another-error-based-sql-injection-on-mysql.html