USE BD;

CREATE TABLE `worker` (
  `id_worker` int primary key auto_increment,
  `personal_data` int
);

CREATE TABLE `URworker` (
  `id_UR_worker` int primary key auto_increment,
  `personal_data` int,
  `permissions` set('SEP E', 'SEP D', '1WJO','2WJO','3WJO'),
  `tool_troley` int
);

CREATE TABLE `personalData` (
  `id_personal_data` int primary key auto_increment,
  `name` varchar(255),
  `surname` varchar(255),
  `birthday` date,
  `gender` ENUM ('male', 'female'),
  `position` int,
  `login` varchar(255),
  `password` varchar(255),
  `licenses` set('Office 360', 'Norton','Jira')
);

CREATE TABLE `machines` (
  `id_machine` int primary key auto_increment,
  `name` varchar(255),
  `type` int,
  `location` int,
  `last_service` timestamp,
  `status` int
);

CREATE TABLE `locations` (
  `id_location` int primary key auto_increment,
  `name` varchar(255),
  `type` int
);

CREATE TABLE `crashReport` (
  `id_crash_report` int primary key auto_increment,
  `report_date` timestamp,
  `crashed_machine` int,
  `reporting_worker` int,
  `type` int,
  `description` varchar(255),
  `UR_worker` int,
  `repair_date` timestamp
);

CREATE TABLE `assigned_location` (
  `id_assigned_location` int primary key auto_increment,
  `location` int,
  `URworker` int
);

CREATE TABLE `assigned_machine` (
  `id_assigned_location` int primary key auto_increment,
  `machine` int,
  `worker` int
);

CREATE TABLE `report_type` (
  `id_report_type` int primary key auto_increment,
  `report_type_name` varchar(255)
);

CREATE TABLE `location_type` (
  `id_location_type` int primary key auto_increment,
  `location_type_name` varchar(255)
);

CREATE TABLE `machine_status` (
  `id_machine_status` int primary key auto_increment,
  `machine_status_name` varchar(255)
);

CREATE TABLE `worker_position` (
  `id_worker_position` int primary key auto_increment,
  `worker_position_type` varchar(255)
);

CREATE TABLE `machine_type` (
  `id_machine_type` int primary key auto_increment,
  `machine_type_name` varchar(255)
);

ALTER TABLE `worker` ADD FOREIGN KEY (`personal_data`) REFERENCES `personalData` (`id_personal_data`);

ALTER TABLE `URworker` ADD FOREIGN KEY (`personal_data`) REFERENCES `personalData` (`id_personal_data`);

ALTER TABLE `personalData` ADD FOREIGN KEY (`position`) REFERENCES `worker_position` (`id_worker_position`);

ALTER TABLE `machines` ADD FOREIGN KEY (`type`) REFERENCES `machine_type` (`id_machine_type`);

ALTER TABLE `machines` ADD FOREIGN KEY (`location`) REFERENCES `locations` (`id_location`);

ALTER TABLE `machines` ADD FOREIGN KEY (`status`) REFERENCES `machine_status` (`id_machine_status`);

ALTER TABLE `locations` ADD FOREIGN KEY (`type`) REFERENCES `location_type` (`id_location_type`);

ALTER TABLE `crashReport` ADD FOREIGN KEY (`crashed_machine`) REFERENCES `machines` (`id_machine`);

ALTER TABLE `crashReport` ADD FOREIGN KEY (`type`) REFERENCES `report_type` (`id_report_type`);

ALTER TABLE `crashReport` ADD FOREIGN KEY (`UR_worker`) REFERENCES `URworker` (`id_UR_worker`);

ALTER TABLE `assigned_location` ADD FOREIGN KEY (`location`) REFERENCES `locations` (`id_location`);

ALTER TABLE `assigned_location` ADD FOREIGN KEY (`URworker`) REFERENCES `URworker` (`id_UR_worker`);

ALTER TABLE `assigned_machine` ADD FOREIGN KEY (`machine`) REFERENCES `machines` (`id_machine`);

ALTER TABLE `assigned_machine` ADD FOREIGN KEY (`worker`) REFERENCES `worker` (`id_worker`);
