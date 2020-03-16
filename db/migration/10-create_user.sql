-- create user table

CREATE TABLE IF NOT EXISTS `mokumoku`.`users` (
	`id` VARCHAR(64) NOT NULL,
	`name` VARCHAR(128) NOT NULL DEFAULT 'email user',
	`img_url` TEXT NOT NULL DEFAULT 'https://via.placeholder.com/128x128?text=User+Image',
	`score` INT NOT NULL DEFAULT '0',
	`total_distance` INT NOT NULL DEFAULT '0' COMMENT 'unit m',
	`total_time` INT NOT NULL DEFAULT '0',
	`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
