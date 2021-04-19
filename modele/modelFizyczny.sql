CREATE TABLE `worker` (
  `id_worker` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `birthday` timestamp,
  `gender` ENUM ('male', 'female'),
  `position` ENUM ('Administration', 'Production worker'),
  `login` varchar(255),
  `password` varchar(255),
  `licenses` set
);

CREATE TABLE `machines` (
  `id_machine` int,
  `name` varchar(255),
  `type` ENUM ('Office machine', 'Production machine'),
  `location` int,
  `last_service` timestamp,
  `status` ENUM ('working', 'idle', 'broken')
);

CREATE TABLE `locations` (
  `id_location` int,
  `name` varchar(255),
  `type` ENUM ('production', 'administration')
);

CREATE TABLE `URworker` (
  `id_UR_worker` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `birthday` timestamp,
  `gender` ENUM ('male', 'female'),
  `position` ENUM ('UR worker', 'UR Leader'),
  `login` varchar(255),
  `password` varchar(255),
  `licenses` set,
  `permissions` set,
  `tool_troley` int
);

CREATE TABLE `crashReport` (
  `id_crash_report` int,
  `report_date` timestamp,
  `crashed_machine` int,
  `reporting_worker` int,
  `type` ENUM ('crash', 'warning', 'other', 'collision'),
  `description` varchar(255),
  `UR_worker` int,
  `repair_date` timestamp
);

CREATE TABLE `assigned_location` (
  `id_assigned_location` int,
  `location` int,
  `URworker` int
);

CREATE TABLE `assigned_machine` (
  `id_assigned_location` int,
  `machine` int,
  `worker` int
);

ALTER TABLE `machines` ADD FOREIGN KEY (`location`) REFERENCES `locations` (`id_location`);

ALTER TABLE `crashReport` ADD FOREIGN KEY (`crashed_machine`) REFERENCES `machines` (`id_machine`);

ALTER TABLE `crashReport` ADD FOREIGN KEY (`UR_worker`) REFERENCES `URworker` (`id_UR_worker`);

ALTER TABLE `assigned_location` ADD FOREIGN KEY (`location`) REFERENCES `locations` (`id_location`);

ALTER TABLE `assigned_location` ADD FOREIGN KEY (`URworker`) REFERENCES `URworker` (`id_UR_worker`);

ALTER TABLE `assigned_machine` ADD FOREIGN KEY (`machine`) REFERENCES `machines` (`id_machine`);

ALTER TABLE `assigned_machine` ADD FOREIGN KEY (`worker`) REFERENCES `worker` (`id_worker`);
