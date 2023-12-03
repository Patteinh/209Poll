import math

def poll(args):
    population_size = int(args[1])
    sample_size = int(args[2])
    voting_intentions = float(args[3]) / 100
    if sample_size > population_size:
        raise Exception("ERROR: sample greater than the population.")
    variance = voting_intentions * (1 - voting_intentions) / sample_size * ((population_size - sample_size) / (population_size - 1))
    confd_95 = [voting_intentions - 1.96 * math.sqrt(variance), voting_intentions + 1.96 * math.sqrt(variance)]
    confd_99 = [voting_intentions - 2.58 * math.sqrt(variance), voting_intentions + 2.58 * math.sqrt(variance)]
    confd_95 = [round(confd_95[0] * 100, 2), round(confd_95[1] * 100, 2)]
    confd_99 = [round(confd_99[0] * 100, 2), round(confd_99[1] * 100, 2)]
    print(f"Population size: \t {population_size}")
    print(f"Sample size: \t         {sample_size}")
    print(f"Voting intentions:\t {voting_intentions * 100:.2f}%")
    print(f"Variance:\t         {variance:.6f}")
    print(f"95% confidence interval: [{confd_95[0]:.2f}%; {confd_95[1]:.2f}%]")
    print(f"99% confidence interval: [{confd_99[0]:.2f}%; {confd_99[1]:.2f}%]")
