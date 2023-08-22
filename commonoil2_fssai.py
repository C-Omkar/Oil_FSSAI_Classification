import os
import numpy as np
import pandas as pd
print("Enter Sample Name")
sample_name = input()
print("Enter Percentages of each fatty acid separated by spaces: ")
lst = input().split()
percentages = [float(i) for i in lst]
fattyacids = {}

fattyacids["C_6_0"] = percentages[0]
fattyacids["C_8_0"] = percentages[1]
fattyacids["C_10_0"] = percentages[2]
fattyacids["C_12_0"] = percentages[3]
fattyacids["C_14_0"] = percentages[4]
fattyacids["C_16_0"] = percentages[5]
fattyacids["C_16_1"] = percentages[6]
fattyacids["C_17_0"] = percentages[7] 
fattyacids["C_17_1"] = percentages[8]
fattyacids["C_18_0"] = percentages[9] 
fattyacids["C_18_1"] = percentages[10]
fattyacids["C_18_2"] = percentages[11]
fattyacids["C_18_3"] = percentages[12]
fattyacids["C_20_0"] = percentages[13]
fattyacids["C_20_1"] = percentages[14] 
fattyacids["C_20_2"] = percentages[15]
fattyacids["C_22_0"] = percentages[16]
fattyacids["C_22_1"] = percentages[17]
fattyacids["C_22_2"] = percentages[18] 
fattyacids["C_24_0"] = percentages[19]
fattyacids["C_24_1"] = percentages[20]


