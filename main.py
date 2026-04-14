from utils import save_data, load_data
from model import train_model

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    hours = int(input("Study hours: "))
    result = int(input("Result (0=Fail, 1=Pass): "))

    students.append({"hours": hours, "result": result})

save_data(students)

data = load_data()

model = train_model(data)

hours = int(input("Enter hours to predict: "))
pred = model.predict([[hours]])

print("Result:", "Pass" if pred == 1 else "Fail")