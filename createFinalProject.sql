-- Clean out the old teefile; likely this command is system specific
\! rm -f creation.txt
tee creation.txt;

-- Show warnings after every statement
warnings;

drop table if exists WeeklyTesting;
drop table if exists Deaths;
drop table if exists Recovered;
drop table if exists Transmissions;
drop table if exists BackgroundInfo;
drop table if exists Location;

select '----------------------------------------------------------------' as '';
select 'Location' as '';

create table Location (
			region int,
			groupName varchar(255),
			provinces varchar(255),
            -- Constraints
            primary key (region),
            check (region != '')
		       );

load data infile '/var/lib/mysql-files/finalProject/Location.csv' ignore into table Location
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\r\n'
     ignore 1 lines;

select '----------------------------------------------------------------' as '';
select 'Weekly Testing' as '';

create table WeeklyTesting (
			region int,
			abbreviation varchar(2),
			episodeWeek decimal(2),
			dailyTested int,
            -- Constraints
			foreign key (region) references Location(region)
		       );

load data infile '/var/lib/mysql-files/finalProject/Weekly_Testing.csv' ignore into table WeeklyTesting
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\r\n'
     ignore 1 lines;

select '----------------------------------------------------------------' as '';
select 'Background Info' as '';

create table BackgroundInfo (
            caseID int NOT NULL AUTO_INCREMENT,
			region int,
			episodeWeek decimal(2),
			gender decimal(1),
			ageGroup decimal(2),
			occupation decimal(1),
-- Constraints
			primary key (caseID),
			foreign key (region) references Location(region)
		       );

load data infile '/var/lib/mysql-files/finalProject/Background_Info.csv' ignore into table BackgroundInfo
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\r\n'
     ignore 1 lines;

select '----------------------------------------------------------------' as '';
select 'Deaths' as '';

create table Deaths (
            caseID int,
			hospitalStatus decimal(1),
-- Constraints
            primary key (caseID),
			foreign key (caseID) references BackgroundInfo(caseID)
		       );

load data infile '/var/lib/mysql-files/finalProject/Deaths.csv' ignore into table Deaths
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\r\n'
     ignore 1 lines;

select '----------------------------------------------------------------' as '';
select 'Recovered' as '';

create table Recovered (
            caseID int,
			hospitalStatus decimal(1),
            episodeWeek decimal(2),
-- Constraints
            primary key (caseID),
			foreign key (caseID) references BackgroundInfo(caseID)
		       );

load data infile '/var/lib/mysql-files/finalProject/Recovered.csv' ignore into table Recovered
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\r\n'
     ignore 1 lines;


select '----------------------------------------------------------------' as '';
select 'Transmissions' as '';

create table Transmissions(
            caseID int,
			asymptomatic decimal(1),
            onsetweekofsymptoms decimal(2),
            tranmissions decimal(1),
-- Constraints
            primary key (caseID),
			foreign key (caseID) references BackgroundInfo(caseID)
		       );

load data infile '/var/lib/mysql-files/finalProject/Transmissions.csv' ignore into table Transmissions
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\r\n'
     ignore 1 lines;

nowarning
notee