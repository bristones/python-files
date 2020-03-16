#starting mysql terminal
#sudo mysql -u root -p

desc  #showing properties





mydbConnection=mysql.connector.connect
#(host="localhost:8080", port="3306",user="root",password="",database="my_school_db")


cursor = mydbConnection.cursor()
cursor.execute("select * from school")
schools=cursor.fetchall()
for sch in schools:
    print (sch)


Create database school
CREATE TABLE students(id int(5)AUTO_INCREMENT PRIMARY KEY, Code varchar(10), name varchar(250), address varchar(250))
INSERT into students(Code,name,address) VALUES ('1003','Eastleigh High School','Nairobi')

#to protect the values from malicious additions, 
INSERT into students(Code,name,address) VALUES(%s,%s,%s) VALUES ('1003','Eastleigh High School','Nairobi')

#insert means you're adding more variables or rows to the DB
insert into Mashule(code,name,location) Values('1','KayBee','Kapsabet');
insert into Mashule(code,name,location) Values('3','Machacha','Kapsabet');
insert into Mashule(code,name,location) Values('4','Mastigaveli','zaza');
insert into Mashule(code,name,location) Values('2','kaka','Ndugu');
insert into Mashule(code,name,location) Values('5','Mama','gaga');
insert into Mashule(code,name,location) Values('6','Dada','wawa');
insert into Mashule(code,name,location) Values('7','baba','papa');
insert into Mashule(code,name,location) Values('8','qaqa','yaya');

#querries


