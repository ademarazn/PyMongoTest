#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dao import persondao
from model import person
import view


class personcontroller():
    def __init__(self):
        self.persondao = persondao()

    def start(self):
        option = view.start()
        while option != '0':
            self.option(option)
            option = view.start()

    def option(self, option):
        view.start(False)
        if option is '1':
            # Insert person
            self.persondao.insert_one(view.get_person(self.persondao.last_id()+1))
        elif option is '2':
            # List registered people
            view.print_people(self.persondao.list_all())
        elif option is '3':
            # Find person by id
            view.print_person(self.persondao.find_by_id(view.get_id()))
        elif option is '4':
            # Find person by name
            view.print_people(self.persondao.find_by_name(view.get_name()), True)
        elif option is '5':
            # Delete person
            p = self.persondao.find_by_id(view.get_id())
            if view.confirm_delete():
                self.persondao.delete_one(p)
        elif option is '6':
            # Update person
            p = self.persondao.find_by_id(view.get_id())
            if view.print_person(p):
                p = view.get_person(p=p)
                self.persondao.update_one(p._id, p)
        elif option is '7':
            # Count registered people
            view.print_count(self.persondao.count_documents())
        elif option is '8':
            # Delete all
            if view.confirm_drop():
                self.persondao.drop()
        else:
            view.invalid_option()
        view.pause()


if __name__ == "__main__":
    main = personcontroller()
    try:
        main.start()
    except KeyboardInterrupt:
        print()
    view.exit()
