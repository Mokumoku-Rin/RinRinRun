CREATE TABLE IF NOT EXISTS `mokumoku`.`workout_histories` (
	`id` INT unsigned NOT NULL AUTO_INCREMENT,
	`user_id` VARCHAR(64) NOT NULL,
	`cource_id` INT unsigned NOT NULL,
	`geometry_track` LINESTRING NOT NULL,
	`time` TIME NOT NULL,
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(`id`)
) ENGINE=InnoDB;
