def computepay(hours,hourly_rate):
    if hours <= 40:
        pay = (hours*hourly_rate)
    elif hours > 40:
        pay = (hours-40)*((1.5)*hourly_rate) + (40*hourly_rate)
    return pay


hours = input("Enter Hours:")
hours = float(hours)

hourly_rate = input("Enter rate per hour:")
hourly_rate = float(hourly_rate)

result = computepay(hours,hourly_rate)
print(result)
