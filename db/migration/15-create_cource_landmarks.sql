CREATE TABLE IF NOT EXISTS `mokumoku`.`course_landmarks` (
    `id` INT unsigned NOT NULL AUTO_INCREMENT,
    `course_id` INT unsigned NOT NULL,
    `landmark_id` INT unsigned NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4