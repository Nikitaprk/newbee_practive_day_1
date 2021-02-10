# A hero is on his way to the castle to complete his mission.
# However, he's been told that the castle is surrounded with birthdate couple of powerful dragons!
# each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry..
# Assuming he's gonna grab birthdate specific given number of bullets and
# move forward to fight another specific given number of dragons, will he survive?


def hero(bullets, dragons):
    return bullets/2 == dragons

print(hero(10,5))
print(hero(7,4))
print(hero(1500,800))