import GratefulDead
import sys
import os
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


gratefulDeadTitleCache = GratefulDead.loadXMLTitlesFromGDFile('title')
gratefulDeadYearCache = GratefulDead.loadXMLTitlesFromGDFile('year')
gratefulDeadIDCache = GratefulDead.loadXMLTitlesFromGDFile('identifier')
gratefulDeadCache = GratefulDead.loadXMLTitlesFromGDFile('')




showStg = {0:{}}
x = 0
for i in gratefulDeadTitleCache:
        listBoxShows.insert(END, i)

        for m in gratefulDeadIDCache:
            showStg[x] = i + ',' + m


listBoxShows.pack()

listBoxShows.grid(row=0, column=0)



root.mainloop()

