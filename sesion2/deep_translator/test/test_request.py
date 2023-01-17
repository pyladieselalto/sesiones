#!/usr/bin/env python

"""Tests for `deep_translator` package."""

import pytest

from deep_translator import GoogleTranslator

def test_content():
    GoogleTranslator(source="nada", target="es")