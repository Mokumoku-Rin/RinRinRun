CREATE TABLE IF NOT EXISTS `mokumoku`.`courses` (
	`id` INT unsigned NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(64) NOT NULL,
	`description` TEXT NOT NULL DEFAULT '',
	`mean_distance` INT unsigned NOT NULL,
	`mean_time` INT unsigned NOT NULL COMMENT 'unit ms',
	`played_count` INT unsigned NOT NULL DEFAULT '0',
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
