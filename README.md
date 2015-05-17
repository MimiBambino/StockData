# GoogleTrends
A python class to download google trend data and transform it to a panda dataframe

# Call with the following:

```python
from google_trends import gtrends

gt = gtrends("username", "password") # your google account user name and password
vol = gt.get_volume(terms = ["iphone", "ipad"]) # input search terms as a list, returns daily data
vol2 = gt.get_volume(terms = ["iphone", "ipad"], daily = False) # for weekly data, set daily=False
```

The csv file in the repository is an example of the dataframe output written to csv.
