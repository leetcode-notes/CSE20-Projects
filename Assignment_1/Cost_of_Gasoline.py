num_miles = float(input())
fuel_efficiency = float(input())
cost_gasoline = float(input())

final_result = (num_miles/fuel_efficiency) * cost_gasoline

print("%.2f" % final_result)
