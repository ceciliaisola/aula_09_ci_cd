import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum ():
    #given two values 
    value1 = 2
    value2 = 5
    #when we calculate the sum
    output = methods.sum(value1,value2)
    #then the sum should be 7
    assert output == 7

def test_subtraction():
    #given two values
    value1 = 10
    value2 = 5
    #when we subtract
    output = methods.sub(value1,value2)
    #then the subtract should be
    assert output == 5

def test_mult():
    #given two values
    value1 = 10
    value2 = 5
    #when we multiply
    output = methods.mult(value1,value2)
    #then the multiply should be
    assert output == 50

def test_div():
    #given two values
    value1 = 10
    value2 = 5
    #when we divide
    output = methods.div(value1,value2)
    #then the division should be
    assert output == 2