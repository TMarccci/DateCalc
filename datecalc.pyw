__author__ = "Tihanyi Marcell"


from tkinter import *
from tkinter import messagebox


def clearAll():
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)
    messagebox.showinfo("Dates cleared", "Success!")


def checkError():
    if (dayField.get() == "" or monthField.get() == ""
            or yearField.get() == "" or givenDayField.get() == ""
            or givenMonthField.get() == "" or givenYearField.get() == ""):
        messagebox.showerror("Input Error", "Incorrect format or nothing in input field!")

        return -1


def calculateAge():
    value = checkError()

    if value == -1:
        return

    else:

        rsltDayField.delete(0, END)
        rsltMonthField.delete(0, END)
        rsltYearField.delete(0, END)

        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())

        given_day = int(givenDayField.get())
        given_month = int(givenMonthField.get())
        given_year = int(givenYearField.get())

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if birth_day > given_day:
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]

        if birth_month > given_month:
            given_year = given_year - 1
            given_month = given_month + 12

        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year

        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))


def themasterguy():
    messagebox.showinfo("The program made by TMarccci", "Thanks for downloading it!")


if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="#edece8")

    gui.title("Age Calculator")

    gui.geometry("260x320")

    gui.iconbitmap("calendar-512.ico")

    dob = Label(gui, text="Date Of Birth")
    givenDate = Label(gui, text="Current Date or Dead date")
    age = Label(gui, text="Age")

    day = Label(gui, text="Day", bg="#edece8")
    month = Label(gui, text="Month", bg="#edece8")
    year = Label(gui, text="Year", bg="#edece8")

    givenYear = Label(gui, text="Given Year", bg="#edece8")
    givenMonth = Label(gui, text="Given Month", bg="#edece8")
    givenDay = Label(gui, text="Given Day", bg="#edece8")

    rsltDay = Label(gui, text="Days", bg="#edece8")
    rsltMonth = Label(gui, text="Months", bg="#edece8")
    rsltYear = Label(gui, text="Years", bg="#edece8")

    resultantAge = Button(gui, text="Calculate", fg="Black", command=calculateAge)
    clearAllEntry = Button(gui, text="Clear All", fg="Black", command=clearAll)
    creator = Button(gui, text="Credits", command=themasterguy)

    yearField = Entry(gui)
    monthField = Entry(gui)
    dayField = Entry(gui)

    givenYearField = Entry(gui)
    givenMonthField = Entry(gui)
    givenDayField = Entry(gui)

    rsltYearField = Entry(gui)
    rsltMonthField = Entry(gui)
    rsltDayField = Entry(gui)

    dob.grid(row=0, column=1)
    day.grid(row=3, column=0)
    dayField.grid(row=3, column=1)
    month.grid(row=2, column=0)
    monthField.grid(row=2, column=1)
    year.grid(row=1, column=0)
    yearField.grid(row=1, column=1)

    givenYear.grid(row=5, column=0)
    givenYearField.grid(row=5, column=1)
    givenMonth.grid(row=6, column=0)
    givenMonthField.grid(row=6, column=1)
    givenDay.grid(row=7, column=0)
    givenDayField.grid(row=7, column=1)
    givenDate.grid(row=4, column=1)

    age.grid(row=8, column=1)
    rsltDay.grid(row=11, column=0)
    rsltDayField.grid(row=11, column=1)
    rsltMonth.grid(row=10, column=0)
    rsltMonthField.grid(row=10, column=1)
    rsltYear.grid(row=9, column=0)
    rsltYearField.grid(row=9, column=1)

    clearAllEntry.grid(row=17, column=1)
    resultantAge.grid(row=16, column=1)
    age.grid(row=8, column=1)
    creator.grid(row=17, column=0)

    gui.mainloop()
