![Swiss Tournament Cover Image](/img/swiss_tournament_cover.jpg)

# Udacity Full Stack Web Developer Nanodegree

## Project: SwissTournamentResults

This project uses a PostgreSQL database to track players and matches in a swiss match style tournament.

## Contents

- [Installation](#installation)
- [Running The Program](#running-the-program)

## Installation Preparation

This program requires a number of things installed for it to run properly.  Install the following:

Python 2.7 [http://docs.python-guide.org/en/latest/starting/installation/][http://docs.python-guide.org/en/latest/starting/installation/]

Vagrant [https://www.vagrantup.com/][https://www.vagrantup.com/]

VirtualBox [https://www.virtualbox.org/][https://www.virtualbox.org/] installed.

## Running The Program

Once installation of the various required programs are completed per your operating system, go to the command line and navigate to the root directory of the program folder and type:

`cd /vagrant`

Press enter and then type:

`vagrant up`

`vagrant ssh`

Once the processes are complete, navigate to the tournament directory:

`cd /vagrant/tournament`

Then type the following to create the database tables necessary for the program to run.

`psql tournament.py`


`\i tournament.sql`

Finally, execute the following to run the test Python file:

`python tournament_test.py`
