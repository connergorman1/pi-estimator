# Pi Estimator

Pi can be estimated by sampling random integers and looking at the ratio between
the total number of samples and the number of samples that are co-prime (i.e. $\`gcd(a,b)=1$\`).

For reasons I don't fully remember, we have the fact that: 
$$\lim_{n \to \inf} \frac{\left( number of co-prime \right)}{n} = \frac{6}{\pi}$$
