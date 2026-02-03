# Initial setup
ice_cubes = 0
melting_rate = 3
total_minutes = 30

# Simulation loop
for minute in range(1, total_minutes + 1):
    # Phase 1: Add ice at the start of specific minutes
    if minute == 1:
        ice_cubes += 4
    elif minute == 2:
        ice_cubes += 5
    
    # Phase 2: Ice melts during the minute
    # We use max(0, ...) to ensure we don't have negative ice cubes
    ice_cubes = max(0, ice_cubes - melting_rate)
    
    # Optional: Print status for each minute
    print(f"End of minute {minute}: {ice_cubes} cubes left")

print(f"\nFinal result at minute 30: {ice_cubes} cubes.")
