def main():
    # call both functions
    blue ()
    blastoff()

    total_cost = candy_shop()
    print("Total candy cost: $", round(total_cost, 2))
    
    fruit_pricing()


def blue ():
    red = 3
    purple = red*12 # multiply red by 12
    print(purple)

def blastoff():
    # count down
    count = int(input("Give me a number: "))

    for i in range(count, 0, -1):
        print(i)


    print("blastoff!")

def candy_shop():
    candies = ["twix", "M&M", "snickers"] # Create Candy list 
    candies.append("kitkat") # Change candy list
    candies.insert(1,"skittles")
    candies.sort()
    candies.remove("kitkat")
    print(candies)


    user_candies = [] # Ask for candy

    for i in range(3):
        candy = input("Give me one of your favorite candies: ")
        user_candies.append(candy)

    all_candies = user_candies + candies # Combine lists
    print (len(all_candies))

    cost = 0

    for candy in all_candies:
        print (candy)
        cost += 1.25

    return cost


def fruit_pricing():
    fruits = { "apple": 0.75, "banana": 1.25, "orange": 0.80, "peach": 2.25, "coconut": 2.80}
    fruits["pear"] = 1.15 # Add pear
    print(fruits.get("peach"))


    for fruit, price in fruits.items(): # Print fruits that costs a minimun $1.25
        if price >= 1.25:
            print(fruit)
    
    # calculate total fruit cost
    total = (3* fruits["apple"] + 2* fruits["banana"] + 0* fruits["orange"] + 0 * fruits["peach"] + 1 * fruits["coconut"])
    print("Total fruit cost: $", round(total,2))


main() # Run it
    











