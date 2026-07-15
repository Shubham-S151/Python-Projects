# Project: Optics Calculator
# This app is going to be helper in the calculation of different optical measure by 
# implementation of following:
# 1. Lens Formula
# 2. Magnification
# 3. Snell's Law
# For this app we are going to need "math" library.

import math

# Lens Formula = 1/f = 1/v - 1/u
def lens_formula() -> float:
    """This function is going to handle all the consol as well as calculation part for lens formula"""
    print("\n--- Lens Formula ---")
    print("1. Calculate Focal Length (f)")
    print("2. Calculate Object Distance (u)")
    print("3. Calculate Image Distance (v)")

    lens_choice = int(input("Enter your choice: "))

    if lens_choice == 1 :
        u = float(input("Enter object distance (u in cm, use negative for virtual objects): "))
        v = float(input("Enter image distance (v in cm, use negative for virtual objects): "))
        f = 1/((1/v) - (1/u))
        print("Focal Length (f) =",f,"cm")
    elif lens_choice == 2 :
        v = float(input("Enter image distance (v in cm, use negative for virtual objects): "))
        f = float(input("Enter focal length (f in cm, use negative for concave lens): "))
        u = 1/((1/v) - (1/f))
        print("Object Distance (u) =", u, "cm")
    elif lens_choice == 3 :
        u = float(input("Enter object distance (u in cm, use negative for virtual objects): "))
        f = float(input("Enter focal length (f in cm, use negative for concave lens): "))
        v = 1/((1/f) - (1/u))
        print("Image Distance (v) =", v, "cm")
    else :
        print("Invalid Choice! Retry")

# Magnification M = v/u
def magnification() -> float:
    """This function is going to ask user for u and v then calculates magnification (m)."""
    print("\n--- Magnification ---")
    u = float(input("Enter object distance (u in cm, use negative for virtual objects): "))
    v = float(input("Enter image distance (v in cm, use negative for virtual objects): "))
    m = v/u
    print("Linear Magnification (m) =",m)

# Refractive Index: n = sin(i) / sin(r)
def refractive_index() -> float:
    """This function is going to ask user for i and r then calculates refractive index (n)."""
    print("\n--- Refractive Index (Snell's Law) ---")
    
    angle_incidence = float(input("Enter angle of incidence (degrees): "))
    angle_refraction = float(input("Enter angle of refraction (degrees): "))

    rad_incidence = math.radians(angle_incidence)
    rad_refraction = math.radians(angle_refraction)

    n = math.sin(rad_incidence) / math.sin(rad_refraction)
    print("Refractive Index (n) =", n)

while True:
    print("\n=== Optics Calculator ===")
    print("1. Lens Formula (f, u, v)")
    print("2. Magnification (linear)")
    print("3. Refractive Index (Snell's Law)")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        lens_formula()
    elif choice == 2:
        magnification()
    elif choice == 3:
        refractive_index()
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid Choice! Retry.")