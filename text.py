'''

-------------
Adding tables
-------------


Adding a table for genre
---

CREATE TABLE  Genre (
	id INTEGER NOT NULL PRIMARY  KEY AUTOINCREMENT UNIQUE,
	name TEXT
)


Adding an table for ALbum
---

CREATE TABLE  Album (
	id INTEGER NOT NULL PRIMARY  KEY AUTOINCREMENT UNIQUE,
	artist_id INTEGER,
	title TEXT
)


Adding a table for Track
---

CREATE TABLE  Track (
	id INTEGER NOT NULL PRIMARY  KEY AUTOINCREMENT UNIQUE,
	title TEXT,
	album_id INTEGER,
	genre_id INTEGER,
	len INTEGER, rating INTEGER, count INTEGER
)


--------------
Inserting data
--------------


- build tables from the outside in, so starting from thefurthest brance and work to the most inner one, track being the inner one in this case.
- When using foregn keys, use numbers instead of strings because it saves a lot of time when searching big data!

Inserting an artist
---
Insert Into Artist (name) VALUES ("AC/DC")


Inserting a genre
---
Insert Into Genre (name) VALUES ("Rock");


Inserting an album
---
Insert Into Album (title,  artist_id) VALUES ("Who Made Who", 2);


Inserting track
---
Insert Into Track (title,  rating, len, count, album_id, genre_id) VALUES ("Black Dog",  5, 297, 0, 2, 1);


-------------
Joining data
------------

Joining the albums with the artist
---
SELECT Album.title, Artist.name from Album JOIN Artist on Album.artist_id = Artist.id


Joining the genre with the tracks 
---
SELECT Track.title, Genre.name from Track JOIN Genre on Track.genre_id = Genre.id


Joining the track title, artist name, album title, and the genre name
---
SELECT Track.title, Artist.name, Album.title, Genre.name from 
Track JOIN Genre join Album join Artist on Track.genre_id = Genre.id
and Track.album_id = Album.id and Album.artist_id = Artist.id


Join
---
SELECT User.name, Member.role, Course.title FROM User JOIN 
Member JOIN Course ON Member.user_id = User.id AND 
Member.course_id = Course.id ORDER BY Course.title, Member.role DESC, User.name


'''


import os


print(os.path.dirname(__file__))
