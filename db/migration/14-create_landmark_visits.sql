CREATE TABLE IF NOT EXISTS `mokumoku`.`landmark_visits` (
	`id` INT unsigned NOT NULL AUTO_INCREMENT,
	`workout_history_id` INT unsigned NOT NULL,
	`landmark_id` INT unsigned NOT NULL,
	`time` TIME NOT NULL,
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;