import random
from collections import Counter

def add_noise(preferences):
    """
    Adds random noise (±2%) to each preference, ensures non-negative, and normalizes to 100%.
    """
    noisy_prefs = [p + random.uniform(-2, 2) for p in preferences]
    noisy_prefs = [max(0, p) for p in noisy_prefs]  # Ensure non-negative
    total = sum(noisy_prefs)
    if total == 0:
        return [0] * len(preferences)  # Edge case, unlikely
    normalized = [p / total * 100 for p in noisy_prefs]
    return normalized

def generate_turnout():
    """
    Generates a random voter turnout between 50% and 80%.
    """
    return random.uniform(50, 80)

def simulate_votes(num_voters, preferences, num_parties):
    """
    Simulates votes for each voter based on preference weights.
    Returns a list of vote counts for each party.
    """
    choices = random.choices(range(num_parties), weights=preferences, k=num_voters)
    vote_counts = Counter(choices)
    return [vote_counts.get(i, 0) for i in range(num_parties)]

def calculate_percentages(vote_counts, num_voters):
    """
    Calculates percentages for each party.
    """
    return [ (votes / num_voters * 100) if num_voters > 0 else 0 for votes in vote_counts ]

def print_results(parties, vote_counts, percentages, threshold=5.0):
    """
    Prints the results for each party: votes, percentage, above threshold.
    Returns the winner party.
    """
    print("Výsledky simulace:")
    winner = None
    max_votes = -1
    for i, party in enumerate(parties):
        votes = vote_counts[i]
        perc = percentages[i]
        above_threshold = perc >= threshold
        print(f"{party}: {votes} hlasů, {perc:.2f} %, {'překročila 5% hranici' if above_threshold else 'nepřekročila 5% hranici'}")
        if votes > max_votes:
            max_votes = votes
            winner = party
    print(f"Strana s největším počtem hlasů: {winner}")
    return winner

def print_histogram(parties, percentages):
    """
    Prints a text-based histogram where * represents 1%.
    """
    print("\nTextový histogram výsledků:")
    for i, party in enumerate(parties):
        perc = percentages[i]
        stars = '*' * int(round(perc))
        print(f"{party:<10}: {perc:6.2f} %  {stars}")

def allocate_seats(vote_counts, total_seats=200):
    """
    Allocates seats using D'Hondt method.
    """
    num_parties = len(vote_counts)
    seats = [0] * num_parties
    for _ in range(total_seats):
        quotients = [vote_counts[i] / (seats[i] + 1) for i in range(num_parties)]
        winner = quotients.index(max(quotients))
        seats[winner] += 1
    return seats

def print_mandates(parties, seats):
    """
    Prints the allocated mandates for each party.
    """
    print("\nRozdělení mandátů (pouze strany nad 5%):")
    total_seats = sum(seats)
    for i, party in enumerate(parties):
        if seats[i] > 0:
            print(f"{party}: {seats[i]} mandátů")
    print(f"Celkem přiděleno: {total_seats} mandátů")

def main():
    # Define parties and base preferences
    parties = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]
    base_preferences = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]
    
    # Add noise to preferences
    preferences = add_noise(base_preferences)
    
    # Generate turnout and calculate number of voters
    total_eligible_voters = 8_200_000  # Approximate for Czech Republic
    turnout = generate_turnout()
    num_voters = int(total_eligible_voters * turnout / 100)
    print(f"Volební účast: {turnout:.2f}%")
    print(f"Počet hlasujících voličů: {num_voters}")
    
    # Simulate votes
    vote_counts = simulate_votes(num_voters, preferences, len(parties))
    
    # Calculate percentages
    percentages = calculate_percentages(vote_counts, num_voters)
    
    # Print results
    print_results(parties, vote_counts, percentages)
    
    # Print histogram
    print_histogram(parties, percentages)
    
    # Filter parties above 5% for mandates
    above_threshold_indices = [i for i, p in enumerate(percentages) if p >= 5.0]
    if above_threshold_indices:
        votes_above = [vote_counts[i] for i in above_threshold_indices]
        parties_above = [parties[i] for i in above_threshold_indices]
        seats = allocate_seats(votes_above)
        print_mandates(parties_above, seats)
    else:
        print("\nŽádná strana nepřekročila 5% hranici, žádné mandáty přiděleny.")

if __name__ == "__main__":
    main()