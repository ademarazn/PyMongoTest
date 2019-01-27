#!/usr/bin/env python
# -*- coding: utf-8 -*-


def has_attr(obj, name):
        try:
            return obj.__getattr__(name) is not None
        except:
            return False

def is_empty(value):
    return value in (None, '')
