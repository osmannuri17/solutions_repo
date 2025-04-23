# Problem 1

# Simulating Sampling Distributions:

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

population_size = 10000
num_samples = 500
sample_sizes = [5, 20, 50]

uniform_population = np.random.uniform(0, 1, population_size)
lambda_param = 2
exponential_population = np.random.exponential(1/lambda_param, population_size)
n_param = 10
p_param = 0.4
binomial_population = np.random.binomial(n_param, p_param, population_size)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(uniform_population, kde=True)
plt.title('Uniform Distribution Population')

plt.subplot(1, 3, 2)
sns.histplot(exponential_population, kde=True)
plt.title('Exponential Distribution Population')

plt.subplot(1, 3, 3)
sns.histplot(binomial_population, kde=True, discrete=True)
plt.title('Binomial Distribution Population')

plt.tight_layout()
plt.show()
```

![alt text](Unknown.png)
