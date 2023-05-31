
from hack_1 import fn_hack_1


# h-1
def test_hack_1():
    v = fn_hack_1()
    ck_1 = True if v != "" else False
    ck_2 =  v.isupper() == True
    ck_3 =  v == "FOOZIMAN"
    assert (ck_1,ck_2,ck_3) == (True,True,True)
