CREATE TABLE IF NOT EXISTS `mokumoku`.`workout_histories` (
  `id` INT unsigned NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(64) NOT NULL,
  `course_id` INT unsigned NOT NULL,
  `total_time` INT unsigned NOT NULL,
  `total_distance` INT unsigned NOT NULL,
  `time_list` TEXT NOT NULL,
  `geo_linestring` GEOMETRY NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY(`id`)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;
