DROP TABLE kuskin_vuorot;
DROP TABLE kuskit;
DROP TABLE vuorot;

CREATE TABLE kuskit (
	kuski_id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(320) NOT NULL,
	email VARCHAR(320) UNIQUE,
	phone BIGINT,
	reminder_minutes INTEGER NOT NULL DEFAULT 60,
	CONSTRAINT email_to_user_id UNIQUE (email, kuski_id)
);

CREATE TABLE vuorot (
	vuoro_id SERIAL PRIMARY KEY NOT NULL UNIQUE,
	description VARCHAR(320),
	starting_time INTEGER NOT NULL,
	ending_time INTEGER NOT NULL
);


CREATE TABLE kuskin_vuorot (
	kuskin_vuoro_id SERIAL PRIMARY KEY NOT NULL,
	date DATE NOT NULL,
	kuski_id INTEGER NOT NULL REFERENCES kuskit(kuski_id),
	vuoro_id INTEGER NOT NULL REFERENCES vuorot(vuoro_id)
);


