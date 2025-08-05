-- bcal

create table u (
    id integer primary key,
    pin text
);

insert into u (pin) values ('0000');

create table d (
    id integer primary key,
    p bool default false,
    c text unique,
    day int,
    month int,
    msg text
);

insert into d (c, day, month, msg) values ('rd12', 24, 10, 'hoy es hoy');
insert into d (c, day, month, msg) values ('rq2x', 21, 10, 'principios de esta semana');
insert into d (c, day, month, msg) values ('rtes', 19, 10, 'semana pasada');
insert into d (c, day, month, msg) values ('87wh', 30, 10, 'semana próxima #1');
insert into d (c, day, month, msg) values ('vbnv', 2, 11, 'semana próxima #2');

-- CHECK

--
-- hoy
--
-- sqlite> select date('now');

--
-- fecha de todos los registros
--
-- sqlite> select date(printf("%d-%02d-%02d", strftime('%Y'), month, day)), msg from d;
-- 2024-10-24|hoy es hoy
-- 2024-10-21|principios de esta semana
-- 2024-10-19|semana pasada
-- 2024-10-30|semana próxima #1
-- 2024-11-02|semana próxima #2

--
-- todos los registros, donde los antiguos pasan al año siguiente
--
-- sqlite> select case
-- when
--     date(printf("%d-%02d-%02d", strftime('%Y'), month, day)) >= date('now')
-- then
--     julianday(date(printf("%d-%02d-%02d", strftime('%Y'), month, day))) - julianday(date('now'))
-- else
--     julianday(date(printf("%d-%02d-%02d", strftime('%Y'), month, day), '+1 years')) - julianday(date('now'))
-- end as dd, msg from d;
-- dd|msg
-- 0.0|hoy es hoy
-- 362.0|principios de esta semana
-- 360.0|semana pasada
-- 6.0|semana próxima #1
-- 9.0|semana próxima #2

--
-- los registros de los próximos 10 días
--
-- sqlite> with tmp as (select case
-- when
--     date(printf("%d-%02d-%02d", strftime('%Y'), month, day)) >= date('now')
-- then
--     julianday(date(printf("%d-%02d-%02d", strftime('%Y'), month, day))) - julianday(date('now'))
-- else
--     julianday(date(printf("%d-%02d-%02d", strftime('%Y'), month, day), '+1 years')) - julianday(date('now'))
-- end as dd, * from d)
-- select dd, day, month, msg from tmp where dd <= 10 order by dd;
-- dd|day|month|msg
-- 0.0|24|10|hoy es hoy
-- 6.0|30|10|semana próxima #1
-- 9.0|2|11|semana próxima #2


-- UPDATE

--
-- los registros públicos
--
-- sqlite> select * from d where p = True;
-- (vacío)

--
-- insertar los nuevos
--
-- import sqlite3
-- con = sqlite3.connect("data.db")
-- cur = con.cursor()
-- res = cur.execute("SELECT c FROM d").fetchall()
-- local_codes = [i[0] for i in res]
-- remote_data = lectura_remota()
-- filtered_remote_data = [i for i in remote_data if i[2] not in local_codes]
-- for i in filtered_remote_data:
--     cur.execute('insert into d (p,c,day,month,msg) values (?,?,?,?,?);', i)
-- con.commit()


-- ADD
-- generar 'c' desde sqlite3
-- sqlite> insert into d (p, c, day, month, msg) values (
--     False, unixepoch()||'-'||hex(randomblob(4)), 2, 11, 'semana próxima #2'
-- );


-- DELETE
-- sqlite> delete from d where id=100;


-- LIST
-- sqlite> select * from d order by id;

