create table sensor (sensor_id serial, name text, pin integer, description text null, value_type text [], primary key(sensor_id));
create table sensordata (id serial, sensor_id integer, data float [], time timestamp, constraint fk_sensor foreign key(sensor_id) references sensor(sensor_id));
create table device (device_id serial, name text, pin integer, description text null, primary key(device_id));

insert into sensor(name, pin, value_type) values ('DHT22', 4, ARRAY ['C', '%']);
insert into sensor(name, pin, value_type) values ('ultrasonic', 17, ARRAY ['cm']);
insert into sensor(name, pin, value_type) values ('Photoresistor', 22, ARRAY ['boolean']);

insert into device(name, pin) values ('red_led', 26);
