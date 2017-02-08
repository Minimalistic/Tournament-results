#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<Error, no database found.>")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor.execute("TRUNCATE Matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor.execute("TRUNCATE Players CASCADE")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    query = ("SELECT COUNT(*) FROM Players;")
    cursor.execute(query)
    count = cursor.fetchone()
    db.close()
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database."""
    db, cursor = connect()
    query = "INSERT INTO Players(name) VALUES (%s);"
    parameter = (name,)
    cursor.execute(query, parameter)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    query = ("SELECT * FROM V_standings;")
    cursor.execute(query)
    V_standings = cursor.fetchall()
    db.close()
    return V_standings


def reportMatch(winner_id, loser_id):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    match_result = ("INSERT INTO Matches (winner_id, loser_id) VALUES (%s, %s)")
    cursor.execute(match_result, (winner_id, loser_id))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    player = [item[0:2] for item in standings]
    index = 0
    pair1 = player[index] + player[index+1]
    pair2 = player[index+2] + player[index+3]
    pair3 = player[index+4] + player[index+5]
    pair4 = player[index+6] + player[index+7]
    combined_swissPairings = ((pair1, pair2, pair3, pair4))
    return combined_swissPairings
