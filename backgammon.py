from cs1graphics import*

#Declares the variable size which I used to scale the rest of my dimensions
size=int(input('Enter pixels per grid cell:'))

paper=Canvas(15*size,13*size,'burlywood4','Backgammon')
halves=2

#the line in the middle of the board
divider=Path(Point(7.5*size,0),Point(7.5*size,13*size))
divider.setBorderWidth(3)
paper.add(divider)

#Splits the board into two halves for the inner design
for rect in range(halves):
    boardinterior=Rectangle(6*size,11*size,Point(4*size+(rect*7*size),6.5*size))
    boardinterior.setFillColor('navajowhite')
    paper.add(boardinterior)

#Introduces the triangles(points) and the corresponding numbers   
for number in range(0,24):
    num=str(number+1) #The texts for the points
    if number <= 5:
        text=Text(num,0.32*size,Point(size*(1.5+number),12.5*size))
        Tri=Polygon(Point((number+1)*size,12*size),Point(size*(1.5+number),7*size),Point(size*(2+number),12*size))
    elif 5 < number <= 11:
        text=Text(num,0.32*size,Point(size*(2.5+number),12.5*size))
        Tri=Polygon(Point((2+number)*size,12*size),Point((2.5+number)*size,7*size),Point((3+number)*size,12*size))
    elif 11 < number <= 17:
        text=Text(num,0.32*size,Point(size*(25.5-number),0.5*size))
        Tri=Polygon(Point((26-number)*size,size),Point((25.5-number)*size,6*size),Point((25-number)*size,size))
    else:
        text=Text(num,0.32*size,Point(size*(24.5-number),0.5*size))
        Tri=Polygon(Point((25-number)*size,size),Point((24.5-number)*size,6*size),Point((24-number)*size,size))
    #sets the differences in color based on if the number is even or odd
    if int(num)%2!=0:
        Tri.setFillColor('darkorange3')
    else:
        Tri.setFillColor('tan')
       
    paper.add(text)
    paper.add(Tri)

#Introduces the white and black checkers unto the board
circ=Circle(0.45*size)
for checkers,point,white,bottom in[(2,1,False,True),(5,6,True,True),(3,8+1,True,True),(5,12+1,False,True),(5,13,True,False),(3,17,False,False),(5,19+1,False,False),(2,24+1,True,False)]:
    for i in range(checkers):
        circ.setFillColor('black')
        if white:
            circ.setFillColor('white')
        if bottom:
            circ2=circ.clone()
            circ2.move((point+0.5)*size,size*(11.5-(i*0.9)))
            paper.add(circ2)
        if not bottom:
            circ2=circ.clone()
            circ2.move(((26-point)+0.5)*size,size*(1.5+(i*0.9)))
            paper.add(circ2)

