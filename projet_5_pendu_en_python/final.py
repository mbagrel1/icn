#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import gtk

fenetre.connect("key-press-event", key_pressed)

def key_pressed(widget, event):
    keyval = event.keyval
    keyval_name = gtk.gdk.keyval_name(keyval)
    state = event.state
    if keyval_name == "Return":
        perform_action()
