hour = int(input("Enter your this week hours "))
if hour <= 0 or hour > 168:
    print("INVALID")
elif hour <= 40 and hour >= 0:
    print("YOU MADE", hour * 8, "DOLLARS THIS WEEK")
elif hour >= 41 and hour <= 50:
    overpay1 = hour % 40
    basic = hour - overpay1
    print("YOU MADE", (basic * 8) + (overpay1 * 9), "DOLLARS THIS WEEK")
elif hour > 50:
    basic = hour % 40
    net = hour - basic
    overpay2 = hour % 50
    overpay1 = basic - overpay2
    print("YOU MADE", (net * 8) + (overpay2 * 10) + (overpay1 * 9),
          "DOLLARS THIS WEEK")