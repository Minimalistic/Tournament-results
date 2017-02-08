-- Kills connections to database, destroys existing and creating the database.

\c vagrant 
SELECT          pg_terminate_backend(pg_stat_activity.pid)
FROM            pg_stat_activity
WHERE           pg_stat_activity.datname = 'tournament'
AND             pid <> pg_backend_pid();
DROP DATABASE   tournament;
CREATE DATABASE tournament;
\c tournament;

-- Creates Players table --
CREATE TABLE Players(
                id          SERIAL,
                name        text,
                PRIMARY KEY (ID)
                );
-- Creates Matches table, has reference id's that link to Players table ID.
CREATE TABLE Matches(
                match_id    SERIAL,
                winner_id   int REFERENCES Players (ID),
                loser_id    int REFERENCES Players (ID),
                PRIMARY KEY (match_id)
                );

-- Views --

-- Creates a losses view --
CREATE VIEW V_losses AS 
    SELECT      Players.id
    AS          ID, COALESCE(COUNT(loser_id),0) AS times
    FROM        Players LEFT JOIN Matches
    ON          Players.id = Matches.loser_id
    GROUP BY    Players.id 
    ORDER BY    times DESC;

-- Creates a wins view --
CREATE VIEW V_wins AS
    SELECT      Players.id as ID, COALESCE(COUNT(winner_id),0) AS times
    FROM        Players LEFT JOIN Matches
    ON          Players.id = Matches.winner_id
    GROUP BY    Players.id 
    ORDER BY    times DESC;

-- Creates a standings view --
CREATE VIEW V_standings AS
    SELECT      V_wins.id AS id, name, V_wins.times AS wins,
                V_losses.times + V_wins.times AS matches
    FROM        Players,
                V_losses,
                V_wins
    WHERE       Players.ID = V_wins.ID AND V_losses.ID = V_wins.ID
    ORDER BY    wins DESC;
