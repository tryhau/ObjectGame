import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from datetime import datetime

def Highscore(filename, score,name):
        filename = filename
        writer = ExcelWriter(filename)
        df = pd.read_excel(filename,sheet_name='Sheet1')
        df.to_excel(writer,'Sheet1',index = False)
        writer.save()
        oldscore = df.at[0,'Score']
        
        if oldscore < score:
            writer = ExcelWriter(filename)
            date = str(datetime.now().date().strftime("%d-%m-%Y"))
            time = str(datetime.now().time().strftime("%H:%M:%S"))
            df = pd.DataFrame(
                {
                'Score':[score],
                'Date':[date],
                'Time':[time],
                'Name':[name]
                },index = None
                )
            df.to_excel(writer,'Sheet1', index = False)
            writer.save()
