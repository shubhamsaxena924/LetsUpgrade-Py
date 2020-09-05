# You all are Pilots, you want to land a plane safely,
# so altitude required for landing a plane is 1000ft,
# it it is less than tell pilot to land the plane,
# or it is more than that but less than 5000ft ask the pilot to “come down to 1000ft”,
# else if it more than 5000ft ask the pilot to “go around and try later”
altitude = int(input('Enter the current altitude in feets: '))
if(altitude <= 1000):
    print('Safe to land')
elif(altitude > 1000 and altitude <= 5000):
    print('Bring down to 1000')
elif(altitude > 5000):
    print('Turn Around')
else:
    print('Not a valid altitude')
