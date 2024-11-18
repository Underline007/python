import math

class Circle:
    #tao hinh tron
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    #tinh dien tich
    def area(self):
        return math.pi * self.radius ** 2
    
    #tinh khoang cach tu P den duong tron
    def distance_to_point(self, point):
        x1, y1 = self.center
        x2, y2 = point
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return abs(distance - self.radius)

while True:
    try:
        #nhap khoi tao hinh tron
        center_x = float(input("Enter the x-coordinate of the circle's center: "))
        center_y = float(input("Enter the y-coordinate of the circle's center: "))
        center = (center_x, center_y)
        radius = float(input("Enter the radius of the circle: "))
        #Tao hinh tron va tinh dien tich
        circle = Circle(center, radius)
        area = circle.area()
        print(f"The area of the circle is: {area:.5f}")
        
        
        #nhap khoi tao cua diem P
        point_x = float(input("Enter the x-coordinate of point P: "))
        point_y = float(input("Enter the y-coordinate of point P: "))
        point = (point_x, point_y)
        
        #tinh khoang cach tu P den hinh tron
        distance = circle.distance_to_point(point)
        
        if distance == 0:
            print("The point is on the circle.")
        elif distance < circle.radius:
            print("The point is inside the circle.")
        else:
            print("The point is outside the circle.")
        
        break
    except ValueError:
        print("Invalid input. Please try again.")
        
    --------------------------
Bai 3

import pandas as pd

# Read the data from the Excel file
df = pd.read_excel("workorders.xlsx")

# Print the column names
print(df.columns)

# chuyen doi ngay thang
df['ReqDate'] = pd.to_datetime(df['ReqDate'])
df['WorkDate'] = pd.to_datetime(df['WorkDate'])

# tinh cot wait
df['Wait'] = (df['WorkDate'] - df['ReqDate']).dt.days

# Doc du lieu
print(df['Doc dữ liệu vào DataFrame'].unique())

# xem du lieu thieu
print(df['Xem thông tin dữ liệu: dữ liệu có bao nhiêu thuộc tính, bao nhiêu quan sát, có dữ liệu khuyết hay không?'].unique())

# dem cac loai service
print(df['Lọc dữ liệu để xem có bao nhiêu loại dịch vụ (Service) khác nhau được cung cấp, và là những loại nào?'].unique())

# Tinh LbrCost
df['LbrCost'] = df['LbrHrs'] * df['LbrRate']

# Tinh 'TotalCost' va 'TotalFee' 
df['TotalCost'] = df['LbrCost'] + df['PartsCost']
df['TotalFee'] = df['LbrCost'] + df['PartsFee']

# Filter the data based on the instructions
filtered_df = df[df['File excel "workorders.xlsx"'] == 'workorders.xlsx']

# Print the filtered data
print(filtered_df)
       
