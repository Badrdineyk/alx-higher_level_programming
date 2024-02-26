#!/usr/bin/python3
"""Defines a Base class"""
import json
import csv
import turtle


class Base:
    """Represents base of all other classes in this project

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises a new Base

        Args:
            id (int): The identity of The base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): is a list of instances who inherits of Base
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dics = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dics))

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation json_string

        Args:
            json_string (str): string representing a list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
            dictionary (dict): A dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_obj = cls(1, 1)
            else:
                dummy_obj = cls(1)
            dummy_obj.update(**dictionary)
            return dummy_obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**dct) for dct in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    args_names = ["id", "width", "height", "x", "y"]
                else:
                    args_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=args_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file."""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    args_names = ["id", "width", "height", "x", "y"]
                else:
                    args_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, fieldnames=args_names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
