# -*- coding: utf-8 -*-

import glassdoor_scraper as gs
import pandas as pd

path = "/Users/apple/Documents/SE_salary_proj/chromedriver"

df = gs.get_jobs('software engineer',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
