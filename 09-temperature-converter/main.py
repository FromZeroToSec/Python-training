def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    kelvin = (fahrenheit - 32) / 1.8 + 273.15
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    fahrenheit = (kelvin - 273.15) * 1.8 + 32
    return fahrenheit

# main menu