# Online Encyclcopedia of Probability Distributions

## Packages to install

Install with `pip install <package>`

```
enum34
scipy
numpy
```


In example distributions (gamma and exponential so far) have a function called goodness_of_fit which for inputted parameters mu, sig2, skew, kurt returns -1,0,1,2,3 corresponding to:
-1 - no fit 
0  - trivial fit
1  - decent fit
2  - good fit
3  - near perfect fit

