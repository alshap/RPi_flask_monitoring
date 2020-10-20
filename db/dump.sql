create table sensor (sensor_id serial, name text, pin integer, description text null, value_type text [], primary key(sensor_id));
create table sensordata (id serial, sensor_id integer, data float [], time timestamp, constraint fk_sensor foreign key(sensor_id) references sensor(sensor_id));
create table device (device_id serial, name text, pin integer, description text null, primary key(device_id));

insert into sensor(name, pin, value_type) values ('ValuesTest', 4, ARRAY ['C', '%', 'distance', 'pressure']);
insert into sensor(name, pin, value_type) values ('ValuesTest2', 17, ARRAY ['cm', '%']);

insert into device(name, pin) values ('red_led', 26);
