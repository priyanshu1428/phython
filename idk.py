a = int(input("PLZ SELECT A NUMBER BETWEEN 1-10"))
c = a + 5
d = c * 10
e = d - 15
f = e + 10
print("DO U WANT TO KNOW UR NO. IS GREATER THAN 100 ? (YES/NO)")
if f > 100:
    print("THE FINAL RESULT IS GREATER THAN 100")
else:
    print("THE FINAL RESULT IS LESS THAN OR EQUAL TO 100")

print("DO U WANT TO KNOW UR NO. ? (YES/NO)")
answer = input()
if answer == "YES":
    print("YOUR NUMBER IS:", a)
else:   print("THANK YOU FOR USING THIS PROGRAM")
print("DO U WANT TO KNOW SOMETHING MORE LIKE UR NO. ? (YES/NO)")
answer2 = input()
if answer2 == "YES":
    print("YOUR NUMBER  IS: ", a )
else:   print("THANK YOU FOR USING THIS PROGRAM")
