import GratefulDead
import sys
from Tkinter import *




root = Tk()
root.config(height=500, width=300)
listBox = Listbox(root)
listBox.config(height=400, width=150)

showYearStg = [1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972,
               1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
               1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988
               1989, 1990, 1991, 1992, 1993, 1994, 1995]

for i in showYearStg:
    listBox.insert(END, i)

selectedYear = map(int, listBox.curselection())




listBox.pack()


showMetaStg = GratefulDead.getShowMeta()



#listBox.grid(row=0, column=0)

root.mainloop()

