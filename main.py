import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
load_dotenv()

api_key = os.environ['api_key']
print(api_key)

from test import Combining_All_Function
res = Combining_All_Function()
res.check_package_version1("3.1")

## inheritance, abstraction, encapsulatiion, poymorphism