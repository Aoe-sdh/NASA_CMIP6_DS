import os
import pandas as pd

def sub2db(subfile):
    if os.path.exists(subfile):
        names = ["NIGSUB", "SUB", "GIS", "MON", "AREA", "PRECIP", "SNOMELT","PET", "ET", "SW", "PREC", "SURQ", "GW_Q", "WYLD", "SYLD", "ORGN"
                   , "ORGP", "NSURQ", "SOLP", "SEDP", "LAT_Q", "LATNO3", "GWNO3", "CHOLA", "CBODU", "DOXQ", "TNO3", "QTILE", "TVAP", "YEAR"]
        subdata =pd.DataFrame(columns=names)
        Year = 2015
        with open(subfile) as infile:
            for _ in range(9):
                next(infile)
            for line in infile:
                splitted = []
                txt1 = line[0:6]   ### BIGSUB
                txt2 = line[6:11]   ### SUB
                txt3 = line[11:20]   ### GIS
                txt4 = line[20:25]   ### MON
                txt5 = line[25:35]   ### AREA
                txt6 = line[35:45]   ### PRECIP
                txt7 = line[45:55]   ### SNOMELT
                txt8 = line[55:65]   ### PET
                txt9 = line[65:75]   ### ET
                txt10 = line[75:85]   ### SW
                txt11 = line[85:95]   ### PREC
                txt12 = line[95:105]   ### SURQ
                txt13 = line[105:115]   ### GW_Q
                txt14 = line[115:125]   ### WYLD
                txt15 = line[125:135]   ### SYLD
                txt16 = line[135:145]   ### ORGN
                txt17 = line[145:155]   ### ORGP
                txt18 = line[155:165]   ### NSURQ
                txt19 = line[165:175]   ### SOLP
                txt20 = line[175:185]   ### SEDP
                txt21 = line[185:195]   ### LAT_Q
                txt22 = line[195:205]   ### LATNO5
                txt23 = line[205:215]   ### GWNO5
                txt24 = line[215:226]   ### CHOLA
                txt25 = line[226:236]   ### CBODU
                txt26 = line[236:246]   ### DOXQ
                txt27 = line[246:256]   ### TNO5
                txt28 = line[256:266]   ### QTILE
                txt29 = line[266:276]   ### TVAP

                splitted.append(txt1.strip())
                splitted.append(int(txt2.strip()))
                splitted.append(int(txt3.strip()))
                # print(txt1.strip(),txt2.strip(),txt3.strip(),txt4.strip(),txt5.strip(),txt6.strip(),txt7.strip()
                #       ,txt8.strip(),txt9.strip(),txt10.strip(),txt11.strip(),txt12.strip(),txt13.strip(),txt14.strip()
                # ,txt15.strip(),txt16.strip(),txt17.strip(),txt18.strip(),txt19.strip(),txt20.strip(),txt21.strip()
                #       ,txt22.strip(),txt23.strip(),txt24.strip(),txt25.strip(),txt26.strip(),txt27.strip(),txt28.strip()
                #       ,txt29.strip())
                splitted.append(int(txt4.strip()))
                splitted.append(float(txt3.strip()))
                splitted.append(float(txt6.strip()))
                splitted.append(float(txt7.strip()))
                splitted.append(float(txt8.strip()))
                splitted.append(float(txt9.strip()))
                splitted.append(float(txt10.strip()))
                splitted.append(float(txt11.strip()))
                splitted.append(float(txt12.strip()))
                splitted.append(float(txt13.strip()))
                splitted.append(float(txt14.strip()))
                splitted.append(float(txt15.strip()))
                splitted.append(float(txt16.strip()))
                splitted.append(float(txt17.strip()))
                splitted.append(float(txt18.strip()))
                splitted.append(float(txt19.strip()))
                splitted.append(float(txt20.strip()))
                splitted.append(float(txt21.strip()))
                splitted.append(float(txt22.strip()))
                splitted.append(float(txt23.strip()))
                splitted.append(float(txt24.strip()))
                splitted.append(float(txt25.strip()))
                splitted.append(float(txt26.strip()))
                splitted.append(float(txt27.strip()))
                splitted.append(float(txt28.strip()))
                splitted.append(float(txt29.strip()))

                mon = int(float(txt4.strip()))
                if mon <= 12:
                    splitted.append(Year)
                else:
                    Year = mon+1
                    splitted.append(mon)

                subdata=subdata.append(pd.DataFrame([splitted], columns=subdata.columns))


    else:
        print("Please check path:",subfile)
    return subdata



if __name__=="__main__":
    input = r"D:\PythonPrj\NASA_CMIP6_DS\Data\ACCESS-CM2\output.sub"
    out = sub2db(input)
    out.to_csv("test.csv")