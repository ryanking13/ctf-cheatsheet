## Generating Runtime Error

    select 1=if(CONDITION, 1, (select 1 union 2))
---
    select 1=(select CONDITION union select 1)

    # if condition is true : len(row) = 1
    # if condition is false: len(row) = 2 -- error
