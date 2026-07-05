'''
Problem statement:
Dispatchers report that the risk engine almost always returns:
LOW
even for deliveries that obviously should be considered high risk.
'''

#Current code 
# def late_risk_label(distance_km, active_orders, weather, pickup_hour):
#     score = 0
#     if distance_km > 20:
#         score += 2
#     if active_orders > 5:
#         score += 2
#     if weather == "storm":
#         score += 3
#     if pickup_hour in (7, 8, 9, 17, 18, 19, 20):
#         score += 1
 

'''
Right now , the function "late_risk_label" calculates a risk score with in total of 8 points. 
based on distance in kilometers, number of active orders, weather conditions, and pickup hour.

while labeling the risk score as "HIGH", "MEDIUM", or "LOW" based on the calculated score.
there is a mistake in the scoring logic. 

Root cause of the problem:
The maximum score that can be achieved is 8, 
but the function checks for scores greater than 10 and 5 to determine the risk label. 
This means that the "HIGH" label will never be assigned because the score never reaches above 8
and the "MEDIUM" label will only be assigned for scores of 6, 7, or 8.
which is why it almost always returns "LOW" even for deliveries that should be considered high risk of being late.
'''

'''
To fix this, we need to adjust the thresholds for the risk labels.
or we can also adjust the scoring logic to allow for a higher maximum score.
'''

#Testing the function with different inputs to see if it returns the expected risk labels.

# risk = late_risk_label(
#     distance_km=35,
#     active_orders=10,
#     weather="storm",
#     pickup_hour=18
# )

#print(risk)
#output: MEDIUM
'''
the HIGH threshold is set above 10, making HIGH unreachable.
'''



# Refactored code with adjusted thresholds for risk labels

def late_risk_label(distance_km, active_orders, weather, pickup_hour):
    score = 0
    HIGH_THRESHOLD = 6
    MEDIUM_THRESHOLD = 3

    if distance_km > 20:
        score += 2

    if active_orders > 5:
        score += 2

    if weather.lower() == "storm":
        score += 3

    if pickup_hour in (7, 8, 9, 17, 18, 19, 20):
        score += 1

    if score >= HIGH_THRESHOLD:
        return "HIGH"
    elif score >= MEDIUM_THRESHOLD:
        return "MEDIUM"
    return "LOW"