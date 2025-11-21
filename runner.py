from rng import roulette_like_trial, set_seed

def run_simulation(strategy_fn, initial_funds, stake, n_rounds,
                   n_bettors, p_win=0.49, seed=None, **kwargs):
    
    if seed is not None:
        set_seed(seed)

    final_values = []
    broke_count = 0

    def rng():
        return roulette_like_trial(p_win)

    for i in range(n_bettors):
        wagers, values = strategy_fn(initial_funds, stake, n_rounds, rng, **kwargs)

        # Final bankroll for this bettor
        if len(values) == 0:
            final = initial_funds
        else:
            final = values[-1]

        final_values.append(final)

        if final <= 0:
            broke_count += 1

    return final_values, broke_count

