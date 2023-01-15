# import turtle

# timmy = turtle.Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("brown")
# timmy.forward(100)


# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon", "Type"]
table.align = "l"
table.add_rows(
    [
        ["Pikachu", "electric"],
        ["Squirtle", "Water"],
        ["Charmander", "fire"],
    ]
)

print(table)