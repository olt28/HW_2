import pytest

from bmi_cal import bmiCAT, bmi_calculation

def test_underweight():
    assert bmiCAT(13.3) == ("Category: Underweight")

def test_normal_weight():
    assert bmiCAT(18.9) == ("Category: Normal Weight")

def test_over__weight():
    assert bmiCAT(25.9) == ("Category: Overweight")

def test_obese():
    assert bmiCAT(39.2) == ("Category: Obese")

def test_boundaries():
    assert bmi_calculation()
    
    assert bmi_calculation(139.9, 74) == (18.4)
    assert bmiCAT(18.4) == ("Category: Underweight")
    
    assert bmi_calculation(77.7, 55) == (18.5)
    assert bmiCAT(18.5) == ("Category: Normal Weight")
    
    assert bmi_calculation(108.9, 56) == (25)
    assert bmiCAT(25) == ("Category: Overweight") 
    
    assert bmi_calculation(130.7, 56) == (30) 
    assert bmiCAT(30) == ("Category: Obese")

def test_shift_bounds():
    assert bmi_calculation(107.2, 64) == (18.4)
    assert bmiCAT(18.5) == ("Category: Normal Weight")


