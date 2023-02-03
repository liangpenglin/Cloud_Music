CREATE DATABASE `cloudmusic`;
CREATE TABLE  `cloudmusic`.`user_comment` (`musicname` TEXT NOT NULL , `id` INT(100) NOT NULL , `name` TEXT NOT NULL , `comment` TEXT NOT NULL , `likeCound` INT(100) NOT NULL , `timeStr` TEXT NOT NULL, `isvip` TEXT NOT NULL,`vipLevel` INT(20) NOT NULL ,`location` TEXT NOT NULL,`emo_result` TEXT NOT NULL) ENGINE = MyISAM;
