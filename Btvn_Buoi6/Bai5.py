def format_phone_number(number_phone):
    s = ""
    for i in number_phone: 
        if i.isdigit() == True:
            s = s + i
    if s[0] != "0" or len(s) != 10 :
        return "Invalid phone number"
    return s
l = [". ? 0123456789"," 02319231", ". ? 0923123145", "8421301203", "absc0123145452ds"]
for i in l:
    chuanhoa = format_phone_number(i)
    print(f"Sđt:{i} --> Chuan hoa:{chuanhoa}")