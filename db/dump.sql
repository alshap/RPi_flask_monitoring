create database flask;

create table sensor (sensor_id serial, name text, pin integer, description text null, primary key(sensor_id));
create table sensordata (id serial, sensor_id integer, data float, time timestamp, value_type integer, constraint fk_sensor foreign key(sensor_id) references sensor(sensor_id));
create table device (device_id serial, name text, pin integer, description text null, primary key(device_id));

insert into sensor(name, pin) values ('dht22', 4);
insert into sensor(name, pin) values ('ultrasonic', 17);
insert into sensor(name, pin) values ('resistor', 22);

insert into device(name, pin) values ('red_led', 26);
