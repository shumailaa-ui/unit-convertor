import streamlit as st

st.title("🌐 Google-style Unit Converter")
st.write("This is a simple unit converter app made by **Shumaila Usmani** using Python and Streamlit.")

conversion_type = st.selectbox("Choose conversion type:", ["Length", "Temperature", "Weight"])

def convert_length(value, from_unit, to_unit):
    units = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def convert_weight(value, from_unit, to_unit):
    units = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    return value * units[from_unit] / units[to_unit]

value = st.number_input("Enter value to convert:", value=0.0, format="%.2f")

if conversion_type == "Length":
    from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"])
    to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"])
    result = convert_length(value, from_unit, to_unit)

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    result = convert_temperature(value, from_unit, to_unit)

elif conversion_type == "Weight":
    from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Pound", "Ounce"])
    to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Pound", "Ounce"])
    result = convert_weight(value, from_unit, to_unit)

st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
