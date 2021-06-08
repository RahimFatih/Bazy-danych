USE BD;

CREATE TABLE `personalData` (
  `id_personal_data` int primary key auto_increment,
  `name` varchar(255),
  `surname` varchar(255),
  `birthday` DATETIME ,
  `gender` ENUM ('male', 'female'),
  `position` int,
  `login` varchar(255),
  `password` varchar(255),
  `licenses` set('Office 360', 'Norton','Jira')
);

CREATE TABLE `machines` (
  `id_machine` int primary key auto_increment,
  `name` varchar(255),
  `last_service` DATETIME ,
  `status` set('Awaria', 'W naprawie', 'Sprawna')
);

CREATE TABLE `crashReport` (
  `id_crash_report` int primary key auto_increment,
  `report_date` DATETIME ,
  `crashed_machine` int,
  `reporting_worker` int,
  `type` set('Awaria całkowita', 'Usterka', 'Kolizja', 'Inny'),
  `description` varchar(255),
  `repair_date` DATETIME 
);

CREATE TABLE `worker_position` (
  `id_worker_position` int primary key auto_increment,
  `worker_position_type` varchar(255)
);


ALTER TABLE `personalData` ADD FOREIGN KEY (`position`) REFERENCES `worker_position` (`id_worker_position`);

ALTER TABLE `crashReport` ADD FOREIGN KEY (`crashed_machine`) REFERENCES `machines` (`id_machine`);

ALTER TABLE `crashReport` ADD FOREIGN KEY (`reporting_worker`) REFERENCES `personalData` (`id_personal_data`);
