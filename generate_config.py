#! /usr/bin/python

import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import time
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--datayml", required=True, help="Data yaml file containing config key value pairs")
ap.add_argument("-t", "--template", required=True, help="File containing config templates in Jinja")
ap.add_argument("-p", "--template_path", required=False, help="Path containing the template file")
args = vars(ap.parse_args())


def config_renderer(datayml, template_file, template_location="~/"):
  #print "Arguments got are {0} and {1}".format(datayml, template_file)
  device_data=yaml.full_load(open(datayml))
  #print device_data
  env = Environment(loader = FileSystemLoader(template_location), trim_blocks=True, lstrip_blocks=True)
  template = env.get_template(template_file)
  filename = device_data.get('name', None)
  if filename is not None :
    filename = filename + "_" + str("config")
    with open(filename, "a") as fd:
      fd.write(template.render(device_data))
  else:
    print ("Filename is None")

config_renderer(args['datayml'], args['template'], args['template_path'])
