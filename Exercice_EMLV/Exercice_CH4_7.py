# Saisie des données
fighter_size = float(input("What's the size of the fighter in meters ?\n"))
courage_shown = input("Was the soldier courageous? Yes/no\n")
seniority = float(input("How many years have been fighting the soldier ?\n"))
legion_honour = input("Has the soldier the legion of honour? Yes/no\n")


# Conversion en vrais ou faux
fighter_size = bool(fighter_size >= 1.76)
courage_shown = bool(courage_shown.strip().capitalize() == "Yes")
seniority = bool(seniority >= 10)
legion_honour = bool(legion_honour.strip().capitalize() == "Yes")


# Determine if soldier meets all elite unit criteria
'''is_accepted_for_all_conditions = all([fighter_size, courage_shown, seniority]) or legion_honour'''
is_accepted_for_all_conditions = fighter_size and courage_shown and seniority or legion_honour

      
# Display results
print(f"\nCriteria met - Fighter Size: {fighter_size}, Courage Shown: {courage_shown}, Seniority: {seniority}, Legion Honour: {legion_honour}")
print("Accepted into elite unit:", is_accepted_for_all_conditions)