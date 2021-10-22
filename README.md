# FIFA 21 Scraper

This repository contains the dataset of FIFA 2021 Player ratings scraped from web.


## Content

This dataset has the following properties:

* Every player in FIFA 21.
* Attributes based on actual data.

```python
>>> df.columns
Index(['Country', 'Flag', 'Short Name', 'Full Name', 'Photo', 'Name', 'Age',
       '↓OVA', 'POT', 'Team & Contract', 'ID', 'Height', 'Weight', 'foot',
       'BOV', 'BP', 'Growth', 'Joined', 'Loan Date End', 'Value', 'Wage',
       'Release Clause', 'Attacking', 'Crossing', 'Finishing',
       'Heading Accuracy', 'Short Passing', 'Volleys', 'Skill', 'Dribbling',
       'Curve', 'FK Accuracy', 'Long Passing', 'Ball Control', 'Movement',
       'Acceleration', 'Sprint Speed', 'Agility', 'Reactions', 'Balance',
       'Power', 'Shot Power', 'Jumping', 'Stamina', 'Strength', 'Long Shots',
       'Mentality', 'Aggression', 'Interceptions', 'Positioning', 'Vision',
       'Penalties', 'Composure', 'Defending', 'Marking', 'Standing Tackle',
       'Sliding Tackle', 'Goalkeeping', 'GK Diving', 'GK Handling',
       'GK Kicking', 'GK Positioning', 'GK Reflexes', 'Total Stats',
       'Base Stats', 'W/F', 'SM', 'A/W', 'D/W', 'IR', 'PAC', 'SHO', 'PAS',
       'DRI', 'DEF', 'PHY', 'Hits'],
      dtype='object')
```

## Acknowledgements

The data has been scraped from the https://sofifa.com website.
