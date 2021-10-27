import re
import os
import shutil

def padding(a,b):
  j=b-len(a)
  i=0
  for i in range(j):
   a='0'+a 
  return a
# try:
#     os.mkdir(r'./correct_srt')
# except FileExistsError:
#     shutil.rmtree('./correct_srt')
#     os.mkdir(r'./correct_srt')
#     pass

def breakingbad(season,episode):
  path=r'./corrected_srt/Breaking Bad'
  source=r'./wrong_srt/Breaking Bad'
  try:
     shutil.rmtree(path)
     shutil.copytree(source,path)
  except:
      shutil.copytree(source,path)
  for file in os.listdir(path):
      oldfile=re.compile(r'\d+')
      x=oldfile.findall(file)
      #print(x)
      y=re.compile(r'.mp4$')
      z=re.compile(r'.srt$')
      if y.search(file):
          dest='Breaking Bad - Season '+ padding(x[0],season) +' Episode ' +padding(x[1],episode)+ '.mp4' 
          os.rename('./corrected_srt/Breaking Bad/'+file,'./corrected_srt/Breaking Bad/'+dest)
      if z.search(file):
          dest='Breaking Bad - Season '+ padding(x[0],season) +' Episode ' +padding(x[1],episode)+'.srt'  
          os.rename('./corrected_srt/Breaking Bad/'+file,'./corrected_srt/Breaking Bad/'+dest)

def gameofthrones(season,episode):
  path=r'./corrected_srt/Game of Thrones'
  source=r'./wrong_srt/Game of Thrones'
  try:
     shutil.rmtree(path)
     shutil.copytree(source,path)
  except:
      shutil.copytree(source,path)
  for file in os.listdir(path):
      oldfile=re.compile(r'\d+')
      r=re.compile(r'[A-Za-z ]*\.|mp4|srt')
      x=oldfile.findall(file)
      p=r.findall(file)
      #print(p)
      y=re.compile(r'.mp4$')
      z=re.compile(r'.srt$')
      if y.search(file):
          dest='Game of Thrones - Season '+ padding(x[0],season) +' Episode ' +padding(x[1],episode)+ ' -'+p[0]+p[-1] 
          os.rename('./corrected_srt/Game of Thrones/'+file,'./corrected_srt/Game of Thrones/'+dest)
      if z.search(file):
          dest='Game of Thrones - Season '+ padding(x[0],season) +' Episode ' +padding(x[1],episode)+ ' -'+p[0]+p[-1]  
          os.rename('./corrected_srt/Game of Thrones/'+file,'./corrected_srt/Game of Thrones/'+dest)

def lucifer(season,episode):
  path=r'./corrected_srt/Lucifer'
  source=r'./wrong_srt/Lucifer'
  try:
     shutil.rmtree(path)
     shutil.copytree(source,path)
  except:
      shutil.copytree(source,path)
  for file in os.listdir(path):
      oldfile=re.compile(r'\d+')
      r=re.compile(r'[A-Za-z \']*\.|mp4|srt')
      x=oldfile.findall(file)
      p=r.findall(file)
      #print(p)
      y=re.compile(r'.mp4$')
      z=re.compile(r'.srt$')
      if y.search(file):
          dest='Lucifer - Season '+ padding(x[0],season) +' Episode ' +padding(x[1],episode)+ ' -'+p[0]+p[-1] 
          os.rename('./corrected_srt/Lucifer/'+file,'./corrected_srt/Lucifer/'+dest)
      if z.search(file):
          dest='Lucifer - Season '+ padding(x[0],season) +' Episode ' +padding(x[1],episode)+ ' -'+p[0]+p[-1]  
          os.rename('./corrected_srt/Lucifer/'+file,'./corrected_srt/Lucifer/'+dest)


def regex_renamer():

    # Taking input from the user

    # print("1. Breaking Bad")
    # print("2. Game of Thrones")
    # print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))
    if webseries_num==1:
        breakingbad(season_padding,episode_padding)
    elif webseries_num==2:
       gameofthrones(season_padding,episode_padding)
    else:
       lucifer(season_padding,episode_padding)

regex_renamer()
