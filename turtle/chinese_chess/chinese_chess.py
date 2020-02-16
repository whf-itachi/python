import turtle

pen = turtle.Pen()
turtle.bgcolor("#F4C79E")  # 设置窗口颜色
turtle.setup(714, 800)  # 设置窗口大小
turtle.title("中国象棋")  # 标题
pen.hideturtle()  # 隐藏海龟图案
turtle.tracer(False)  # 关闭动画，让海龟以比较高的速度渲染

array = [
    {
        "text": "车",
        "role": "A",
        "pix": (-300, 369)
    },
    {
        "text": "马",
        "role": "A",
        "pix": (-247.0, 369.0)
    },
    {
        "text": "象",
        "role": "A",
        "pix": (-166.0, 369.0)
    },
    {
        "text": "车",
        "role": "A",
        "pix": (-300, 369)
    },
    {
        "text": "士",
        "role": "A",
        "pix": (-86.0, 369.0)
    },
    {
        "text": "将",
        "role": "A",
        "pix": (-5.0, 369.0)
    },
    {
        "text": "士",
        "role": "A",
        "pix": (79.0, 369.0)
    },
    {
        "text": "象",
        "role": "A",
        "pix": (159, 369.0)
    },
    {
        "text": "马",
        "role": "A",
        "pix": (239.0, 369.0)
    },
    {
        "text": "卒",
        "role": "A",
        "pix": (-329.0, 126.0)
    },
    {
        "text": "卒",
        "role": "A",
        "pix": (-167.0, 128.0)
    },
    {
        "text": "卒",
        "role": "A",
        "pix": (-6.0, 125.0)
    },
    {
        "text": "卒",
        "role": "A",
        "pix": (156.0, 126.0)
    },
    {
        "text": "卒",
        "role": "A",
        "pix": (329.0, 369.0)
    },
    {
        "text": "炮",
        "role": "A",
        "pix": (-248.0, 209.0)
    },
    {
        "text": "炮",
        "role": "A",
        "pix": (239.0, 208.0)
    },
    # 下方为B方阵容
    {
        "text": "车",
        "role": "A",
        "pix": (-300, -369)
    },
    {
        "text": "马",
        "role": "B",
        "pix": (-247.0, -369.0)
    },
    {
        "text": "象",
        "role": "B",
        "pix": (-166.0, -369.0)
    },
    {
        "text": "车",
        "role": "B",
        "pix": (-300, -369.0)
    },
    {
        "text": "士",
        "role": "B",
        "pix": (-86.0, -369.0)
    },
    {
        "text": "将",
        "role": "B",
        "pix": (-5.0, -369.0)
    },
    {
        "text": "士",
        "role": "B",
        "pix": (79.0, -369.0)
    },
    {
        "text": "象",
        "role": "B",
        "pix": (159, -369.0)
    },
    {
        "text": "马",
        "role": "B",
        "pix": (239.0, -369.0)
    },
    {
        "text": "卒",
        "role": "B",
        "pix": (-329.0, -126.0)
    },
    {
        "text": "卒",
        "role": "B",
        "pix": (-167.0, -128.0)
    },
    {
        "text": "卒",
        "role": "B",
        "pix": (-6.0, -125.0)
    },
    {
        "text": "卒",
        "role": "B",
        "pix": (156.0, -126.0)
    },
    {
        "text": "卒",
        "role": "B",
        "pix": (329.0, -126.0)
    },
{
        "text": "炮",
        "role": "B",
        "pix": (-248.0, -209.0)
    },
    {
        "text": "炮",
        "role": "B",
        "pix": (239.0, -208.0)
    },
]


def chess(text, pix, bgcolor, textcolor):
    """
    落子
    :param text: 棋子名称
    :param pix:  棋子坐标
    :param bgcolor:  棋子背景
    :param textcolor:  棋子文字显示的颜色
    :return:
    """
    pen.penup()
    pen.setposition(pix)
    pen.pendown()
    pen.color("#6E3F25")
    pen.dot(70)
    pen.color(bgcolor)
    pen.dot(55)
    pen.color("white")
    pen.penup()
    pen.setheading(270)
    pen.color(textcolor)
    pen.write(text, align="center", font=("Baoli TC", 40, "bold"))

def draw():
    """
    绘制棋盘
    :return:
    """
    # 绘制网格边框
    pen.penup()
    pen.setposition(-360, 402)
    pen.pendown()
    pen.color("#6E3F25")
    pen.width(30)
    for x in range(1, 5):
        if x % 2 != 0:
            pen.forward(710)
        else:
            pen.forward(795)
        pen.right(90)

    # 绘制网格
    pen.penup()
    pen.setposition(-330, 370)
    pen.width(2)
    pen.pendown()
    for x in range(9):
        pen.forward(650)
        pen.backward(650)
        pen.right(90)
        pen.forward(81)
        pen.left(90)
    pen.forward(650)

    pen.left(90)
    for x in range(8):
        pen.forward(730)
        pen.backward(730)
        pen.left(90)
        pen.forward(81)
        pen.right(90)

    pen.penup()
    pen.setposition(-280, 6)
    pen.pendown()
    pen.pencolor("#F4C79E")
    pen.right(90)
    pen.width(79)
    pen.forward(550)
    pen.width(1)

    pen.penup()
    pen.setposition(-230, -25)
    pen.color("#6E3F25")
    pen.write("楚河", align="center", font=("Baoli TC", 50, "bold"))

    pen.penup()
    pen.forward(450)
    pen.write("汉界", align="center", font=("Baoli TC", 50, "bold"))

    pen.penup()
    for x in [[-3.0, 290.0], [-4.0, -278.0]]:
        pen.up()
        pen.setposition(x)
        pen.down()
        pen.setheading(45)
        pen.pendown()
        pen.width(2)
        pen.color("#6E3F25")
        for x in range(4):
            pen.forward(114)
            pen.backward(114)
            pen.left(90)

    for x in array:
        if x["role"] == "A":
            chess(x["text"], x["pix"], "#A46A0C", "#2F1500")
        else:
            chess(x["text"], x["pix"], "#E69772", "#AB2A0E")

    turtle.update()

draw()

priChess = {}


def click(x, y):
    """
    鼠标点击事件
    :param x:
    :param y:
    :return:
    """
    global priChess
    if priChess == {}:
        for z in array:
            if abs(z["pix"][0] - x) <= 35 and abs(z["pix"][1] - y) <= 35:
                print("发现目标：", z)
                priChess = z
                pen.penup()
                pen.setposition(z["pix"])
                pen.color("white")
                pen.penup()
                pen.setheading(270)
                pen.forward(25)
                pen.write(z["text"], align="center", font=("Baoli TC", 40, "bold"))

                break
    else:
        print("落子")
        priChess["pix"] = (x, y)
        array.append(priChess)
        priChess = {}
        pen.reset()
        draw()

turtle.onscreenclick(click)

turtle.done()
