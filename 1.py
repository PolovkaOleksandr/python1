from tkinter import *

root = Tk()
root.title("Program")
root.geometry("500x500")

# Create a frame for the button
button_frame = Frame(root)
button_frame.pack(side=RIGHT)

# Create a label above the button
lab1 = Label(button_frame, text="0 дн 0 міс 0 р ")
lab1.pack(side=TOP)
lab2=Label(button_frame, text="0 днів ")
lab2.pack(side=TOP)
lab3=Label(button_frame, text="0 днів ")
lab3.pack(side=TOP)

# Create a button that calls the main function when clicked
def main():
    values1 = [entry.get() for entry in entries1]
    values2 = [entry.get() for entry in entries2]
    days = 0
    months = 0
    years = 0
    daysf1 = 0
    daysf2=0

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
                days = days + day_diff
                if days > 29:
                    days = days - 30
                    months = months + 1
                months = months + month_diff
                if months > 11:
                    months = months - 1
                    years = years + 1
                years = years + year_diff

                if entry31.get():  # Check if the entry is not empty
                    try:
                        days_per_year = float(entry31.get())  # Check if the entry contains a valid number
                        daysf1 = round((years * days_per_year) + (days_per_year / 12 * months) + (days_per_year / 12 / days))
                    except ValueError:
                        lab2.config(text="Invalid number of days per year")
                else:
                    lab2.config(text="Enter number of days per year")
                    
                if entry32.get():
                    daysf2=daysf1-int(entry32.get())
                else:
                    daysf2=daysf1
                

                lab1.config(text=f"{days} дн {months} міс {years} р")
                lab2.config(text=f"{daysf1} днів заробив")
                lab3.config(text=f"{daysf2} днів до компенсації")
                
                
            else:
                labels[i].config(text="")
        except ValueError as e:
            labels[i].config(text=f"Invalid date format: {e}")
                
button = Button(button_frame, text="Запустити", command=main)
button.pack()

# Create three entries below the button

label11s = []
label12s = []
label13s = []

    
label11 = Label(button_frame, text="кільк днів відпустки на рік", font=("Helvetica", 10))
label11.pack()
entry31 = Entry(button_frame, width=20)
entry31.pack()
label12 = Label(button_frame, text="кільк використаних дн", font=("Helvetica", 10))
label12.pack()
entry32 = Entry(button_frame, width=20)
entry32.pack()
label13 = Label(button_frame, text="кільк міс днів", font=("Helvetica", 10))
label13.pack()
entry33 = Entry(button_frame, width=20)
entry33.pack()

# Create a frame for the columns
frame = Frame(root)
frame.pack(side=LEFT)

# Create 15 buttons in each column
entries1 = []
entries2 = []
labels = []
for i in range(15):
    entry1 = Entry(frame, width=10, font=("Helvetica", 10))
    entry1.grid(row=i, column=0, sticky="nsew")
    entries1.append(entry1)

    entry2 = Entry(frame, width=10, font=("Helvetica", 10))
    entry2.grid(row=i, column=1, sticky="nsew")
    entries2.append(entry2)

    label = Label(frame, text="", font=("Helvetica", 10))
    label.grid(row=i, column=2, sticky="nsew")
    labels.append(label)

root.mainloop()