oils = ["Groundnut oil", "Coconut oil", "Cottonseed oil", "Maize oil", "Palm oil", "Palm kernel oil", "Palm olein", "Rice bran oil", "Safflowerseed oil", "Safflowerseed oil (high oleic)", "Soyabean oil", "Mustardseed oil", "Rapeseed oil", "Rapeseed oil (low erucic acid)", "Sesameseed oil", "Sunflowerseed oil", "Sunflowerseed oil (high oleic acid)", "Virgin olive oils", "Olive oil (refined olive oil)", "Olive pomace oil (refined olive pomace oil)", "Avocado oil", "Palm stearin", "Palm kernel stearin", "Palm kernel olein", "Palm superlolein", "Chia oil", "Grapeseed oil"]
oil_bounds = {"Groundnut oil" : [
[0, 0.05],
[0,	0.05],
[0,	0.05],
[0,	0.1],
[0,	0.5],
[6,	14],
[0,	0.2],
[0,	0.1],
[0,	0.1],
[0.6, 7],
[35, 69],
[12, 43],
[0,	0.3],
[1,	4],
[0.7, 1.7],
[0,	0.05],
[1.5, 4.5],
[0,	0.3],
[0,	0.05],
[0.5, 2.5],
[0,	0.3],

], "Coconut oil" : [
[0,	1],
[4.0,	10],
[5,	10],
[44.0,	53.2],
[13,	21.9],
[7.5,	11],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[1,	4.9],
[5,	10],
[1,	2.5],
[0,	0.2],
[0,	0.2],
[0,	0.2],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05]

], "Cottonseed oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.2]
,[0.6,	1]
,[21.4,	26.4]
,[0,	1.2]
,[0,	0.1]
,[0,	0.1]
,[2.1,	3.4]
,[14.7,	23.5]
,[46.7,	58.2]
,[0,	0.4]
,[0.2,	0.5]
,[0,	0.1]
,[0,	0.1]
,[0,	0.6]
,[0,	0.3]
,[0,	0.1]
,[0,	0.1]
,[0,	0.05]


], "Maize oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.3]
,[0,	0.3]
,[8.6,	16.5]
,[0,	0.5]
,[0,	0.1]
,[0,	0.1]
,[0,	3.3]
,[20,	42.2]
,[34,	65.6]
,[0,	2]
,[0.3,	1]
,[0.2,	0.6]
,[0,	0.1]
,[0,	0.5]
,[0,	0.3]
,[0,	0.05]
,[0,	0.5]
,[0,	0.05]


], "Palm oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	1.5]
,[0.5,	2]
,[32.0,	47.5]
,[0,	0.6]
,[0,	0.2]
,[0,	0.05]
,[3.5,	6]
,[36,	44]
,[8.5,	12]
,[0,	0.5]
,[0,	1]
,[0,	0.4]
,[0,	0.05]
,[0,	0.2]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]


], "Palm kernel oil" : [
[0,	2.5]
,[2.0,	6.3]
,[2.7,	7]
,[39.7, 55]
,[11.5, 19]
,[6,	14]
,[0,	0.1]
,[0,	0.05]
,[0,	0.05]
,[1,	4]
,[10.5, 24.6]
,[0.5, 4.3]
,[0,	0.3]
,[0,	0.5]
,[0,	0.2]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]


], "Palm olein" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0.1,	0.5]
,[0.5,	1.5]
,[38,	43.5]
,[0,	0.6]
,[0,	0.2]
,[0,	0.1]
,[3.5,	5.4]
,[39.8,	47]
,[10,	13.5]
,[0,	0.6]
,[0,	0.9]
,[0,	0.4]
,[0,	0.05]
,[0,	0.2]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]


], "Rice bran oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.2]
,[0.0,	1.0]
,[14, 23]
,[0,	0.5]
,[0,	0.05]
,[0,	0.05]
,[0.9, 5.2]
,[38, 48]
,[21, 42]
,[0.1, 2.9]
,[0,	0.9]
,[0,	1.1]
,[0,	0.05]
,[0,	1.0]
,[0,	0.05]
,[0,	0.05]
,[0,	0.09]
,[0,	0.05]


], "Safflowerseed oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.2]
,[5.3,	8]
,[0,	0.2]
,[0,	0.1]
,[0,	0.1]
,[1.9,	2.9]
,[8.4,	21.3]
,[67.8,	83.2]
,[0,	0.1]
,[0.2,	0.4]
,[0.1,	0.3]
,[0,	0.05]
,[0,	1]
,[0, 1.8]
,[0,	0.05]
,[0,	0.2]
,[0,	0.2]

    
], "Safflowerseed oil (high oleic)" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.2]
,[0,	0.2]
,[3.6,	6]
,[0,	0.2]
,[0,	0.1]
,[0,	0.1]
,[1.5,	2.4]
,[70,	83.7]
,[9,	19.9]
,[0,	1.2]
,[0.3,	0.6]
,[0.1,	0.5]
,[0,	0.05]
,[0,	0.4]
,[0,	0.3]
,[0,	0.05]
,[0,	0.3]
,[0,	0.3]


], "Soyabean oil": [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.1]
,[0,	0.2]
,[8,	13.5]
,[0,	0.2]
,[0,	0.1]
,[0,	0.1]
,[2,	5.4]
,[17,	30]
,[48,	59]
,[4.5,	11]
,[0.1,	0.6]
,[0,	0.5]
,[0,	0.1]
,[0,	0.7]
,[0,	0.3]
,[0,	0.05]
,[0,	0.5]
,[0,	0.05]


], "Mustardseed oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	1]
,[0.5,	5.0]
,[0,	0.5]
,[0,	0.05]
,[0,	0.05]
,[0.5,	2]
,[8,	23]
,[10,	24]
,[6,	18]
,[0,	1.5]
,[5,	13]
,[0,	1]
,[0.2,	2.5]
,[40, 58.0]
,[0,	1]
,[0,	0.8]
,[0.5,	2.5]


], "Rapeseed oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.2]
,[1.5,	6]
,[0,	3]
,[0, 0.1]
,[0,	0.1]
,[0.5,	3.1]
,[8,	60]
,[11,	23]
,[5,	13]
,[0,	3]
,[3,	15]
,[0,	1]
,[0,	2]
,[2,	60]
,[0,	2]
,[0,	2]
,[0,	3]

    
], "Rapeseed oil (low erucic acid)" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.2]
,[2.5,	7]
,[0,	0.6]
,[0, 0.3]
,[0,	0.3]
,[0.8,	3]
,[51,	70]
,[15,	30]
,[5,	14]
,[0.2,	1.2]
,[0.1,	4.3]
,[0,	0.1]
,[0,	0.6]
,[0,	2]
,[0,	0.1]
,[0,	0.3]
,[0,	0.4]


], "Sesameseed oil": [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	1.5]
,[0,	0.8]
,[7.9,	14.6]
,[0,	0.2]
,[0,	0.2]
,[0,	0.1]
,[2, 8]
,[34.4, 48.0]
,[28, 47.9]
,[0.0,	1]
,[0.1,	0.8]
,[0,	0.5]
,[0,	0.05]
,[0,	1.1]
,[0,	0.05]
,[0,	0.05]
,[0,	0.5]
,[0,	0.05]


], "Sunflowerseed oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.3]
,[0,	0.3]
,[4,	8]
,[0,	0.3]
,[0,	0.2]
,[0,	0.1]
,[1, 7]
,[14,	39.4]
,[48.3,	74]
,[0,	0.3]
,[0.1,	0.5]
,[0,	0.3]
,[0,	0.05]
,[0.3,	1.5]
,[0,	0.3]
,[0,	0.05]
,[0,	0.5]
,[0,	0.5]


], "Sunflowerseed oil (high oleic acid)": [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.1]
,[2.6,	5]
,[0,	0.1]
,[0,	0.1]
,[0,	0.1]
,[2.9,	6.2]
,[75,	90.7]
,[2.1,	17]
,[0,	0.3]
,[0.2,	0.5]
,[0.1,	0.5]
,[0,	0.05]
,[0.5,	1.6]
,[0,	0.3]
,[0,	0.05]
,[0,	0.5]
,[0,	0.05]

], "Virgin olive oils" : [
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0, 0.1],
[7.5,	20],
[0.3, 3.5],
[0,	0.03],
[0,	0.3],
[0.5, 5],
[55, 83],
[2.5, 21],
[0,	0.05],
[0,	0.8],
[0,	0.4],
[0,	0.05],
[0,	0.3],
[0,	0.05],
[0,	0.05],
[0,	1.0],
[0,	0.05]

], "Olive oil (refined olive oil)" : [
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0, 0.1],
[7.5,	20],
[0.3, 3.5],
[0,	0.03],
[0,	0.3],
[0.5, 5],
[55, 83],
[2.5, 21],
[0,	0.05],
[0,	0.8],
[0,	0.4],
[0,	0.05],
[0,	0.3],
[0,	0.05],
[0,	0.05],
[0,	1.0],
[0,	0.05]

], "Olive pomace oil (refined olive pomace oil)" : [
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0, 0.1],
[7.5,	20],
[0.3, 3.5],
[0,	0.03],
[0,	0.3],
[0.5, 5],
[55, 83],
[2.5, 21],
[0,	0.05],
[0,	0.8],
[0,	0.4],
[0,	0.05],
[0,	0.3],
[0,	0.05],
[0,	0.05],
[0,	1.0],
[0,	0.05]

], "Avocado oil" : [
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0, 0.3],
[7.0,	35],
[2.0, 16.8],
[0,	0.3],
[0,	0.3],
[0, 1.5],
[36, 80],
[6, 21.2],
[0,	3.0],
[0,	0.5],
[0,	0.2],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.1],
[0,	0.05]

], "Palm stearin" : [
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0.1, 0.5],
[1, 2],
[48, 74],
[0,	0.2],
[0,	0.2],
[0, 0.1],
[3.9, 6],
[15.5, 36],
[3, 10],
[0,	0.5],
[0,	1.0],
[0,	0.4],
[0,	0.05],
[0,	0.2],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0, 0.05]

], "Palm kernel stearin" : [
[0,	0.2],
[1.3, 3],
[2.4, 3.3],
[52, 59.7],
[20, 25],
[6.7, 10],
[0,	0.05],
[0,	0.05],
[0, 0.05],
[1, 3],
[4.1, 8],
[0.5, 1.5],
[0,	0.1],
[0,	0.5],
[0,	0.1],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0, 0.05]

], "Palm kernel olein" : [
[0,	0.7],
[2.9, 6.3],
[2.7, 4.5],
[39.7, 47],
[11.5, 15.5],
[6.2, 10.6],
[0,	0.1],
[0,	0.05],
[0,	0.05],
[1.7,	3],
[14.4, 24.6],
[2.4, 4.3],
[0,	0.3],
[0,	0.5],
[0,	0.2],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05]

], "Palm superlolein" : [
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0.1,	0.5],
[0.5, 1.5],
[30, 39],
[0,	0.5],
[0,	0.1],
[0,	0.05],
[2.8, 4.5],
[43, 49.5],
[10.5, 15],
[0.2, 1],
[0,	0.4],
[0,	0.2],
[0,	0.05],
[0,	0.2],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05]

], "Chia oil" : [
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0, 0.1],
[6, 8],
[0,	0.5],
[0,	0.05],
[0,	0.05],
[3, 4.5],
[6, 9],
[17, 22],
[58, 65],
[0,	0.5],
[0,	0.05],
[0,	0.05],
[0,	0.2],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05]

], "Grapeseed oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.3]
,[5.5,	11]
,[0, 1.2]
,[0,	0.2]
,[0,	0.1]
,[3,	6.5]
,[12,	28]
,[58,	78]
,[0,	1]
,[0,	1]
,[0,	0.3]
,[0,	0.05]
,[0,	0.5]
,[0,	0.3]
,[0,	0.05]
,[0,	0.4]
,[0,	0.05]
]}


