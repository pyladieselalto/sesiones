#!/usr/bin/env python

from deep_translator import GoogleTranslator
from exceptions import LanguageNotSupportedException

def test_response():
    x="en"
    y="es"
    if x=="" and y=="":
        raise LanguageNotSupportedException("Empty languages")
    if x=="auto" and y=="none":
        raise LanguageNotSupportedException("Not valid Languages")
    if (x is None) or (y is None):
        raise LanguageNotSupportedException("Not Type")
    assert GoogleTranslator(source=x, target=y)