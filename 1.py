from tkinter import *

root = Tk()
root.title("Program")
root.geometry("400x500")

# Create a frame for the button
button_frame = Frame(root)
button_frame.pack(side=RIGHT)

# Create a label above the button
lab1 = Label(button_frame, text="0 дн 0 міс 0 р ")
lab1.pack(side=TOP)

# Create a button that calls the main function when clicked
def main():
    values1 = [entry.get() for entry in entries1]
    values2 = [entry.get() for entry in entries2]
    days=0
    months=0
    years=0
    for i, (value1, value2) in enumerate(zip(values1, values2)):
        try:
            parts1 = value1.split('.')
            parts2 = value2.split('.')

            if len(parts1) == 3 and len(parts2) == 3:
                day1, month1, year1 = map(int, parts1)
                day2, month2, year2 = map(int, parts2)

                day_diff = day2 - day1
                if day_diff < 0:
                    day_diff += 30
                    month_diff = month2 - month1 - 1
                else:
                    month_diff = month2 - month1

                if month_diff < 0:
                    month_diff += 12
                    year_diff = year2 - year1 - 1
                else:
                    year_diff = year2 - year1

                
                labels[i].config(text=f"{day_diff} дн {month_diff} міс {year_diff} р")
                days=days+day_diff
                if days>29:
                    days=days-30
                    months=months+1
                months=months+month_diff
                if months>11:
                    months=months-1
                    years=years+1
                years=years+year_diff
                lab1.config(text=f"{days} дн {months} міс {years} р")
            else:
                labels[i].config(text="")
        except ValueError as e:
            labels[i].config(text=f"Invalid date format: {e}")
                
button = Button(button_frame, text="Запустити", command=main)
button.pack()

# Create three entries below the button
entries3 = []
for i in range(3):
    entry = Entry(button_frame, width=20)
    entry.pack()
    entries3.append(entry)

# Create two frames for the columns
frame1 = Frame(root)
frame1.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(side=LEFT)
frame3 = Frame(root)
frame3.pack(side=LEFT)

# Create 15 buttons in each column
entries1 = []
for i in range(15):
    entry = Entry(frame1, width=20)
    entry.pack()
    entries1.append(entry)

entries2 = []
for i in range(15):
    entry = Entry(frame2, width=20)
    entry.pack()
    entries2.append(entry)

labels = []
for i in range(15):
    label = Label(frame3, text="")
    label.pack()
    labels.append(label)

root.mainloop()