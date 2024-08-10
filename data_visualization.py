import matplotlib.pyplot as plt
import numpy as np
#should be run in software where matplotlib is supported

def line_plot():
    x = np.array([])
    y = np.array([])
    n = int(input("Enter the number of coordinates for each axis: "))

    print("Enter the coordinates of x:")
    for i in range(n):
        ele1 = int(input())
        x = np.append(x, ele1)  # Append to x

    print("Enter the coordinates of y:")
    for i in range(n):
        ele2 = int(input())
        y = np.append(y, ele2)  # Append to y

    x_label = str(input("enter the label for x axis"))
    y_label = str(input("enter the label for y axis"))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    Title = str(input("enter the title of the graph"))
    plt.title(Title)
    m_color=[]
    m=str(input("enter marker color : "))
    m_color.append(m)

    plt.plot(x, y, marker='o', ms=8, mec=m)
    plt.grid()
    plt.show()


def scatter_plot():
    x = np.array([])
    y = np.array([])
    n = int(input("Enter the number of coordinates for each axis: "))

    print("Enter the coordinates of x:")
    for i in range(n):
        ele1 = int(input())
        x = np.append(x, ele1)  # Append to x

    print("Enter the coordinates of y:")
    for i in range(n):
        ele2 = int(input())
        y = np.append(y, ele2)  # Append to y

    x_label = str(input("enter the label for x axis: "))
    y_label = str(input("enter the label for y axis: "))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    Title = str(input("enter the title of the graph: "))
    plt.title(Title)
    mul_colors = str(input("do you want multiple colors (y/n): "))
    if mul_colors == "y":
        colors = []
        print("enter the different colors for the scatter points: ")
        for i in range(n):
            c2 = str(input())
            colors.append(c2)
    else:
        colors = []
        print("enter the colors for the scatter points: ")
        for i in range(n):
            c1 = str(input())
            colors.append(c1)
    plt.scatter(x, y,c=colors)
    plt.grid()
    plt.show()
def bar_plot():
    x = np.array([])
    y = np.array([])
    n = int(input("Enter the number of coordinates for each axis: "))

    print("Enter the value for the bars :")
    for i in range(n):
        ele1 = str(input())
        x = np.append(x, ele1)  # Append to x

    print("Enter the data :")
    for i in range(n):
        ele2 = int(input())
        y = np.append(y, ele2)  # Append to y

    x_label = str(input("enter the label for x axis: "))
    y_label = str(input("enter the label for y axis: "))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    Title = str(input("enter the title of the graph: "))
    plt.title(Title)
    mul_colors=str(input("do you want multiple colors colors(y/n): "))
    if mul_colors=="y":
        colors = []
        print("enter the different colors:  ")
        for i in range(n):
            c2 = str(input())
            colors.append(c2)
    else:
        colors = []
        print("enter the color: ")
        for i in range(n):
            c1= str(input())
            colors.append(c1)
    h_or_v=str(input("do you want a vertical plot or horizontal plot (h/v) : "))
    if (h_or_v=="h"):
        plt.barh(x, y, color=colors)
        plt.grid()
        plt.show()
    else:
        plt.bar(x, y, color=colors)
        plt.grid()
        plt.show()


def pie_chart():

    x = []
    n = int(input("Enter the number of segments: "))

    print("Enter the data:")
    for i in range(n):
        ele = int(input())
        x.append(ele)

    mylabels = []
    print("Enter the labels:")
    for i in range(n):
        l = str(input())
        mylabels.append(l)

    mycolors = []
    print("Enter the colors (in hex or color names):")
    for i in range(n):
        c = str(input())
        mycolors.append(c)

    plt.pie(x, labels=mylabels, colors=mycolors, shadow=True)
    plt.legend()
    Title = str(input("enter the title of the graph: "))
    plt.axis('equal')
    plt.show()


print("--------WELCOME TO DATA VISUALIZATION----------")
while(True):
    print("    1.LINE PLOT    2.SCATTER PLPOT    3.BAR PLOT    4.PIE PLOT    ")
    ch = int(input("SELECT THE TYPE OF PLOTTING FOR DATA VISUALIZATION : "))
    if ch == 1:
        line_plot()
    elif ch == 2:
        scatter_plot()
    elif ch == 3:
        bar_plot()
    elif ch == 4:
        pie_chart()
    else:
        print("wrong input")
    c=str(input("do you wantto continue (y/n) :"))
    if (c=="n"):
        break




