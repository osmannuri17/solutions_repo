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

# Sampling and Visualization:

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for seaborn
sns.set(style="whitegrid")

# Parameters
sample_sizes = [5, 10, 30, 50]
n_repeats = 1000
population_size = 100000

# Distributions to simulate
distributions = {
    "Uniform": np.random.uniform(0, 100, population_size),
    "Exponential": np.random.exponential(scale=10, size=population_size),
    "Binomial": np.random.binomial(n=20, p=0.5, size=population_size),
}

# Create subplots
fig, axs = plt.subplots(len(distributions), len(sample_sizes), figsize=(20, 12))
fig.suptitle('Sampling Distributions of the Sample Mean for Different Populations and Sample Sizes', fontsize=16)

# Loop over each distribution
for i, (dist_name, population) in enumerate(distributions.items()):
    # Loop over each sample size
    for j, sample_size in enumerate(sample_sizes):
        sample_means = []
        for _ in range(n_repeats):
            sample = np.random.choice(population, size=sample_size, replace=False)
            sample_means.append(np.mean(sample))
        # Plot histogram of sample means
        ax = axs[i, j]
        sns.histplot(sample_means, kde=True, ax=ax, stat="density", color="skyblue", bins=30)
        ax.set_title(f'{dist_name} Dist - Sample Size {sample_size}')
        ax.set_xlabel('Sample Mean')
        ax.set_ylabel('Density')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

```

![alt text](Unknown-3.png) 
