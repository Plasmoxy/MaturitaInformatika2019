from turtle import Turtle, Screen



# mocniny 2 splnaju podmienku: delielne vsetkymi predchadzajucimi




    

def kresli_vezu():
    W = 500
    H = 500
    d = 5
    
    win = Screen()
    win.screensize(W, H)
    t = Turtle()
    t.speed(1000)
    
    def obdlz(t, w, h):
        t.pendown()
        t.forward(d*w/2)
        t.left(90)
        t.forward(d*h)
        t.left(90)
        t.forward(d*w)
        t.left(90)
        t.forward(d*h)
        t.left(90)
        t.forward(d*w/2)
        t.left(90)
        t.penup()
        t.forward(d*h)
        t.right(90)
    
    s = 32 # mocniny dvojky!
    w = 1
    
    while s > 0:
        s = s / 2
        w = w * 2
        obdlz(t, s, w)
    
    win.mainloop()

# delba = [1]

# for i in range (2,1000000):
#     DELITe = True
#     for o in delba:
#         if i%o != 0:
#             DELITe =False
#         else:
#             continue
#     if DELITe == True:
#         delba.append(i)


# print( delba)

kresli_vezu()