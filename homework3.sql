create table if not exists Genre(
	id serial primary key,
	genre_name varchar(80) unique not null
);

create table if not exists Artists(
	id serial primary key,
	artist_name varchar(80) not null
);

create table if not exists GenreArtists(
	genre_id integer not null references Genre(id),
	artist_id integer not null references Artists(id),
	constraint pk primary key (genre_id, artist_id)
);

create table if not exists Albums(
	id serial primary key, 
	album_name varchar(80) not null,
	year_ integer not null	
);

create table if not exists ArtistsAlbums( 
	artist_id integer not null references Artists(id),
	album_id integer not null references Albums(id),
	constraint p_k primary key (album_id, artist_id)	
);

create table if not exists Track( 
	id serial primary key, 
	track_name varchar(80) not null,
	track_time numeric(2,2) not null,
	album_id integer not null references Albums(id)
);

create table if not exists Collection(
	id serial primary key,
	name_ varchar(80) not null,
	year_ integer not null
);

create table if not exists CollectionTrack(
	collection_id integer not null references Collection(id),
	track_id integer not null references Track(id),
	constraint _p_k primary key (collection_id, track_id)
);
