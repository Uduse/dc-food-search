# DC Food Search

Search if a food is provided this week in DC at UC Davis. Search is done by scanning DC menu web pages, so it might not be accurate.

## Motivation
I miss menudo and basa fish from Cuarto too much ...

## Usage
`python dc_food_search.py *names`

Names is a list of food names that you want to find in this week DC menus.

Search a single dish:
```
$ python dc_food_search.py oatmeal
Menus successfully retrieved.

Cuarto has oatmeal!  Check it out here: http://dining.ucdavis.edu/res-cuarto-menu.html

Segundo has oatmeal!  Check it out here: http://dining.ucdavis.edu/res-segundo-menu.html

Tercero has oatmeal!  Check it out here: http://dining.ucdavis.edu/res-tercero-menu.html
```

Search multiple dishes:

```
$ python dc_food_search.py oatmeal eggmeal fishmeal
Menus successfully retrieved.

Cuarto has oatmeal!  Check it out here: http://dining.ucdavis.edu/res-cuarto-menu.html

Segundo has oatmeal!  Check it out here: http://dining.ucdavis.edu/res-segundo-menu.html

Tercero has oatmeal!  Check it out here: http://dining.ucdavis.edu/res-tercero-menu.html

Sadly no DC has eggmeal this week, forget about it so you may lose some weight.

Sadly no DC has fishmeal this week, forget about it so you may lose some weight.
```