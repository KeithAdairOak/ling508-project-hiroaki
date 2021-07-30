Create schema french_words;

CREATE TABLE lexicon (
    id int not null AUTO_INCREMENT,
    form CHARACTER(255),
    pos character(3),
    gender character(1),
    verb_class character(3),
    adj_f CHARACTER(255),
    adj_p CHARACTER(255),
    adj_fp CHARACTER(255),
    definition CHARACTER(255),
    origin_form CHARACTER(255)
    );
