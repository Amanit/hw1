# -*- coding: utf-8 -*-
import types

import numpy as np
import pandas as pd
import pytest

from hw1.import_monster import methods_importer
from tests.test_modules import module_1


def test_methods_importer_imported_module_callable():
    assert isinstance(module_1, types.ModuleType)
    result = methods_importer(
        method_name='test_callable',
        modules=[module_1]
    )

    assert result == [module_1.test_callable]


def test_methods_importer_imported_module_not_callable():
    assert isinstance(module_1, types.ModuleType)
    result = methods_importer(
        method_name='SOME_CONSTANT',
        modules=[module_1]
    )

    assert result == []


def test_methods_importer_wrong_type():
    with pytest.raises(TypeError):
        methods_importer(
            method_name='test_callable',
            modules=[1]
        )


def test_methods_importer_string_module():
    result = methods_importer(
        method_name='array',
        modules=['numpy']
    )

    assert result == [np.array]


def test_methods_importer_multiple_modules():
    result = methods_importer(
        method_name='array',
        modules=['numpy', 'pandas']
    )

    assert result == [np.array, pd.array]


def test_methods_importer_different_modules_types():
    result = methods_importer(
        method_name='array',
        modules=['numpy', module_1]
    )

    assert result == [np.array, module_1.array]


def test_methods_importer_nonexistant_module():
    result = methods_importer(
        method_name='array',
        modules=[module_1, 'nonexistant']
    )

    assert result == [module_1.array]
