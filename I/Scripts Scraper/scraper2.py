##### Guardar información a CSV
#pip install xlsxwriter
#pip install xlrd
#pip install pandas
#pip install matplotlib

import pandas as pd
import os
import matplotlib.pyplot as plt
from facebook_scraper import get_posts

os.chdir(r"C:\Users\Nicolas\Desktop\Universidad\2021-2\Mineria de Datos\I\Scripts Scraper")
posts = []

# Se obtiene la información de las publicaciones
for post in get_posts('mercadolibrecol', pages=5):
    print(post)
    posts.append(post)

# Se pasa a formato base de datos
fb_posts = pd.DataFrame(posts)
plt.plot(fb_posts['time'], fb_posts['likes'])
fb_posts.to_excel('fb_emp.xlsx',index=False)

