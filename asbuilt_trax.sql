
--Creates asbuilt_trax database for portfolio project


CREATE TABLE db_mains (
    pk_id SERIAL,
    MAOP INT NOT NULL,
    GEOMETRY TEXT NOT NULL,
    trans BOOLEAN NOT NULL DEFAULT FALSE,
    asbuilts_id INT NOT NULL,
    PRIMARY KEY (pk_id)
);

CREATE TABLE asbuilts (
    pk_id SERIAL,
    work_order TEXT NOT NULL,
    install_Date DATE NOT NULL,
    crew_leader_id INT NOT NULL,
    gis_user_id INT NOT NULL,
    PRIMARY KEY (pk_id)
);

CREATE TABLE gis_users (
    pk_id SERIAL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    PRIMARY KEY (pk_id)
);

CREATE TABLE crew_leaders (
    pk_id SERIAL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    PRIMARY KEY (pk_id)
);

CREATE TABLE asbuilts_gis (
    asbuilt_id INT,
    gis_user_id INT,
    PRIMARY KEY (asbuilt_id, gis_user_id)
);


ALTER TABLE asbuilts
ADD CONSTRAINT fk_asbuilt_crew 
FOREIGN KEY (crew_leader_id) 
REFERENCES crew_leaders(pk_id);

ALTER TABLE db_mains
ADD CONSTRAINT fk_dbmain_asbuilt
FOREIGN KEY (asbuilts_id) 
REFERENCES asbuilts(pk_id);

ALTER TABLE asbuilts_gis
ADD CONSTRAINT fk_asbuilt_gis
FOREIGN KEY (asbuilt_id) 
REFERENCES asbuilts(pk_id);

ALTER TABLE asbuilts_gis
ADD CONSTRAINT fk_gis_asbuilts
FOREIGN KEY (gis_user_id) 
REFERENCES gis_users(pk_id);


INSERT INTO crew_leaders(name, email)
VALUES ('Bill','bill@email.com'), ('Karl','karl@email.gov'), ('Sue', 'sue@altavista.com'),
			('Mike', 'mike@yahoo.com');

INSERT INTO gis_users (name, email)
VALUES ('Harold','harold@hotmail.com'), ('Quentin','q@aol.com')

INSERT INTO asbuilts (work_order,install_Date,crew_leader_id, gis_user_id)
VALUES (0001,'01/15/2022',1,1), (0345,'01/20/2022',2,2), (5468,'05/11/2021',3,2), 
(8887,'04/01/2020',3,2), (4565,'09/04/2021',4,1), (7887,'10/10/2019',4,1);

INSERT INTO db_mains (MAOP,geometry,trans,asbuilts_id)
VALUES (60,'LINE',FALSE,1), (60,'LINE',FALSE,2), (45,'LINE',FALSE,3), 
(400,'LINE',TRUE,4), (800,'LINE',TRUE,5), (55,'LINE',FALSE,5), (60,'LINE',FALSE,6);