
# Define the function to calculate health score
def calculate_health_score(blood_pressure, bmi, gender, sleep_time, age):
    health_score = 0
    
    # Age criteria
    if age < 30:
        health_score += 1
    elif 30 <= age < 40:
        health_score += 1
    elif 40 <= age < 50:
        health_score += 2
    elif 50 <= age < 65:
        health_score += 2
    else:
        health_score += 3
        
    # BMI criteria
    if 18.5 <= bmi < 24.9:
        health_score += 2
    elif 24.9 <= bmi < 27.9:
        health_score += 1
    elif 27.9 <= bmi < 29.9:
        health_score += 1
    
    # Blood Pressure criteria
    if 50 <= blood_pressure <= 60:
        health_score += 1
    elif 60 <= blood_pressure <= 90:
        health_score += 1
    
    # Sleep Time criteria
    if 5 <= sleep_time < 7:
        health_score += 1
    elif 7 <= sleep_time < 9:
        health_score += 1
    
    # Gender criteria
    if gender == 1:
        health_score += 1
    
    # Adjust health score to fit within range [1, 5]
    health_score = min(5, max(1, health_score))
    
    return health_score
