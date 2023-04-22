import numpy as np
import pandas as pd

# 读取Excel文件
df0= pd.read_excel('/Users/ethan/LocalFiles/ProgramsFile/AutomaticOperation/Projects/汇总表格2023-03-14/副本银行网点数据.xlsx', sheet_name='Sheet1',engine='openpyxl')


# 剔除日期的空缺数据
df1 = df0.dropna(axis=0,subset=['批准成立日期'])

# 获取日期和省份的值
df1['year']=df1['批准成立日期'].dt.year
# df1_province=df1['省份'].unique()
# df1['year']=df1['批准成立日期'].dt.year.unique()

sum=df1.groupby(['year','省份']).size()
print(sum)

# # 找到批准成立日期和省份的联合

# sum_year_province=np.ndarray([0,0])
# for y in df1_year:
#     for p in df1_province:
#         sum[y,p] = df1[(df1['批准成立日期']==y) & (df1['省份']==p)]
        



# # 按年份和省份进行分组并汇总数量数据
# result = df.groupby(['批准成立日期', '省份'])['Count'].sum()

# 打印结果
# print(result)
