CREATE TABLE IF NOT EXISTS `mokumoku`.`cources` (
	`id` INT unsigned NOT NULL AUTO_INCREMENT,
	`landmark_id` INT unsigned NOT NULL,
	`played_count` INT unsigned NOT NULL DEFAULT '0',
	`difficulity` TINYINT unsigned NOT NULL DEFAULT '0',
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;