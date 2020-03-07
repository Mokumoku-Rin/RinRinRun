CREATE TABLE IF NOT EXISTS `mokumoku`.`landmarks` (
	`id` INT unsigned NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(64) NOT NULL,
	`description` TEXT NOT NULL DEFAULT '',
	`img_url` TEXT NOT NULL DEFAULT 'https://via.placeholder.com/720x360.png?text=Null+landmark+image',
	`pos` VARCHAR(64) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;