Python 3.7.0b3 (v3.7.0b3:4e7efa9c6f, Mar 29 2018, 18:42:04) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> col_name = ['user_id','item_id','rating','timestamp']
>>> path = 'https://media.geeksforgeeks.org/wp-content/uploads/file.tsv'
>>> df=pd.read_csv(path,sep='\t',names=col_name)
>>> df.head()
   user_id  item_id  rating  timestamp
0        0       50       5  881250949
1        0      172       5  881250949
2        0      133       1  881250949
3      196      242       3  881250949
4      186      302       3  891717742
>>> movie_titles = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv')
			       
>>> movie_titles.head(10)
			       
   item_id                                              title
0        1                                   Toy Story (1995)
1        2                                   GoldenEye (1995)
2        3                                  Four Rooms (1995)
3        4                                  Get Shorty (1995)
4        5                                     Copycat (1995)
5        6  Shanghai Triad (Yao a yao yao dao waipo qiao) ...
6        7                              Twelve Monkeys (1995)
7        8                                        Babe (1995)
8        9                            Dead Man Walking (1995)
9       10                                 Richard III (1995)
>>> data = pd.merge(df,movie_titles,on = 'item_id')
			       
>>> data.head()
			       
   user_id  item_id  rating  timestamp             title
0        0       50       5  881250949  Star Wars (1977)
1      290       50       5  880473582  Star Wars (1977)
2       79       50       4  891271545  Star Wars (1977)
3        2       50       5  888552084  Star Wars (1977)
4        8       50       5  879362124  Star Wars (1977)
>>> data.groupby('title')['rating'].mean().head()
			       
title
'Til There Was You (1997)    2.333333
1-900 (1994)                 2.600000
101 Dalmatians (1996)        2.908257
12 Angry Men (1957)          4.344000
187 (1997)                   3.024390
Name: rating, dtype: float64
>>> data.groupby('item_id')['rating'].mean().sort_values(ascending=False).head()
			       
item_id
1293    5.0
1467    5.0
1653    5.0
814     5.0
1122    5.0
Name: rating, dtype: float64
>>> data.groupby('title')['rating'].count().sort_values(ascending=False).head()
			       
title
Star Wars (1977)             584
Contact (1997)               509
Fargo (1996)                 508
Return of the Jedi (1983)    507
Liar Liar (1997)             485
Name: rating, dtype: int64
>>> ratings = pd.DataFrame(data.groupby('title')['rating'].mean())
			       
>>> ratings['total ratings']=pd.DataFrame(data.groupby('title')['rating'].count())
			       
>>> ratings.head()
			       
                             rating  total ratings
title                                             
'Til There Was You (1997)  2.333333              9
1-900 (1994)               2.600000              5
101 Dalmatians (1996)      2.908257            109
12 Angry Men (1957)        4.344000            125
187 (1997)                 3.024390             41
>>> 
