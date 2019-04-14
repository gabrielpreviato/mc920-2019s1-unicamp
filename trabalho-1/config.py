#-*- coding: utf-8 -*-
import argparse

def str2bool(v):
  return v.lower() in ('true', '1')

arg_lists = []
parser = argparse.ArgumentParser()

def add_argument_group(name):
  arg = parser.add_argument_group(name)
  arg_lists.append(arg)
  return arg

# Network
net_arg = add_argument_group('Network')

# Data
data_arg = add_argument_group('Data')

# Save
save_arg = add_argument_group('Save')
save_arg.add_argument('--is_save', type=str2bool, default=False)

# Misc
misc_arg = add_argument_group('Misc')
misc_arg.add_argument('--path', type=str, default='.')

misc_arg.add_argument('--problems', type=float, default=[1.1, 1.2, 1.3, 1.4])
misc_arg.add_argument('--clean_at_init', type=str2bool, default=True)

misc_arg.add_argument('--gama', type=float, default=[0.25, 0.5, 2.0, 4.0], help='')
misc_arg.add_argument('--bits', type=int, default=[0, 1, 2, 3, 4, 5, 6, 7], help='')


def get_config():
  config, unparsed = parser.parse_known_args()
  return config, unparsed