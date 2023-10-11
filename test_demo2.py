from demo2 import Bulb_example

def test_bulb_status():
    bulb = Bulb_example()
    assert bulb.getStatus() == "Bulb is not glowing"
