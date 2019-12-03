#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: November 2019
# This program calculates the area of a triangle when given height and radius


def mail(address_number, address_name, f_name, m_name, l_name, city, province,
         postal):
    if m_name == "":
        print("{} {}".format(f_name, l_name))
    else:
        print("{} {} {}".format(f_name, m_name, l_name))
    print("{} {}".format(address_number, address_name))
    print("{} {} {}".format(city, province, postal))


def main():
    add_input = input("enter street number: ")
    adn_input = input("enter street name: ")
    fir_input = input("enter first name: ")
    mid_input = input("enter middle name (leave blank if none): ")
    las_input = input("enter last name: ")
    cit_input = input("enter city: ")
    pro_input = input("enter province: ")
    pos_input = input("enter postal code: ")
    print("")
    mail(add_input, adn_input, fir_input, mid_input,
         las_input, cit_input, pro_input, pos_input)


if __name__ == "__main__":
    main()
