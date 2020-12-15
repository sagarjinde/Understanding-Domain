# Understanding Domain

## Objective
- Scrape data of a specific domain
- Understand the domain in terms of word similarity and document similarity

## Get Started

Domain of choice: Games

Word similarity is calculated using word2vec 

Document similarity is calculated using doc2vec

## Observations

### Observations about clusters formed

![word2vec_50](https://github.com/sagarjinde/Understanding_Domain/blob/main/figs/word2vec50.png)

- The light blue cluster contains terms that are used as a mode of dealing
damage. Terms like 'ability', 'weapon', 'combat', 'attack' are present in this
cluster.

- The red cluster contains terms that define the environment of the game.
Words like 'puzzle', 'place', 'world', 'life', 'time', experience', 'story' are present
in this cluster.

- The light green cluster contains terms that defines the mode of play. That
is, it tells us if the game is a single player game, two player game or a team
game. Words like 'player', 'team', 'two', 'one' are present in this cluster.

The purple cluster contains terms that are used to explain the game objective. 
Terms like 'map', 'mission', 'battle', 'system', 'level' are present in this
cluster.

![word2vec_100](https://github.com/sagarjinde/Understanding_Domain/blob/main/figs/word2vec100.png)

### Observations about words
Following are few words that appear close to each other
| Word 1 | Word 2 |
| --- | --- |
| team | player |
|play | playing |
| puzzle | mechanics |
| ability | weapons |
| get | back |
| series | game |

### Observations on documents

![doc2vec](https://github.com/sagarjinde/Understanding_Domain/blob/main/figs/doc2vec.png)

**Games in light green clusters**
- FIFA 18 (Football)
- Ashes Cricket (Cricket)
- PES 2019 (Football)
- F1 2019 (Car racing)
- FIFA 19 (Football)
- FIFA 19 Nintendo switch (Football)
- MLB The Show 19 (Baseball)
- NHL 19 (Ice Hockey)

**Observation:** This cluster contains sports games.

**Games in purple cluster:**
- Fortnite
- PUBG
- H1Z1
- Far Cry 5
- Monster Hunter Generations Ultimate
- Monster Hunter World
- Middle-earth: Shadow Of War

**Observation:** This cluster contains Open world fighting games.

**Games in light blue cluster:**
- Transference
- Perception
- Hellblade: Senua's Sacrifice
- Star Wars Jedi: Fallen Order
- Subnautica
- Outer Wilds
- Darq

**Observation:** This cluster contains puzzle based games. Such games gen-
erally fall under action, adventure and horror genre.

**Games in red cluster:**
- The Walking Dead: The Final Season Episode 3
- The Walking Dead: The Final Season Episode 2
- The Walking Dead - The Final Season Episode 1
- Night Call
- Life Is Strange: Before The Storm
- Life Is Strange: Before The Storm - Episode 1
- Cosmic Top Secret

**Observation:** This cluster contains Adventure games.

**General game observations:**
- Games that belong to the same series are close by
- Maximum intra-cluster similarity was seen in sports category. The reason
behind this might be because other genre game have multiple ways to describe
them, but for sports games, we can review in only a few specific ways using
sports terminology.
- Games in light blue and red cluster are almost similar. The reason is because
almost all adventure games contain some sort of puzzles in them. Few games
in red cluster can also be considered as a part of blue cluster because of their
striking similarities.

## Running the code

`Python version: 3.6.8`

### Create a virtual environment (Recommended but optional)
Install virtualenv  : `sudo apt-get install virtualenv` </br>
Create virtualenv   : `virtualenv --system-site-packages -p python3 ./venv` </br>
Activate virtualenv : `source venv/bin/activate` </br>

### Install Requirements
Run `pip install -r requirements.txt`

Run `python understand.py`

## Custom Dataset 

### Generate Data
Provide website URL in `./assign1/spiders/game_review.py`

To generate data (crawling), run `scrapy crawl game_review` command. This will create a folder `asdf` and gameCSV file inside which game reviews `.txt` files 
and metadata about scraped data is stored respectively.

**Note:** System on which this code is executing should be initially connected to the internet to download stopwords and punkt.