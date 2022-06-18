import logging
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET
import re

def process_posts(fd_in, fd_out_train, fd_out_test, target_tag, split):
