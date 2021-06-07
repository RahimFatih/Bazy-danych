create view worker as
select w.id_worker, p.name, p.surname, p.birthday, p.gender, p.position, p.licenses 
from personal_data p inner join worker w;

create view machineFatalCrashHistory as
select crashed_machine, report_date, type, repair_date from crashReport
where type = 'Awaria całkowita';

create view machineWarningHistory as
select crashed_machine, report_date, type, repair_date from crashReport
where type = 'Ostrzeżenie';