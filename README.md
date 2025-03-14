# Pi Estimator

Pi can be estimated by sampling random integers and looking at the ratio between
the total number of samples and the number of samples that are co-prime (i.e. $\gcd(a,b)=1$\).

For reasons I don't fully remember, we have the fact that: 

$$\lim_{n \to \infty} \mu = \frac{6}{\pi^{2}}$$ 

where $\mu$ is the number coprime integers sampled from $1,n$ divided by $n$.

Therefore, we have a formula for estimating $\pi$

$$\pi = \sqrt{6}{\mu}$$