#common_oils = ["Coconut oil", "Mustardseed oil", "Sesameseed oil" ]
common_oils = ["Groundnut oil", "Coconut oil", "Cottonseed oil", "Maize oil", "Palm oil", "Palm kernel oil", "Palm olein", "Rice bran oil", "Safflowerseed oil", "Safflowerseed oil (high oleic)", "Soyabean oil", "Mustardseed oil", "Rapeseed oil", "Rapeseed oil (low erucic acid)", "Sesameseed oil", "Sunflowerseed oil", "Sunflowerseed oil (high oleic acid)", "Virgin olive oils", "Olive oil (refined olive oil)", "Olive pomace oil (refined olive pomace oil)", "Avocado oil", "Palm stearin", "Palm kernel stearin", "Palm kernel olein", "Palm superlolein", "Chia oil", "Grapeseed oil"]


def check_oil(v, o1, o2):
    contain = True
    ctr = 0
    while(contain):
        if(oil_bounds[o1][ctr][0]*v + oil_bounds[o2][ctr][0]*(1-v) <= percentages[ctr] and percentages[ctr] <= oil_bounds[o1][ctr][1]*v + oil_bounds[o2][ctr][1]*(1-v)):
            ctr +=1
            if ctr == 21:
                return True
        else:
            contain = False
            return False


solutions = []

for i in range(27):
    for j in range(i, 27):
                    o1 = oils[i]
                    o2 = oils[j]
                    temp = [o1, o2]
                    temp2 = [*set(temp)]
                    if len(temp) == len(temp2):
                        checkv = np.linspace(0,1, 101)
                        for v in checkv:
                            if check_oil(v, o1, o2):
                                solutions.append([o1, round(100*v, 2), o2, round(100*(1-v), 2)])
                                #  print([o1, round(100*v, 2), o2, round(100*(1-v), 2)])

solutions = np.array(solutions)
print(solutions)
df = pd.DataFrame(solutions)
if os.path.exists("potential_oil2_compositions.xlsx"):
    with pd.ExcelWriter("potential_oil2_compositions.xlsx", mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name=sample_name)     
else:
    df.to_excel("potential_oil2_compositions.xlsx", sheet_name=sample_name)
exit()