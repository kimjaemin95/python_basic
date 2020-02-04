BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, e_mail text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'KIMJAEMIN','todaybow@naver.com','010-3309-7000','www.tigerai.net.cn','2020-02-04 23:28:29');
INSERT INTO "users" VALUES(2,'ChoiHeeyeon','top2road@naver.com','010-9xxx-xxxx','www.naver.com','2020-02-04 23:28:29');
INSERT INTO "users" VALUES(3,'Lee','duam@naver.com','010-9xxx-xxxx','www.naver.com','2020-02-04 23:28:29');
INSERT INTO "users" VALUES(4,'Park','hanmail@naver.com','010-9xxx-xxxx','www.daum.com','2020-02-04 23:28:29');
INSERT INTO "users" VALUES(5,'Joo','cake@naver.com','010-9xxx-xxxx','www.hanmail.com','2020-02-04 23:28:29');
COMMIT;
