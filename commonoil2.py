import numpy as np
import pandas as pd
import os
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


oils = ["Arachis oil", "Babassu oil", "Coconut oil", "Cottonseed oil", "Grapeseed oil", "Maize oil", "Mustardseed oil", "Palm oil", "Palm kernel oil", "Palm olein", "Palm stearin", "Rapeseed oil", "Rapeseed oil (low erucic acid)", "Safflowerseed oil", "Safflowerseed oil (high oleic)", "Sesameseed oil", "Soyabean oil", "Sunflowerseed oil", "Sunflowerseed oil (high oleic acid)"]
oil_bounds = {"Arachis oil" : [
[0, 0.05],
[0,	0.05],
[0,	0.05],
[0,	0.1],
[0,	0.1],
[8,	14],
[0,	0.2],
[0,	0.1],
[0,	0.1],
[1,	4.5],
[35, 69],
[12, 43],
[0,	0.3],
[1,	2],
[0.7, 1.7],
[0,	0.05],
[1.5, 4.5],
[0,	0.3],
[0,	0.05],
[0.5, 2.5],
[0,	0.3],
], "Babassu oil" : [
[0,	0.05],
[2.6, 7.3],
[1.2,	7.6],
[40,	55],
[11,	27],
[5.2,	11],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[1.8,	7.4],
[9,	20],
[1.4,	6.6],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[0,	0.05]


], "Coconut oil" : [
[0,	0.7],
[4.6,	10],
[5,	8],
[45.1,	53.2],
[16.8,	21],
[7.5,	10.2],
[0,	0.05],
[0,	0.05],
[0,	0.05],
[2,	4],
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
,[2.1,	3.3]
,[14.7,	21.7]
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


], "Mustardseed oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	1]
,[0.5,	4.5]
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
,[22,	50]
,[0,	1]
,[0,	0.5]
,[0.5,	2.5]


], "Palm oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.5]
,[0.5,	2]
,[39.3,	47.5]
,[0,	0.6]
,[0,	0.2]
,[0,	0.05]
,[3.5,	6]
,[36,	44]
,[9,	12]
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
[0,	0.8]
,[2.4,	6.2]
,[2.6,	5]
,[45,	55]
,[14,	18]
,[6.5,	10]
,[0,	0.2]
,[0,	0.05]
,[0,	0.05]
,[1,	3]
,[12,	19]
,[1,	3.5]
,[0,	0.2]
,[0,	0.2]
,[0,	0.2]
,[0,	0.05]
,[0,	0.2]
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
,[3.5,	5]
,[39.8,	46]
,[10,	13.5]
,[0,	0.6]
,[0,	0.6]
,[0,	0.4]
,[0,	0.05]
,[0,	0.2]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]


], "Palm stearin" : [
[0,	0.05]
,[0, 0.05]
,[0,	0.05]
,[0.1,	0.5]
,[1,	2]
,[48,	74]
,[0,	0.2]
,[0,	0.2]
,[0,	0.1]
,[3.9,	6]
,[15.5,	36]
,[3,	10]
,[0,	0.5]
,[0,	1]
,[0,	0.4]
,[0,	0.05]
,[0,	0.2]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]


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


], "Sesameseed oil": [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.1]
,[7.9,	12]
,[0.1,	0.2]
,[0,	0.2]
,[0,	0.1]
,[4.8,	6.1]
,[35.9,	42.3]
,[41.5,	47.9]
,[0.3,	0.4]
,[0.3,	0.6]
,[0,	0.3]
,[0,	0.05]
,[0,	0.3]
,[0,	0.05]
,[0,	0.05]
,[0,	0.3]
,[0,	0.05]


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


], "Sunflowerseed oil" : [
[0,	0.05]
,[0,	0.05]
,[0,	0.05]
,[0,	0.1]
,[0,	0.2]
,[5,	7.6]
,[0,	0.3]
,[0,	0.2]
,[0,	0.1]
,[2.7,	6.5]
,[14,	39.4]
,[48.3,	74]
,[0,	0.3]
,[0.1,	0.5]
,[0,	0.3]
,[0,	0.05]
,[0.3,	1.5]
,[0,	0.3]
,[0,	0.3]
,[0,	0.5]
,[0,	0.05]


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
,[0,	0.05]]}

#common_oils = ["Coconut oil", "Mustardseed oil", "Sesameseed oil" ]
common_oils = ["Arachis oil", "Babassu oil", "Coconut oil", "Cottonseed oil", "Grapeseed oil", "Maize oil", "Mustardseed oil", "Palm oil", "Palm kernel oil", "Palm olein", "Palm stearin", "Rapeseed oil", "Rapeseed oil (low erucic acid)", "Safflowerseed oil", "Safflowerseed oil (high oleic)", "Sesameseed oil", "Soyabean oil", "Sunflowerseed oil", "Sunflowerseed oil (high oleic acid)"]


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

for i in range(19):
    for j in range(i, 19):
                    o1 = oils[i]
                    o2 = oils[j]
                    temp = [o1, o2]
                    temp2 = [*set(temp)]
                    if len(temp) == len(temp2):
                        checkv = np.linspace(0,1, 101)
                        for v in checkv:
                            if check_oil(v, o1, o2):
                                solutions.append([o1, round(100*v, 2), o2, round(100*(1-v), 2)])
                                            # print([o1, round(100*v, 2), o2, round(100*w, 2), o3, round(100*(1-v-w), 2)])

solutions = np.array(solutions)
print(solutions)
df = pd.DataFrame(solutions)
if os.path.exists("potential_oil2_compositions.xlsx"):
    with pd.ExcelWriter("potential_oil2_compositions.xlsx", mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name=sample_name)
     
else:
    df.to_excel("potential_oil2_compositions.xlsx", sheet_name=sample_name)
exit()