import simple_draw as sd
import random

sd.resolution = (1200, 800)

x_coordinates = []
y_coordinates = []
sizes_rays = []
old_snowflakes = []


def create_snowflakes():
    global x_coordinates
    global y_coordinates
    global sizes_rays
    x_coordinates = [coord_x for coord_x in range(100, 1100, 50)]
    y_coordinates = [coord_y for coord_y in range(800, 1900, 55)]
    sizes_rays = [rays_snowflakes for rays_snowflakes in range(10, 50, 2)]
    random.shuffle(x_coordinates)
    random.shuffle(y_coordinates)
    random.shuffle(sizes_rays)


def create_snowflake():
    x_coordinates.append(x_coordinates[random.randint(0, len(x_coordinates) - 1)])
    y_coordinates.append(random.randint(800, 1900))
    sizes_rays.append(sizes_rays[random.randint(0, len(sizes_rays) - 1)])


def snow_draw(color, number_snowflakes=-1):
    if number_snowflakes == -1:
        for i in range(0, len(x_coordinates)):
            point = sd.get_point(x_coordinates[i], y_coordinates[i])
            sd.snowflake(center=point, length=sizes_rays[i], factor_a=0.5, color=color)
    else:
        point = sd.get_point(x_coordinates[number_snowflakes], y_coordinates[number_snowflakes])
        sd.snowflake(center=point, length=sizes_rays[number_snowflakes], factor_a=0.5, color=color)


def move_snowflakes():
    for i in range(0, len(x_coordinates)):
        if y_coordinates[i] > sizes_rays[i]:
            y_coordinates[i] -= 25
            delta = random.randint(-5, 5)
            x_coordinates[i] += delta


def numbers_reaching_bottom_screen():
    snowflakes = []
    for i in range(0, len(x_coordinates)):
        if y_coordinates[i] <= sizes_rays[i]:
            snowflakes.append(i)

    return snowflakes


def add_new_snowflake(reached_bottom=numbers_reaching_bottom_screen):
    for i in range(0, len(reached_bottom)):
        if i in reached_bottom:
            create_snowflake()


def remove_snowflakes(reached_bottom=numbers_reaching_bottom_screen):
    for i in range(len(reached_bottom) - 1, -1, -1):
        if i in reached_bottom:
            snow_draw(sd.background_color, i)
            del x_coordinates[i]
            del y_coordinates[i]
            del sizes_rays[i]

