Git help:
https://github.com/KalleHallden/FinanceAutomation/blob/master/.gitignore

1. Leer datos de CVS
2. Separar y organizar:
   
   `Fecha`, `entrada o salida`, `cantidad`,`estado de cuenta`
   
3. sumar `salidas` y así mismo `entradas`
4. Aplicar a estado de cuenta y obtenr el balance.

___
## Understanding [Pandas](https://pandas.pydata.org/docs/user_guide/dsintro.html#dsintro)

[_Data structures_](https://pandas.pydata.org/docs/user_guide/dsintro.html#dsintro)

***Series***

    s= pd.Series(data, index=index)

e.g.
~~~
s= pd.Series(np.random.rand(5), index=["a","b","c","d","e"])

print(s)

Out
a    0.214499
b    0.725041
c    0.067285
d    0.604419
e    0.343110
dtype: float64
~~~
if we don't specify the index, then by the fault enumerates the elements.
~~~
s= pd.Series(np.random.rand(5))

print(s)

Out
0    0.630581
1    0.977345
2    0.048337
3    0.665574
4    0.117142
dtype: float64
~~~
***Data frame***
    
    pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)

e.g.

~~~
dates = pd.date_range("20130101", periods=6)
print(dates)

Out
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
~~~