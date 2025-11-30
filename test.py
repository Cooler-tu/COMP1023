import pandas as pd
a1 = pd.Series([1,2,3,4], ['a', 'b', 'c', 'd'])
a2 = pd.Series([5,6,7,8], ['a', 'b', 'c', 'd'])
a3 = pd.Series([9,10,11,12], ['a','c', 'b', 'e'])

data = pd.DataFrame({'A': a1, 'B': a2, 'C': a3})
print(data)