## False Based SQL injection

### MySQL

    mysql> select '1234 blah'=1234;
    +------------------+
    | '1234 blah'=1234 |
    +------------------+
    |                1 |
    +------------------+

    mysql> select '1234 blah'=4321;
    +------------------+
    | '1234 blah'=4321 |
    +------------------+
    |                0 |
    +------------------+

    mysql> select 'blah 1234'=1234;
    +------------------+
    | 'blah 1234'=1234 |
    +------------------+
    |                0 |
    +------------------+

When comparing String and Number, type juggling happens.

MySQL parses number from string's front, which is 0 when there is no number in string's forehead.

    mysql> select 'blah'=0;
    +----------+
    | 'blah'=0 |
    +----------+
    |        1 |
    +----------+

This behavior makes comparison with 0 true.

__Other True cases__

    mysql> select 'blah'=''|0;
    mysql> select 'blah'=''&0;
    mysql> select 'blah'=''^1;
    mysql> select 'blah'=''+0;
    mysql> select 'blah'=''-0;
    mysql> select 'blah'=''*0;
    mysql> select 'blah'=''/1;
    mysql> select 'blah'=''<<0;
    mysql> select 'blah'=''>>0;

### References

https://www.exploit-db.com/papers/18263/
