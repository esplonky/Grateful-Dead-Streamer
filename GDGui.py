import GratefulDead
import sys
from Tkinter import *




root = Tk()
root.config(height=500, width=300)
listBoxYears = Listbox(root)
listBoxYears.config(height=400, width=150)
listBoxShows = Listbox(root)
listBoxShows.config(height=400, width=150)
showYearStg = [1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972,
               1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
               1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988,
               1989, 1990, 1991, 1992, 1993, 1994, 1995]

showMetaStgList = []
showMetaStg = GratefulDead.getShowMetaTitle()
for i in showMetaStg:
    showMetaStgList.append[i]




showMetaStgList = []
for i in showYearStg:
    listBoxYears.insert(END, i)


selectedYear = map(int, listBoxYears.curselection())

listBoxYears.pack()




for show in showMetaStgList:
    listBoxShows.insert(END, show)






#listBoxYears.grid(row=0, column=0)

root.mainloop()

