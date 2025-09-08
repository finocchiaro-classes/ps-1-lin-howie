# number of prior arrests
# 2 are the prior arrests for local ordinance
# Age of release

def calculate_recidivism(prior_arrest, local_ordinance, release_age):
    point_count = 0

    # Determines local_ordinance
    if(local_ordinance == "Y"):
        local_ordinance = True
    else:
        local_ordinance = False

    # Determines recidivism points
    if(prior_arrest >= 2):
        point_count += 1
    if(prior_arrest >= 5):
        point_count += 1
    if(local_ordinance):
        point_count += 1
    if(18 <= release_age <= 24):
        point_count += 1
    if(release_age >= 40):
        point_count -= 1

    """
    if(point_count == -1):
        risk = 11.9
    if(point_count == 0):
        risk = 26.9
    if(point_count == 1):
        risk = 50.0
    if(point_count == 2):
        risk = 73.1
    if(point_count == 3):
        risk = 88.1
    if(point_count == 4):
        risk = 95.3
    """
    
    print(f"The recidivism risk score is {point_count}")

# Inputs
prior_arrest = int(input("Prior arrest: "))
local_ordinance = input("Prior arrests for local ordinance (Y/N): ")
release_age = int(input("Age at release: "))
                        
calculate_recidivism(prior_arrest, local_ordinance, release_age)
