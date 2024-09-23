# Площадь квартиры в квадратных метрах (X)
X = [25,30, 35, 45, 55, 60 , 65, 75, 85, 95, 105, 115]
# Цена квартиры в миллионах тенге (Y)
y = [12,50, 18, 23, 28, 20 ,34, 40, 47, 55, 62, 70]

n = len(X)

sum_x = sum(X)
sum_y = sum(y)
sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_xy += X[i] * y[i]
    sum_x2 += X[i] ** 2
print(sum_xy)
print(sum_x2)

a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
print(a)
b = (sum_y - a * sum_x) / n
print(b)

def predict_price(a, b, area):
    return a * area + b

area = 60
predicted_price = predict_price(a, b, area)
print(f"Предсказанная цена для квартиры площадью {area} кв.м: {round(predicted_price, 4)} млн тенге")

