'''
Created on 06.11.2024

@author: sholzhauer
'''
from glob import glob
import logging
import os

import pytest

from pyan.analyzer import CallGraphVisitor
from pyan.visgraph import VisualGraph

if __name__ == '__main__':
    
    graph_options = {
        "draw_defines": False,
        "draw_uses": True,
        "colored": True,
        "grouped_alt": False,
        "grouped": True,
        "nested_groups": True,
        "annotated": False,
    }
        
    filenames = glob(os.path.join(os.path.dirname(__file__), "../../building-stock-model/building_stock_model/energy/building_final_energy_demand.py"), recursive=True)
    v = CallGraphVisitor(filenames)
    graph = VisualGraph.from_visitor(v, options = graph_options, logger=logging.getLogger())