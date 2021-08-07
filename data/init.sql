DROP DATABASE IF EXISTS french_words;
CREATE DATABASE french_words;
#ALTER DATABASE french_words CHARACTER SET utf8 collate utf8_unicode_ci;
USE french_words;
    CREATE TABLE lexicon (
        id int not null AUTO_INCREMENT,
        entry NVARCHAR(255),
        form NVARCHAR(255),
        pos VARCHAR(10),
        gender VARCHAR(10),
        verb_class VARCHAR(10),
        form_f VARCHAR(255),
        form_p VARCHAR(255),
        form_fp VARCHAR(255),
        definition VARCHAR(255),
        origin_form VARCHAR(255),
        primary key (id)
        );

