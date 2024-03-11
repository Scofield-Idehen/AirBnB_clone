#!/usr/bin/python3
"""AirBnB Console - project entry point """

import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Class definition for HBNBCommand """

    prompt = '(hbnb) '
    class_list = {'BaseModel': BaseModel, 'User': User,
                  'City': City, 'Place':
                      Place, 'Amenity': Amenity,
                      'Review': Review, 'State': State}

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Signal to exit the program """
        print('')
        return True

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_create(self, arg):
        """ Create a new class instance and print its id """
        if not arg:
            print('** class name missing **')
            return

        class_name = arg.strip()
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        new_instance = self.class_list[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """  Prints the str rep of an inst based on class name and id"""

        args_list = arg.split()
        if not args_list:
            print('** class name missing **')
            return
        class_name = args_list[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print('** instance id missing **')
            return
        instance_id = args_list[1]
        key = f'{class_name}.{instance_id}'
        if key in storage.all():
            instance = storage.all()[key]
            print(instance)
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        """ Method to del instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return

        arg_list = arg.split()

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        class_name = arg_list[0]
        instance_id = arg_list[1]

        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances"""
        if not arg:
            print([str(instance) for instance in storage.all().values()])
        elif arg not in self.class_list:
            print("** class doesn't exist **")
        else:
            print([str(instance) for key, instance
                   in storage.all().items() if arg in key])

    def do_update(self, argument):
        """Update an instance based on the class name and id """
        token_list = shlex.split(argument)
        if len(token_list) == 0:
            print("** class name missing **")
            return
        elif len(token_list) == 1:
            print("** instance id missing **")
            return
        elif len(token_list) == 2:
            print("** attribute name missing **")
            return
        elif len(token_list) == 3:
            print("** value missing **")
            return
        elif token_list[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        keyI = token_list[0] + "." + token_list[1]
        dicI = storage.all()
        try:
            instanceU = dicI[keyI]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(instanceU, token_list[2]))
            token_list[3] = typeA(token_list[3])
        except AttributeError:
            pass
        setattr(instanceU, token_list[2], token_list[3])
        storage.save()

    def precmd(self, argument):
        """execute just before the command line is interpreted"""
        try:
            args = argument.split('.', 1)
            if len(args) != 2:
                return argument

            class_name = args[0]
            args = args[1].split('(', 1)
            if len(args) != 2:
                return argument

            class_name_strip = args[0]
            args = args[1].split(')', 1)
            if len(args) != 2:
                return argument

            _id = args[0].replace(",", "").strip()
            other_arguments = args[1].replace(",", "").strip()

            line = "{} {} {} {}".format(class_name_strip,
                                        class_name, _id, other_arguments)
            print(line)
            return line
        except Exception as e:
            print("Error parsing command: {}".format(str(e)))
            return argument

    def do_count(self, argument):
        """  Retrives the number of instances of a class """
        token_list = shlex.split(argument)
        dict = storage.all()
        num_instances = 0
        if token_list[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        else:
            for key in dict:
                class_name = key.split('.')
                if class_name[0] == token_list[0]:
                    num_instances += 1

            print(num_instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
