# 209Poll 📉

Welcome to **209poll**.

This project is focused on calculating confidence intervals for election polls to estimate their accuracy and reliability.

## Language and Tools 🛠️

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Language:** Python
- **Compilation:** Via Makefile, including `re`, `clean`, and `fclean` rules.
- **Binary Name:** 209poll

## Project Overview 🔎

The goal of 209poll is to compute 95% and 99% confidence intervals for a given poll.

The project involves applying statistical methods, particularly the binomial distribution converging towards a normal distribution, to determine the reliability of voting intention polls.

### Key Features

- **Confidence Interval Calculation:** Compute 95% and 99% confidence intervals for election polls.
- **Variance Calculation:** Determine the variance of the sample proportion, corrected for finite populations.
- **Command-Line Interface:** Provide a user-friendly interface for input and displaying results.

### Usage

```
∼> ./209poll -h
USAGE
    ./209poll pSize sSize p
DESCRIPTION
    pSize   size of the population
    sSize   size of the sample (supposed to be representative)
    p       percentage of voting intentions for a specific candidate
```

### Exemples

```
∼> ./209poll 10000 500 42.24
Population size:            10000
Sample size:                500
Voting intentions:          42.24%
Variance:                   0.000464
95% confidence interval:    [38.02%; 46.46%]
99% confidence interval:    [36.68%; 47.80%

∼> ./209poll 10000 100 45
Population size:            10000
Sample size:                100
Voting intentions:          45.00%
Variance:                   0.002450
95% confidence interval:    [35.30%; 54.70%]
99% confidence interval:    [32.23%; 57.77%]
2
```

## Installation and Usage 💾

1. Clone the repository.
2. Compile the program using the provided Makefile.
3. Run the program: `./209poll pSize sSize p`.
4. For detailed guidelines, refer to `209poll.pdf`.

## License ⚖️

This project is released under the MIT License. See `LICENSE` for more details.
