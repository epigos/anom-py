# flake8: noqa
from . import properties, properties as props
from .adapter import Adapter, get_adapter, set_adapter
from .model import Key, Model, Property, delete_multi, get_multi, put_multi, lookup_model_by_kind
from .query import Query, Resultset, Page, Pages

__version__ = "0.0.2"
