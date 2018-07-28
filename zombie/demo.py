temperature = input("temperature")
water = ""
if temperature < 0:
    water = "固态"
elif temperature >= 0 and temperature <= 100:
    water = "液态"
else:
    water = "气态"
