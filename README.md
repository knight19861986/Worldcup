
## World Cup Groupping Tool

### Description
A project written in python, containing several scripts to randomize groups for FIFA World Cup 2018, as well as some useful calculation of certain related probabilities.   

### Key Features

- Randomly result a grouping for FIFA World Cup 2018, according to grouping rules of FIFA 
- Calculate the probability of country teams being in one group
- Calculate the probability of a country team avoiding several certain country teams being in the same group

### Requirements
- Python >= 2.7, <3

### Usage

- python groupping_2018.py

- python same_group_2018.py country1 country2 [country3 county4 ...]

- python avoiding_2018.py country1 country2 [country3 county4 ...]

The valid values of "county" could be checked from input_data.py

### Scalability
For other world cup besides 2018, only need to change datas in input_data.py
