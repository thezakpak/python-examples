#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PopoverWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Popover Demo")
        self.set_border_width(10)

        outerbox = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        self.add(outerbox)

        button = Gtk.Button.new_with_label("Click Me")
        button.connect("clicked", self.on_click_me_clicked)
        outerbox.pack_start(button, False, True, 0)

        self.popover = Gtk.Popover()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        vbox.pack_start(Gtk.ModelButton("Item 1"), False, True, 10)
        vbox.pack_start(Gtk.Label("Item 2"), False, True, 10)
        self.popover.add(vbox)
        self.popover.set_position(Gtk.PositionType.BOTTOM)

    def on_click_me_clicked(self, button):
        self.popover.set_relative_to(button)
        self.popover.show_all()
        self.popover.popup()

    def on_open_clicked(self, button):
        print("\"Open\" button was clicked")


win = PopoverWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
