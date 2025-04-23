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


# Parameter Exploration:

***Investigating the effects of the original distribution and sample size.***

We’ll explore how:

The shape of the original distribution (uniform, exponential, binomial) affects the rate of convergence to a normal distribution as the sample size increases.

The population variance influences the spread of the sample mean distribution.

***Key Insights to Explore:***

## Shape of the original distribution:

### For uniform:

The distribution is already flat, so it might converge to normality fairly quickly.

### For exponential:

This is right-skewed, and convergence to normal might take a bit longer.

### For binomial:

Symmetry can form quickly, depending on the number of trials (n) and the probability (p).

### Effect of population variance:

Larger variances in the population will lead to wider spread (more variability) in the sample mean distribution, even as the sample size increases.

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
population_size = 100000
uniform_pop = np.random.uniform(0, 1, population_size)
exponential_pop = np.random.exponential(scale=1, size=population_size)
binomial_pop = np.random.binomial(n=10, p=0.5, size=population_size)
sample_sizes = [5, 10, 30, 50]
n_iterations = 1000
def calculate_variance(sample_means):
    return np.var(sample_means)
def sample_means_from_population(population, sample_sizes, n_iterations):
    sample_means = {}
    
    for size in sample_sizes:
        means = []
        for _ in range(n_iterations):
            sample = np.random.choice(population, size=size)
            means.append(np.mean(sample))
        sample_means[size] = means
    return sample_means
uniform_sample_means = sample_means_from_population(uniform_pop, sample_sizes, n_iterations)
exponential_sample_means = sample_means_from_population(exponential_pop, sample_sizes, n_iterations)
binomial_sample_means = sample_means_from_population(binomial_pop, sample_sizes, n_iterations)
uniform_variances = {size: calculate_variance(means) for size, means in uniform_sample_means.items()}
exponential_variances = {size: calculate_variance(means) for size, means in exponential_sample_means.items()}
binomial_variances = {size: calculate_variance(means) for size, means in binomial_sample_means.items()}
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, list(uniform_variances.values()), label='Uniform', marker='o', color='green')
plt.plot(sample_sizes, list(exponential_variances.values()), label='Exponential', marker='o', color='red')
plt.plot(sample_sizes, list(binomial_variances.values()), label='Binomial', marker='o', color='blue')
plt.title('Variance of Sample Means vs. Sample Size')
plt.xlabel('Sample Size')
plt.ylabel('Variance of Sample Means')
plt.legend()
plt.grid(True)
plt.show()
```

![alt text](graphics.png) 

# Practical Applications:

**Central Limit Theorem (CLT)**:

### 1. **Estimating Population Parameters (Polling)**

- **Scenario**:

 A political pollster wants to estimate the percentage of voters supporting a candidate but can’t survey everyone.

- **How CLT Helps**:

 By sampling a small group (e.g., 1,000 people), the sample mean (percentage of support) will follow a normal distribution, even if the actual voter opinions are not normally distributed.

This allows the pollster to estimate the population’s support with confidence.

### 2. **Quality Control in Manufacturing**

- **Scenario**:

 A factory produces parts and wants to ensure they meet quality standards but can’t check every part.

- **How CLT Helps**:

 The factory samples 30 parts every hour, calculates the sample mean dimension, and checks if it’s within the expected range. CLT ensures that the sample means will be normally distributed, making it easier to detect quality issues.

### 3. **Financial Modeling (Risk Assessment)**

- **Scenario**:

 A financial analyst wants to predict the return of a stock portfolio over a month.

- **How CLT Helps**:

 Even if daily returns are not normally distributed, averaging them over time gives a normal distribution for the sample mean.

This allows the analyst to calculate risks and expected returns more accurately.

### 4. **Medical Research (Average Blood Pressure)**

- **Scenario**:

 Researchers want to estimate the average blood pressure of people with hypertension but can’t measure everyone.

- **How CLT Helps**:

 By sampling 500 patients, the sample mean blood pressure will follow a normal distribution, allowing researchers to estimate the population's average blood pressure with confidence.

### 5. **Consumer Behavior (Average Spending)**

- **Scenario**:

 A company wants to estimate how much customers spend during a sale but can't track every purchase.
 
- **How CLT Helps**:

 By sampling 100 customers, the sample mean spending will be normally distributed. This allows the company to predict the average spending of all customers accurately.

---

### **Key Takeaway**:

The **CLT** helps in situations where you have a large population but can only sample a small group. It ensures that the 

**sample mean**

 will follow a normal distribution, making it easier to estimate population parameters, detect issues, and predict outcomes accurately.



