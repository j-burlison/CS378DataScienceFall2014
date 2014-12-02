CREATE TABLE CHRISTIAN_charities AS 
(SELECT * FROM Charities where name like '%CHURCH%' 
or name like '%MINISTRY%' or name like '%CHRISTIAN%' 
or name like '%BABTIST%' or name like '%CHRIST%' 
or name like '%JESUS%' or name like '%EVANGELISTIC%' 
or name like '%EVANGEL%' or name like '%GOSPEL%'
or name like '%HOLY GHOST%' or name like '%GOD%'
or name like '%MORMON%' or name like '%METHODIST%'
or name like '%BIBLE%' or name like '%LUTHERAN%');




CREATE TABLE SPORTS_charities AS 
(SELECT * FROM Charities where name like '%FOOTBALL%' 
or name like '%BASEBALL%' or name like '%BASKETBALL%' 
or name like '%SPORT%' or name like '%ATHLETIC%' 
or name like '%SWIM%' or name like '%OLYMPI%' 
or name like '%TENNIS%' or name like '%GOLF%'
or name like '%POLO%' or name like '%CRICKET%'
or name like '%LACROSSE%' or name like '%ULTIMATE FRISBEE%'
or name like '%POWERLIFT%' or name like '%GYM%' or name like '%WRESTLING%'
 or name like '%SOFTBALL%'  or name like '%VOLLEYBALL%');
 
 
 
 CREATE TABLE CHURCH_charities AS 
(SELECT * FROM Charities where name like '%CHURCH%'
or name like '%CHAPEL%' or name like '%CATHEDRAL%' 
or name like '%MINISTRY%');


 CREATE TABLE HEALTH_charities AS 
(SELECT * FROM Charities where name like '%HEALTH%');


CREATE TABLE CHILD_charities AS 
(SELECT * FROM FCHARITIES where name like '%DAUGHTER%'
or name like '%CHILD%' or name like '%ORPHAN%' or name like '%YOUTH%');
