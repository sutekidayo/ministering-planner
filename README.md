# Ministering Planner   

Simple python scripts to pull data from lcr.lds.org and the LDS Tools App APIs.

Also includes a simple webapp to better digest the data and inspect ministering assignments and update assignments 
without affecting live data.

Everything is stored locally on your machine, and nothing is sent to Google except for latitude and longitude when 
mapping markers.

## Getting the data
The first thing you will need to do is create a `config.ini` at the root of the repo, 
(see `sample.config.ini` for a template).  This is required to authenticate against lds.org and gain access to the 
various APIs.

Next, you need to run `get_data.py` which will generate a bunch of .json files in the `data/` folder.

If anything fails, make sure you have the appropriate roles in LCR/MLS for the account you have entered in config.ini, 
and that your username and password works.

## Viewing the data
In Development!

Some plans for how to view the data:
* Filter members based on unit-statistics and drop pins on the map
* Highlight households within companionship assignments and drop them on a map with a color per companionship
* Highlight households without ministers
* for any member draw them on the map and their ministering assignment and / or the brother's
 assigned to minister to them.
