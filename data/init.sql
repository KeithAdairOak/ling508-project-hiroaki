CREATE DATABASE french_words;
#ALTER DATABASE french_words CHARACTER SET utf8 collate utf8_unicode_ci;
USE french_words;
    CREATE TABLE lexicon (
        id int not null AUTO_INCREMENT,
        entry NVARCHAR(255),
        form NVARCHAR(255),
        pos VARCHAR(3),
        gender VARCHAR(1),
        verb_class VARCHAR(3),
        adj_f VARCHAR(255),
        adj_p VARCHAR(255),
        adj_fp VARCHAR(255),
        definition VARCHAR(255),
        origin_form VARCHAR(255),
        primary key (id)
        );

